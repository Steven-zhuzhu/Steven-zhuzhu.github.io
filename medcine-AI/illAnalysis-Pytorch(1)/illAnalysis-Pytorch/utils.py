# coding: UTF-8
import os
import torch
import numpy as np
import pickle as pkl
from tqdm import tqdm
import time
from datetime import timedelta


MAX_VOCAB_SIZE = 10000  # 词表长度限制
UNK, PAD = '<UNK>', '<PAD>'  # 未知字，padding符号


def build_vocab(file_path, tokenizer, max_size, min_freq):
    """
    构建词汇表（vocabulary dictionary）。

    参数：
    - file_path: str，数据文件的路径，每行包含文本和标签，格式为 "文本\t标签"。
    - tokenizer: function，用于分词的函数，例如将句子切分为单词或字符。
    - max_size: int，词汇表的最大大小。
    - min_freq: int，词语在语料中出现的最小频率，小于该频率的词语会被过滤掉。

    返回：
    - vocab_dic: dict，词汇表，键是词语，值是词语对应的索引。
    """
    vocab_dic = {}  # 用于存储词语及其出现频率的字典

    # 打开文件，逐行读取
    with open(file_path, 'r', encoding='UTF-8') as f:
        for line in tqdm(f):  # 使用 tqdm 显示处理进度条
            lin = line.strip()  # 去掉每行首尾的空格和换行符
            if not lin:  # 如果行为空，跳过
                continue
            content = lin.split('\t')[0]  # 按 '\t' 分割行，获取文本部分（忽略标签部分）
            for word in tokenizer(content):  # 使用 tokenizer 对文本进行分词
                # vocab_dic.get(word, 0)：使用 get 方法检查 vocab_dic 字典中是否已经存在当前的 word（即当前词）。
                # 如果存在该词，get 返回该词的当前频率（即字典中的值）。
                # 如果不存在该词，get 返回默认值 0。
                vocab_dic[word] = vocab_dic.get(word, 0) + 1  # 更新词频统计

        # 按频率过滤词语并排序，保留频率 >= min_freq 的词
        vocab_list = sorted(
            # vocab_dic 是一个字典，保存了每个词和其出现的次数（词频）。vocab_dic.items() 返回字典的 键值对，即 (word, frequency) 的元组列表。
            [item for item in vocab_dic.items() if item[1] >= min_freq],
            # key=lambda x: x[1] 指定排序的依据是每个元组的第二个元素（即词频）。
            key=lambda x: x[1],  # 按词频排序
            reverse=True  # 从高到低排序
        )[:max_size]  # 截取词汇表的最大大小

        # 将词汇表的词语分配索引，从 0 开始,抛去频率
        # [('word1', 10), ('word2', 5), ('word3', 3)]
        # {'word1': 0, 'word2': 1, 'word3': 2}
        vocab_dic = {word_count[0]: idx for idx, word_count in enumerate(vocab_list)}

        # 添加特殊标记 UNK（未知词）和 PAD（填充词）到词汇表
        # vocab_dic = {'word1': 0, 'word2': 1, 'word3': 2}
        #{'word1': 0, 'word2': 1,  'word3': 2, 'UNK': 3, 'PAD': 4}
        vocab_dic.update({UNK: len(vocab_dic), PAD: len(vocab_dic) + 1})

    return vocab_dic  # 返回构建的词汇表



