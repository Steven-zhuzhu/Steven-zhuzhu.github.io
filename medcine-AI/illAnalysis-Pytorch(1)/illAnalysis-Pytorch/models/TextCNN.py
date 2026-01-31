# coding: UTF-8
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np


class Config(object):

    """配置参数"""
    def __init__(self, dataset, embedding):
        self.model_name = 'TextCNN'
        self.train_path = dataset + '/data/train.txt'                                # 训练集
        self.dev_path = dataset + '/data/dev.txt'                                    # 验证集
        self.test_path = dataset + '/data/test.txt'                                  # 测试集
        # x.strip()：移除字符串首尾的空格或换行符。
        self.class_list = [x.strip() for x in open(
            dataset + '/data/class.txt', encoding='utf-8').readlines()]              # 类别名单
        self.vocab_path = dataset + '/data/vocab.pkl'                                # 词表
        self.save_path = dataset + '/saved_dict/' + self.model_name + '.ckpt'        # 模型训练结果
        self.log_path = dataset + '/log/' + self.model_name
        # 三元运算符：a if () else b
        self.embedding_pretrained = torch.tensor(
            np.load(dataset + '/data/' + embedding)["embeddings"].astype('float32'))\
            if embedding != 'random' else None                                       # 预训练词向量
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')   # 设备

        self.dropout = 0.5                                              # 随机失活
        self.require_improvement = 1000                                 # 若超过1000batch效果还没提升，则提前结束训练
        self.num_classes = len(self.class_list)                         # 类别数
        self.n_vocab = 0                                                # 词表大小，在运行时赋值
        self.num_epochs = 100                                           # epoch数
        self.batch_size = 1                                             # mini-batch大小
        self.pad_size = 32                                              # 每句话处理成的长度(短填长切)
        self.learning_rate = 1e-3                                       # 学习率
        self.embed = self.embedding_pretrained.size(1)\
            if self.embedding_pretrained is not None else 300           # 字向量维度
        self.filter_sizes = (2, 3, 4)                                   # 卷积核尺寸
        self.num_filters = 256                                          # 卷积核数量(channels数)



class Model(nn.Module):
    def __init__(self, config):
        # 初始化模型，配置相关参数
        super(Model, self).__init__()

        # 如果预训练嵌入存在，则使用预训练的词向量
        if config.embedding_pretrained is not None:
            # 使用预训练词向量创建嵌入层，freeze=False表示训练嵌入层的参数
            self.embedding = nn.Embedding.from_pretrained(config.embedding_pretrained, freeze=False)
        else:
            # 如果没有预训练的词向量，随机初始化嵌入层
            # 指定用于填充的词的索引,config.n_vocab - 1表示词汇表中的最后一个索引
            self.embedding = nn.Embedding(config.n_vocab, config.embed, padding_idx=config.n_vocab - 1)

        # 创建多个卷积层，每个卷积层使用不同大小的卷积核（filter_sizes）
        # nn.ModuleList 用来存储多个层
        self.convs = nn.ModuleList(
            [nn.Conv2d(1, config.num_filters, (k, config.embed)) for k in config.filter_sizes])

        # Dropout 层，防止过拟合
        self.dropout = nn.Dropout(config.dropout)

        # 全连接层，输出类别数为 config.num_classes
        self.fc = nn.Linear(config.num_filters * len(config.filter_sizes), config.num_classes)

    def conv_and_pool(self, x, conv):
        # 卷积 + 激活 + 最大池化
        # squeeze(3) 表示去掉第四维（width）的大小为 1 的维度
        x = F.relu(conv(x)).squeeze(3)  # 经过卷积层和 ReLU 激活，去掉多余的维度
        # x.size(2) 表示输入张量的第三维（即特征图的长度或高度）。池化的大小是这个长度，即对每个特征图进行一次全局最大池化操作，将每个特征图的所有值压缩成一个最大值。
        x = F.max_pool1d(x, x.size(2)).squeeze(2)  # 进行最大池化操作，
        return x

    def forward(self, x):
        # 前向传播函数
        # 将输入 x（包括输入的文本 token 序列）传入嵌入层，获取词嵌入表示
        out = self.embedding(x[0])

        # 增加一个维度，表示批次中的单个“通道”
        out = out.unsqueeze(1)

        # 对每个卷积层应用卷积操作 + 池化操作，并将它们的输出拼接
        out = torch.cat([self.conv_and_pool(out, conv) for conv in self.convs], 1)

        # 应用 dropout 防止过拟合
        out = self.dropout(out)

        # 通过全连接层进行最终的分类输出
        out = self.fc(out)
        return out
