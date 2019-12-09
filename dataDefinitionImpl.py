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
from values.strings import VERSION_NOT_SUPPORTED

import numpy as np


class DataDefinitionImplV0(DataDefinition):
    """
    TODO right key
    
    v0： 说明这是一个多分类定义模型
    3 ： 三分类
    """
    KEY = "v0-3-x-x"

    def details(self):
        """
        用于后续汇总输出信息时使用，
        :return: 返回出必要的记录信息
        """
        # TODO
        pass

    def __init__(self, train: float) -> None:
        super().__init__()

        assert 0 < train < 1
        self.train = train  # 训练集比例
        self.dataset = DataSet().getData(dim=3)  # 264 * 10 * 16

    def checkKey(self, key: str) -> None:
        """
        check key,查看此类是否能用于目标Key
        :param key: 目标Key
        :return:
        """
        version1, sub1, _, dataVersion1 = key.split(DELIMITER)
        version2, sub2, _, dataVersion2 = DataDefinitionImplV0.KEY.split(DELIMITER)

        if version1 == version2 and sub1 == sub2:
            return
        else:
            raise ValueError(VERSION_NOT_SUPPORTED)

    def getData(self, key: str) -> tuple:
        """
        见父类描述
        :param key: dst key. for check
        :return: 训练所需数据(xTrain, yTrain, xTest, yTest) if checked.
        """
        self.checkKey(key)
        return self.postProcess(self.getXY(self.labelDef()))

    def labelDef(self):
        """
        v0版本的定义位置点所属类
        :return: 分类结果
        """

        # TODO  labels decide by this

        class1 = [x for x in range(0, 61)]
        class2 = [x for x in range(157, 204)]
        class3 = [x for x in range(216, 264)]

        string = "class 1: " + arrayString(class1) + "\n"
        string += "class 2: " + arrayString(class2) + "\n"
        string += "class 3: " + arrayString(class3) + "\n"

        self.string = string

        return class1, class2, class3

    def getXY(self, labelInfo: tuple) -> tuple:
        """
        获取 input data & target data
        :param labelInfo: 分类信息数据
        :return:
        """
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
        """
        随机打乱数据，分出train & test 数据
        :param data: input data & target data
        :return:
        """
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