def build_dataset(config, ues_word):
    """
    构建数据集，包括加载词汇表和处理训练集、验证集、测试集。

    参数：
    - config: 配置对象，包含数据路径、词汇表路径等信息。
    - ues_word: 布尔值，表示是否使用词级别的分词。如果为 True，使用词级别分词，否则使用字符级别分词。

    返回：
    - vocab: 词汇表字典，包含词到索引的映射。
    - train: 训练集数据，列表形式，每个元素是 (词语索引序列, 标签, 序列长度)。
    - dev: 验证集数据，格式同上。
    - test: 测试集数据，格式同上。
    """
    # 根据是否使用词级别的分词，选择合适的分词器
    if ues_word:
        tokenizer = lambda x: x.split(' ')  # 以空格分割，词级别分词
    else:
        # [y for y in x]: 这是一个列表推导式，用于遍历 x 中的每个字符，并将这些字符放入一个新的列表中。
        tokenizer = lambda x: [y for y in x]  # 字符级别分词，即按字符分割
    # 如果词汇表已存在，加载词汇表；否则，重新构建词汇表并保存
    if os.path.exists(config.vocab_path):
        vocab = pkl.load(open(config.vocab_path, 'rb'))  # 从文件中加载词汇表
    else:
        # 如果词汇表不存在，构建新的词汇表并保存
        vocab = build_vocab(config.train_path, tokenizer=tokenizer, max_size=MAX_VOCAB_SIZE, min_freq=1)
        # pkl.dump(data, f) 将 data 对象序列化并写入到文件 f 中
        pkl.dump(vocab, open(config.vocab_path, 'wb'))  # 保存词汇表到文件
    print(f"Vocab size: {len(vocab)}")  # 输出词汇表大小

    # 定义加载数据集的函数
    def load_dataset(path, pad_size=32):
        """
        加载数据集，处理文本和标签，并进行分词和填充。

        参数：
        - path: 数据文件路径，格式为每行 "文本\t标签"。
        - pad_size: 填充长度，默认32。

        返回：
        - contents: 处理后的数据集，每个元素是一个元组 (词语索引序列, 标签, 序列长度)。
        """
        contents = []  # 存储处理后的数据
        with open(path, 'r', encoding='UTF-8') as f:
            for line in tqdm(f):  # 使用 tqdm 显示读取进度
                lin = line.strip()  # 去掉行首尾空格
                if not lin:  # 跳过空行
                    continue
                if len(lin.split('\t')) != 2:  # 如果一行数据格式不正确（不是两个部分），跳过
                    print(f"Warning: Line skipped due to unexpected format: {lin}")
                content, label = lin.split('\t')  # 拆分文本和标签
                words_line = []  # 存储该行文本的词语索引
                token = tokenizer(content)  # 对文本进行分词
                seq_len = len(token)  # 获取分词后的长度（序列长度）
                if pad_size:
                    # 如果序列长度小于 pad_size，进行填充；否则，截断
                    if len(token) < pad_size:
                        token.extend([PAD] * (pad_size - len(token)))  # 填充
                    else:
                        token = token[:pad_size]  # 截断
                        seq_len = pad_size  # 更新序列长度为填充后的长度
                # 将分词后的词语转换为词汇表中的索引
                for word in token:
                    words_line.append(vocab.get(word, vocab.get(UNK)))  # 如果词不在词汇表中，使用 UNK 索引
                # 添加处理后的数据到 contents 列表
                contents.append((words_line, int(label), seq_len))  # (词语索引序列, 标签, 序列长度)

        return contents  # 返回处理后的数据集，形式为 [(词语索引序列, 标签, 序列长度), ...]

    # 加载训练集、验证集和测试集
    train = load_dataset(config.train_path, config.pad_size)
    dev = load_dataset(config.dev_path, config.pad_size)
    test = load_dataset(config.test_path, config.pad_size)

    return vocab, train, dev, test  # 返回词汇表和数据集


class DatasetIterater(object):
    def __init__(self, batches, batch_size, device):
        self.batch_size = batch_size  # 每个批次的大小
        self.batches = batches  # 数据集的所有数据
        self.n_batches = len(batches) // batch_size  # 计算总批次数
        self.residue = False  # 记录是否有剩余的数据（数据量无法整除批次大小）

        # 如果数据集大小不能整除批次大小，那么就有剩余数据
        if len(batches) % self.n_batches != 0:
            self.residue = True

        self.index = 0  # 当前处理的批次索引
        self.device = device  # 数据存放的设备（如 CPU 或 GPU）

    def _to_tensor(self, datas):
        # 将数据转换为 Tensor，并放到指定的设备上
        # 从 datas 中提取每个样本的输入数据（x）、标签（y）和序列长度（seq_len）
        x = torch.LongTensor([_[0] for _ in datas]).to(self.device)
        y = torch.LongTensor([_[1] for _ in datas]).to(self.device)
        seq_len = torch.LongTensor([_[2] for _ in datas]).to(self.device)

        # 返回输入数据（x，seq_len）和标签（y）
        return (x, seq_len), y

    def __next__(self):
        # 迭代器的下一个批次
        # 如果有剩余数据，并且当前是最后一个批次，处理剩余的数据
        if self.residue and self.index == self.n_batches:
            batches = self.batches[self.index * self.batch_size: len(self.batches)]  # 取剩余的数据
            self.index += 1
            batches = self._to_tensor(batches)  # 转换为 Tensor 格式
            return batches

        # 如果已经迭代完成所有批次，重置索引并停止迭代
        elif self.index >= self.n_batches:
            self.index = 0
            raise StopIteration

        # 否则正常返回当前批次的数据
        else:
            batches = self.batches[self.index * self.batch_size: (self.index + 1) * self.batch_size]  # 获取当前批次的数据
            self.index += 1
            batches = self._to_tensor(batches)  # 转换为 Tensor 格式
            return batches

    def __iter__(self):
        # 使得 DatasetIterater 对象本身成为可迭代对象
        return self

    def __len__(self):
        # 返回迭代器的长度，即批次数量
        if self.residue:
            return self.n_batches + 1  # 如果有剩余数据，返回总批次 + 1
        else:
            return self.n_batches  # 否则返回完整的批次数量


def build_iterator(dataset, config):
    iter = DatasetIterater(dataset, config.batch_size, config.device)
    return iter


def get_time_dif(start_time):
    """获取已使用时间"""
    end_time = time.time()
    time_dif = end_time - start_time
    # 四舍五入之后转换成秒
    return timedelta(seconds=int(round(time_dif)))



