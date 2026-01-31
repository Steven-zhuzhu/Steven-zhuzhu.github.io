# coding: UTF-8
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn import metrics
import time
from utils import get_time_dif
from tensorboardX import SummaryWriter


def train(config, model, train_iter, dev_iter, test_iter):
    """
    模型训练函数。

    Args:
        config: 配置参数，包括学习率、训练轮数等。
        model: 要训练的神经网络模型。
        train_iter: 训练集的迭代器。
        dev_iter: 验证集的迭代器。
        test_iter: 测试集的迭代器。
    """
    start_time = time.time()  # 记录训练开始时间
    model.train()  # 设置模型为训练模式
    optimizer = torch.optim.Adam(model.parameters(), lr=config.learning_rate)  # 使用 Adam 优化器

    total_batch = 0  # 已训练的 batch 总数
    dev_best_loss = float('inf')  # 验证集上最好的损失值，初始为正无穷大
    writer = SummaryWriter(
        # time.strftime('%m-%d_%H.%M', time.localtime()),这是一个格式化时间的函数，用于生成当前时间的字符串。
        # time.localtime() 获取当前本地时间。
        log_dir=config.log_path + '/' + time.strftime('%m-%d_%H.%M', time.localtime()))  # TensorBoard 日志记录器

    for epoch in range(config.num_epochs):  # 遍历每个 epoch
        print('Epoch [{}/{}]'.format(epoch + 1, config.num_epochs))

        # scheduler.step()  # 调整学习率

        for i, (trains, labels) in enumerate(train_iter):  # 遍历训练集
            outputs = model(trains)  # 前向传播，获取模型输出
            model.zero_grad()  # 清空梯度
            loss = F.cross_entropy(outputs, labels)  # 计算交叉熵损失
            loss.backward()  # 反向传播
            optimizer.step()  # 更新模型参数

            if total_batch % 100 == 0:  # 每 100 个 batch 进行一次验证集测试
                true = labels.data.cpu()  # 获取真实标签，转移到 CPU
                # torch.max 返回一个元组：
                # [0]：每行的最大值（即每个样本对某类别的最高得分）。
                # [1]：每行最大值的索引（即预测类别的索引）。
                predic = torch.max(outputs.data, 1)[1].cpu()  # 获取预测标签
                train_acc = metrics.accuracy_score(true, predic)  # 计算训练集准确率
                dev_acc, dev_loss = evaluate(config, model, dev_iter)  # 验证集上计算损失和准确率

                if dev_loss < dev_best_loss:  # 如果验证集损失减少
                    dev_best_loss = dev_loss  # 更新最优损失
                    torch.save(model.state_dict(), config.save_path)  # 保存当前模型参数
                    improve = '*'  # 表示有提升
                else:
                    improve = ''  # 无提升

                time_dif = get_time_dif(start_time)  # 计算训练耗时
                msg = 'Iter: {0:>6},  Train Loss: {1:>5.2},  Train Acc: {2:>6.2%},  Val Loss: {3:>5.2},  Val Acc: {4:>6.2%},  Time: {5} {6}'
                print(msg.format(total_batch, loss.item(), train_acc, dev_loss, dev_acc, time_dif, improve))

                # 使用 TensorBoard 记录训练过程中的损失和准确率
                writer.add_scalar("loss/train", loss.item(), total_batch)
                writer.add_scalar("loss/dev", dev_loss, total_batch)
                writer.add_scalar("acc/train", train_acc, total_batch)
                writer.add_scalar("acc/dev", dev_acc, total_batch)

                model.train()  # 切换回训练模式

            total_batch += 1  # 更新 batch 数


    writer.close()  # 关闭 TensorBoard 日志记录器
    test(config, model, test_iter)  # 在测试集上评估模型性能


def test(config, model, test_iter):
    """
    测试模型在测试集上的性能。

    Args:
        config: 配置对象，包含超参数和路径设置。
        model: 训练好的模型。
        test_iter: 测试数据的迭代器。
    """
    # 加载训练期间保存的最佳模型参数
    model.load_state_dict(torch.load(config.save_path))

    # 设置模型为评估模式（关闭 Dropout 等训练特性）
    model.eval()

    # 记录开始时间，用于计算测试耗时
    start_time = time.time()

    # 调用 evaluate 函数在测试集上评估模型性能，返回测试集准确率、损失、分类报告和混淆矩阵
    test_acc, test_loss, test_report, test_confusion = evaluate(config, model, test_iter, test=True)

    # 打印测试集损失和准确率
    msg = 'Test Loss: {0:>5.2},  Test Acc: {1:>6.2%}'  # 格式化显示测试损失和准确率
    print(msg.format(test_loss, test_acc))

    # 打印分类指标（Precision, Recall 和 F1-Score）
    print("Precision, Recall and F1-Score...")
    print(test_report)

    # 打印混淆矩阵，显示分类的错误分布
    print("Confusion Matrix...")
    print(test_confusion)

    # 计算并打印测试耗时
    time_dif = get_time_dif(start_time)
    print("Time usage:", time_dif)


def evaluate(config, model, data_iter, test=False):
    """
    评估模型在验证集或测试集上的性能。

    Args:
        config: 配置对象，包含超参数和路径设置。
        model: 待评估的模型。
        data_iter: 数据迭代器，用于提供评估所需的数据。
        test (bool): 是否为测试模式。默认为 False。

    Returns:
        acc: 模型的准确率。
        avg_loss: 平均损失值。
        如果是测试模式，还会返回分类报告和混淆矩阵。
    """
    # 设置模型为评估模式，禁用 Dropout 等训练相关的特性
    model.eval()

    # 累计损失
    loss_total = 0

    # 存储所有预测值
    predict_all = np.array([], dtype=int)

    # 存储所有真实标签
    labels_all = np.array([], dtype=int)

    # 禁用梯度计算，加快评估速度并减少内存占用
    with torch.no_grad():
        for texts, labels in data_iter:  # 遍历数据迭代器中的批次
            outputs = model(texts)  # 获取模型预测输出
            loss = F.cross_entropy(outputs, labels)  # 计算当前批次的交叉熵损失
            loss_total += loss  # 累计损失

            # 将标签和预测值从 GPU 转移到 CPU，并转换为 NumPy 数组
            labels = labels.data.cpu().numpy()  # 获取真实标签
            predic = torch.max(outputs.data, 1)[1].cpu().numpy()  # 获取预测标签

            # 将当前批次的真实标签和预测值追加到总数组中
            labels_all = np.append(labels_all, labels)
            predict_all = np.append(predict_all, predic)

    # 计算整体的准确率
    acc = metrics.accuracy_score(labels_all, predict_all)

    if test:  # 如果处于测试模式，额外返回分类报告和混淆矩阵
        report = metrics.classification_report(
        # 分类报告，包括 Precision、Recall 和 F1-Score
            labels_all,  # 所有真实标签
            predict_all,  # 所有预测标签
            target_names=config.class_list,  # 类别名称列表
            digits=4  # 输出结果保留 4 位小数
        )
        confusion = metrics.confusion_matrix(labels_all, predict_all)  # 混淆矩阵
        return acc, loss_total / len(data_iter), report, confusion

    # 返回准确率和平均损失值
    return acc, loss_total / len(data_iter)
