# 作者 : lxw
# 文件 : modelDefinition.py
# 日期 : 2019/12/4 18:35
# IDE : PyCharm
# Description : 定义 NN
# Github : https://github.com/liuxw123

from torch import nn
from modelConfig import DELIMITER, LAYER


class PstModel(nn.Module):

    def __init__(self, key) -> None:
        super().__init__()
        self.model = None

        self.createModel(key)

    def createModel(self, key: str):
        """
        确定方法创建model
        :param key:
        :return:
        """
        if key.startswith("v0"):
            self.modelV0()

    def modelV0(self):
        """
        v0版本的model创建
        :param key:
        :return:
        """
        hidden = LAYER
        part = []

        for i in range(len(hidden) - 2):
            inChn = hidden[i]
            outChn = hidden[i + 1]
            part.append(nn.Linear(inChn, outChn))
            part.append(nn.ReLU())

        part.append(nn.Linear(hidden[-2], hidden[-1]))
        part.append(nn.Softmax())

        self.model = nn.ModuleList(part)

    def forward(self, x):
        """

        :param x: input data
        :return:
        """
        for layer in self.model:
            x = layer(x)
        return x
