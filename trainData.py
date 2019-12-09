# 作者 : lxw
# 文件 : trainData.py
# 日期 : 2019/12/4 17:10
# IDE : PyCharm
# Description : 训练时所需要的数据集，继承于torch.utils.data.Dataset
# Github : https://github.com/liuxw123

from torch.utils.data import Dataset

from dataDefinitionImpl import DataDefinitionImplV0

import torch
import numpy as np


class TrainData(Dataset):
    """
    data stream:
                                    TrainData(trainData.py)


    """

    def __init__(self, trainRate: float, key: str) -> None:
        super().__init__()

        # TODO choose right data process class
        self.xTrain, self.yTrain, self.xTest, self.yTest = DataDefinitionImplV0(trainRate).getData(key)

        self.phase = None
        self.xData = None
        self.yData = None
        self.samples = 0

        self.changeToTrainPhase()

    def change(self, phase):

        assert phase in ["train", "test"]

        self.phase = phase

        if self.phase == "train":
            self.xData = self.xTrain
            self.yData = self.yTrain
        else:
            self.xData = self.xTest
            self.yData = self.yTest

        self.samples = self.yData.shape[0]

    def changeToTrainPhase(self):
        self.change("train")

    def changeToTestPhase(self):
        self.change("test")

    def __getitem__(self, index: int):

        assert 0 <= index < self.samples
        return self.xData[index], self.yData[index]

    def __len__(self) -> int:
        return self.samples


def collate(batch):
    xd = None
    yd = None
    for item in batch:
        x, y = item

        if xd is None:
            xd = x
            yd = y
        else:
            xd = np.vstack((xd, x))
            yd = np.hstack((yd, y))

    return torch.tensor(xd, dtype=torch.float), torch.tensor(yd, dtype=torch.long)

# usage
# data = TrainData(0.9, "train", "v0-3-1")
