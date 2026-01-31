import torch
import numpy as np
import os
from importlib import import_module
import pickle as pkl

from torch import tensor
from tqdm import tqdm

from utils import build_vocab

MAX_VOCAB_SIZE = 10000
UNK, PAD = '<UNK>', '<PAD>'




if __name__ == '__main__':
    dataset = 'THUCNews'
    pad_size = 32
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    embedding = 'embedding_SougouNews.npz'
    # 假设您的模型名为 'TextCNN'
    model_name = 'TextCNN'
    x = import_module('models.' + model_name)
    # 加载配置和模型
    config = x.Config(dataset, embedding)
    model = x.Model(config).to(config.device)
    model.eval()
    # 加载模型权重
    model.load_state_dict(torch.load(config.save_path))
    # 输入文本
    text = "持续胸痛，心电图异常，冠脉CTA证实冠脉多处狭窄，确诊冠心病，建议药物治疗及生活方式调整。"

    tokenizer = lambda x: [y for y in x]  # 字符级分词
    vocab = pkl.load(open(config.vocab_path, 'rb'))  # 如果词汇表存在，则加载，，训练保存的词表

    contents = []
    words_line = []
    token = tokenizer(text)
    seq_len = len(token)
    if pad_size:
        if len(token) < pad_size:
            token.extend([PAD] * (pad_size - len(token)))
        else:
            token = token[:pad_size]
            seq_len = pad_size
    # word to id
    for word in token:
        words_line.append(vocab.get(word, vocab.get(UNK)))
    contents.append((words_line, 0, seq_len))


    x = torch.LongTensor([contents[0][0]]).to(device)

    # pad前的长度(超过pad_size的设为pad_size)
    seq_len = torch.LongTensor([contents[0][2]]).to(device)
    # 进行预测
    #print((x,seq_len))
    #print(x.shape)
    print(seq_len.shape)
    test = (x, seq_len)
    print(test)
    output = model(test)
    # 获取最大值的下标
    max_index = torch.argmax(output).item()#转成int

    # 打印最大值下标
    print("预测的类别是:", max_index)
