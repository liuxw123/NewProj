# 作者 : lxw
# 文件 : dataDefinitionImpl.py
# 日期 : 2019/12/6 下午5:49
# IDE : PyCharm
# Description : DataDefinition 实现类
# Github : https://github.com/liuxw123
from DataOprt.dataset import DataSet
from common import NUM_TIMES, NUM_ANTENNA, IS_COMPLEX
from dataDefinition import DataDefinition
from modelConfig import DELIMITER
from DataOprt.utils import arrayString

import numpy as np


class DataDefinitionImplV0(DataDefinition):

    def toString(self):
        # TODO
        pass

    def details(self):
        # TODO
        pass

    def __init__(self, train) -> None:
        # TODO  right key
        super().__init__("v0-0-0-0")

        self.train = train
        self.string = ""
        self.dataset = DataSet().getData(dim=3)  # 264 * 10 * 16

    def checkKey(self, key: str):
        version1, sub1, _, dataVersion1 = key.split(DELIMITER)
        version2, sub2, _, dataVersion2 = self.key.split(DELIMITER)

        if version1 == version2 and sub1 == sub2 and dataVersion1 == dataVersion2:
            return
        else:
            raise ValueError("版本不匹配！ 程序退出.")

    def getData(self, key: str) -> tuple:
        self.checkKey(key)
        return self.postProcess(self.getXY(self.labelDef()))

    def labelDef(self):

        class1 = [x for x in range(0, 61)]
        class2 = [x for x in range(157, 204)]
        class3 = [x for x in range(216, 264)]

        string = "class 1: " + arrayString(class1) + "\n"
        string += "class 2: " + arrayString(class2) + "\n"
        string += "class 3: " + arrayString(class3) + "\n"

        self.string = string

        return class1, class2, class3

    def getXY(self, labelInfo: tuple) -> tuple:

        labels = []
        inData = None
        for k, item in enumerate(labelInfo):
            data = np.ndarray((len(item) * NUM_TIMES, NUM_ANTENNA * IS_COMPLEX))
            for idx, num in enumerate(item):
                data[idx * NUM_TIMES:(idx + 1) * NUM_TIMES] = self.dataset[num]
                labels = labels + [k] * NUM_TIMES

            if inData is None:
                inData = data
            else:
                inData = np.vstack((inData, data))

        return inData, np.asarray(labels)

    def postProcess(self, data):
        xData, yData = data
        dim = xData.ndim
        nSample = xData.shape[0]
        train = int(self.train * nSample)

        random = np.random.permutation(nSample)
        shuffledXData = xData[random]
        shuffledYData = yData[random]

        if dim == 2:
            trainXData = shuffledXData[:train]
            trainYData = shuffledYData[:train]
            testXData = shuffledXData[train:]
            testYData = shuffledYData[train:]

        return trainXData, trainYData, testXData, testYData
