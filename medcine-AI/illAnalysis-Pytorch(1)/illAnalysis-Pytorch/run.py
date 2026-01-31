# coding: UTF-8
import time
import torch
import numpy as np
from train_eval import train
from importlib import import_module
import argparse

import argparse

# 创建一个ArgumentParser对象，用于从命令行解析参数
parser = argparse.ArgumentParser(description='Chinese Text Classification')

# 添加参数 --model，指定要选择的模型名称
# type=str 表示输入值必须是字符串
# required=True 表示此参数是必需的
# help 提供参数说明
parser.add_argument('--model', type=str, required=True,
                    help='Choose a model: TextCNN, TextRNN, FastText, TextRCNN, TextRNN_Att, DPCNN, Transformer')
# 添加参数 --embedding，指定嵌入方式
# default='pre_trained' 表示默认值为 'pre_trained'，指定语料库
# help 提供参数说明
parser.add_argument('--embedding', default='pre_trained', type=str,
                    help='Embedding type: random or pre_trained')

# 添加参数 --word，用于指定是基于单词还是字符的处理方式
# default=False 表示默认值为 False
# type=bool 表示输入值是布尔类型
# help 提供参数说明
parser.add_argument('--word', default=False, type=bool,
                    help='True for word-level processing, False for character-level processing')

# 解析命令行参数
args = parser.parse_args()



import time
import numpy as np
import torch
from importlib import import_module

if __name__ == '__main__':
    # 指定数据集名称
    dataset = 'THUCNews'  # 数据集名称

    # 指定词嵌入类型
    # 搜狗新闻的预训练词嵌入文件: embedding_SougouNews.npz
    # 腾讯的预训练词嵌入文件: embedding_Tencent.npz
    # 随机初始化词嵌入: random
    embedding = 'embedding_SougouNews.npz'
    if args.embedding == 'random':  # 如果指定使用随机初始化
        embedding = 'random'

    # 获取指定的模型名称
    model_name = args.model  # 可选: TextCNN, TextRNN, FastText, TextRCNN, TextRNN_Att, DPCNN, Transformer

    if model_name == 'FastText':
        # 如果选择的是 FastText 模型，必须使用随机初始化的词嵌入
        embedding = 'random'
    else:
        # 如果选择其他模型，使用通用工具函数
        from utils import build_dataset, build_iterator, get_time_dif

    # 动态导入模型模块，例如 models.TextCNN, models.TextRNN 等
    x = import_module('models.' + model_name)
    # 加载模型的配置类，并传入数据集路径和词嵌入方式
    config = x.Config(dataset, embedding)

    # 设置随机种子，保证结果的可复现性
    np.random.seed(1)  # 设置 NumPy 的随机种子
    torch.manual_seed(1)  # 设置 PyTorch 的随机种子
    torch.cuda.manual_seed_all(1)  # 如果使用多块 GPU，设置所有 GPU 的随机种子
    # 这行代码用于设置 PyTorch 中的 CuDNN 后端为确定性模式，以确保相同输入下的结果可复现（即多次运行代码产生的结果一致）
    torch.backends.cudnn.deterministic = True  # 确保每次运行的结果完全一致

    # 记录起始时间
    start_time = time.time()
    print("Loading data...")

    # 调用工具函数加载数据集
    # vocab: 词汇表
    # train_data, dev_data, test_data: 训练集、验证集、测试集
    vocab, train_data, dev_data, test_data = build_dataset(config, args.word)

    # 构建数据迭代器
    # train_iter: 训练集迭代器
    # dev_iter: 验证集迭代器
    # test_iter: 测试集迭代器
    train_iter = build_iterator(train_data, config)
    dev_iter = build_iterator(dev_data, config)
    test_iter = build_iterator(test_data, config)

    # 计算加载数据的时间消耗
    time_dif = get_time_dif(start_time)
    print("Time usage:", time_dif)

    # 模型训练部分
    # 获取词汇表大小，设置为配置的 n_vocab
    config.n_vocab = len(vocab)

    # 初始化模型，并将其加载到指定设备（CPU/GPU）
    model = x.Model(config).to(config.device)

    # 打印模型的参数信息
    print(model.parameters)

    # 开始训练模型，传入配置对象、模型、以及训练/验证/测试迭代器
    train(config, model, train_iter, dev_iter, test_iter)

