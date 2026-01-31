import re
import sys
import cv2
import pytesseract
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog
import torch
import numpy as np
import os
from importlib import import_module
import pickle as pkl
from torch import tensor
from tqdm import tqdm

from utils import build_vocab


class ORC_UI(QWidget):
    def __init__(self):
        super().__init__()
        self.intUI()

    def intUI(self):
        self.ui = uic.loadUi("./UI/main.ui")
        # 固定窗口大小（例如 800x600）
        self.ui.setFixedSize(1662, 1100)
        # 提取UI文件中的对象
        #print(self.ui.__dict__)
        self.choose_pic = self.ui.choose
        self.upload_pic = self.ui.orc
        self.picture_label = self.ui.picture
        self.recommend_net = self.ui.recommend
        self.choose_pic.clicked.connect(self.chooseImage)
        self.upload_pic.clicked.connect(self.recognizeText)
        self.recommend_net.clicked.connect(self.recommend)

    def chooseImage(self):
        # QFileDialog 是 Qt 提供的一个对话框类，用于让用户选择文件
        options = QFileDialog.Options()
        """
        self: 表示当前对象（即类的实例），用来显示对话框。
        "选择图片文件": 是对话框的标题。
        "": 这是初始的路径，空字符串表示打开文件对话框时没有默认路径。
        "Images (*.png *.xpm *.jpg *.jpeg);;All Files (*)": 这是文件过滤器，指定了文件类型。第一个过滤器让用户只能选择图片文件（.png、.xpm、.jpg、.jpeg），第二个过滤器允许选择所有文件（*）。;; 是分隔符，用来表示多个文件类型过滤器。
        options=options: 将之前创建的 options 参数传递给 QFileDialog，目前为空，意味着没有额外的设置。
        返回值：
        self.filePath 保存用户选择的文件路径。
        _ 用于接收文件对话框返回的过滤器选择（通常用 _ 来表示我们不需要这个值）。
        """
        self.filePath, _ = QFileDialog.getOpenFileName(self, "选择图片文件", "",
                                                       "Images (*.png *.xpm *.jpg *.jpeg);;All Files (*)",
                                                       options=options)
        if self.filePath:
            # QPixmap 是 Qt 中用于处理图像的类。这里，它使用用户选择的文件路径加载图像
            pixmap = QPixmap(self.filePath)  # 替换为你的图片路径
            """
            self.picture_label.setPixmap() 用来设置图片标签（picture_label）显示的图片。
            pixmap.scaled() 将 pixmap（即图片）缩放到标签的尺寸，self.picture_label.size() 返回标签的大小。
            aspectRatioMode=1：这是一个参数，表示保持图像的宽高比进行缩放。
            在 Qt 中，aspectRatioMode=1 对应 Qt.KeepAspectRatio，即图像按比例缩放，确保不变形。
            """
            self.picture_label.setPixmap(pixmap.scaled(self.picture_label.size(), aspectRatioMode=1))  # 设置图片到标签
            print("选择的文件路径:", self.filePath)  # 打印路径


    def recognizeText(self):
        # 设置 Tesseract 的路径
        pytesseract.pytesseract.tesseract_cmd = r'D:\SoftWare\Tesseract-OCR\tesseract.exe'
        # 读取图像并进行OCR识别
        image = cv2.imread(self.filePath)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # 使用 Tesseract 进行文字识别
        self.text = pytesseract.image_to_string(gray_image, lang='chi_sim')
        # 提取检查结论
        self.text = self.text.replace(" ", "")  # 去除多余空格
        print(self.text)
        self.picture_label.setText(self.text)
        self.text = self.text.replace("\n", "")  # 去除换行符

    def recommend(self):
        MAX_VOCAB_SIZE = 10000
        UNK, PAD = '<UNK>', '<PAD>'
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

        tokenizer = lambda x: [y for y in x]  # 字符级分词

        vocab = pkl.load(open(config.vocab_path, 'rb'))  # 如果词汇表存在，则加载

        contents = []# 就一条数据，为了格式统一，加一个维度
        words_line = []
        token = tokenizer(self.text)
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
        contents.append((words_line, 0, seq_len))#  标签设置为0

        x = torch.LongTensor([contents[0][0]]).to(device)

        seq_len = torch.LongTensor([contents[0][2]]).to(device)
        # 进行预测
        # print((x,seq_len))
        # print(x.shape)
        #print(seq_len.shape)
        test = (x, seq_len)
        #print(test)
        output = model(test)
        # 获取最大值的下标
        max_index = torch.argmax(output).item()  # [1]转成int
        # 打印最大值下标
        print("预测的类别是:", max_index)
        self.picture_label.setText(str(max_index))

        #生成推荐内容
        def read_txt_by_index(file_path, index):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # 将整个文件按块分割，以双换行符分割
            blocks = content.split('\n\n')

            # 查找对应数字的块，返回它的内容
            for block in blocks:
                lines = block.split('\n')
                if lines[0] == str(index):
                    return '\n'.join(lines[1:])# 拼接成字符串，最后显示的是字符串
            return None

        # 你可以调用该函数并传入文件路径和数字
        file_path = 'recommend.txt'  # 替换成实际文件路径
        result = read_txt_by_index(file_path, str(max_index))

        self.picture_label.setText(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ORC_UI()
    w.ui.show()
    app.exec_()

