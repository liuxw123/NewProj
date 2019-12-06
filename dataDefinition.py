# 作者 : lxw
# 文件 : dataDefinition.py
# 日期 : 2019/12/3 17:30
# IDE : PyCharm
# Description : 定义模型标签，应注意所有定义情况，测试结果都应该记录该类中
# Github : https://github.com/liuxw123

import numpy as np

from DataOprt.dataset import DataSet
from common import *
from modelConfig import DELIMITER
from commonInterface import Common


from torch.utils.data import Dataset

from abc import abstractmethod, ABCMeta


class DataDefinition(Common, metaclass=ABCMeta):

    def __init__(self, key: str) -> None:
        super().__init__(key)

    @abstractmethod
    def getData(self):
        pass


class MyData:
    def __init__(self, key: str) -> None:
        super().__init__()

        self.key = key
        self.label = MyData.LabelDef(key)
        self.commit = MyData.CommitData(key)

    def getData(self) -> tuple:
        """
        获取xData, yData
        :return: 返回training data
        """
        if self.key.startswith("v0-0-") and self.key.endswith("-0"):
            return self.commit.threeClassZeroTry(self.label.threeClassZeroTry())

    @staticmethod
    def checkKeyVersion(curKey: str, dstKey: str) -> None:
        """
        版本校验
        :param curKey: 当前使用的版本
        :param dstKey: 支持的版本，string
        :return:
        """

        keys1 = curKey.split(DELIMITER)
        keys2 = dstKey.split(DELIMITER)

        # 对比 version sub_version data_process_version
        if keys1[0] == keys2[0] and keys1[1] == keys2[1] and keys1[3] == keys2[3]:
            return
        else:
            raise ValueError("Key不匹配或不支持的类型！程序终止")

    class LabelDef:
        """
        定义标签的类。
        1. 20191203 定义思想： 将264个点，按位置不同，分成几个区域，训练时直接分类成对应区域，后期逐渐划分更多类
            # 命名规则，v0-3-1 v0 定义标签版本， 3 分成3类  1第一次自定义划分
            v0-3-1:见相关函数


        """

        def __init__(self, key: str) -> None:
            super().__init__()
            # key version 标识实验版本
            self.KEY_VERSION = key

        def changeKeyVersion(self, key: str) -> None:
            """
            变更 key version
            :param key:
            :return:
            """
            self.KEY_VERSION = key

        def threeClassZeroTry(self) -> list:
            """
            划分3类,0次尝试

            0 -- 60 划分成I类   61点
            157 -- 203 划分成II类  47点
            216 -- 263 划分成III类  48点
            :return: 返回每类的序号 List<int>
            """

            key = "v0-0-x-0"
            MyData.checkKeyVersion(self.KEY_VERSION, key)

            class1 = [x for x in range(0, 61)]
            class2 = [x for x in range(157, 204)]
            class3 = [x for x in range(216, 264)]

            return [class1, class2, class3]

    class CommitData:

        def __init__(self, key: str) -> None:
            super().__init__()
            # key version 标识实验版本
            self.KEY_VERSION = key
            self.dataset = DataSet().getData(dim=3)  # 264 * 10 * 16

        def changeKeyVersion(self, key: str) -> None:
            """
            变更 key version
            :param key:
            :return:
            """
            self.KEY_VERSION = key

        def threeClassZeroTry(self, labelInfo: list):
            """
            定义标签 v0-3-1

            与LabelDef.version0To3To1对应
            """
            key = "v0-0-x-0"
            MyData.checkKeyVersion(self.KEY_VERSION, key)

            # numClass = len(labelInfo)
            # labels = None  # one-hot labels
            labels = []
            inData = None
            for k, item in enumerate(labelInfo):
                data = np.ndarray((len(item) * NUM_TIMES, NUM_ANTENNA * IS_COMPLEX))
                for idx, num in enumerate(item):
                    data[idx * NUM_TIMES:(idx + 1) * NUM_TIMES] = self.dataset[num]
                    labels = labels + [k] * NUM_TIMES

                # one-hot labels
                # label = np.zeros(numClass)
                # label[k] = 1
                # label = np.tile(label, (data.shape[0], 1))

                if inData is None:
                    # labels = label  # one-hot labels
                    inData = data
                else:
                    # labels = np.vstack((labels, label))  # one-hot labels
                    inData = np.vstack((inData, data))

            return inData, np.asarray(labels)


class PostProcess(Dataset):
    """
    后置处理的类，主要是随机打乱，类型转换，训练集测试集划分等操作，不改变本体数据
    """

    def __init__(self, train: float, key: str) -> None:
        super().__init__()

        self.train = train

        self.myData = MyData(key)
        xd, yd = self.myData.getData()
        self.xData = xd
        self.yData = yd

    def process(self):
        dim = self.xData.ndim
        nSample = self.xData.shape[0]
        train = int(self.train * nSample)
        # test = nSample - train

        random = np.random.permutation(nSample)
        shuffledXData = self.xData[random]
        shuffledYData = self.yData[random]

        if dim == 2:
            trainXData = shuffledXData[:train]
            trainYData = shuffledYData[:train]
            testXData = shuffledXData[train:]
            testYData = shuffledYData[train:]

        return trainXData, trainYData, testXData, testYData

# usage
# dataset = PostProcess(0.9)
# xTrain, yTrain, xTest, yTest = dataset.process()
