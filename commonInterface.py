# 作者 : lxw
# 文件 : commonInterface.py
# 日期 : 2019/12/6 下午6:49
# IDE : PyCharm
# Description : 此工程的基类接口
# Github : https://github.com/liuxw123
from abc import ABCMeta, abstractmethod


class Common(metaclass=ABCMeta):

    def __init__(self, key: str) -> None:
        super().__init__()
        self.key = None  # 类的唯一使用标识，不匹配，说明此类不可使用
        self.setKey(key)
        self.string = ""

    def setKey(self, key) -> None:
        """
        set key
        :param key: dst key
        :return:
        """
        self.key = key

    def getKey(self) -> str:
        """
        get key
        :return: key
        """
        return self.key

    @abstractmethod
    def checkKey(self, key: str) -> None:
        """
        check key,查看此类是否能用于目标Key，不匹配，说明此类不可使用
        :param key: dst key
        :return:
        """
        pass

    def toString(self):
        """
        描述此类
        :return: 描述信息
        """
        return self.string

    @abstractmethod
    def details(self):
        """
        用于后续汇总输出信息时使用
        :return: 返回出必要的记录信息
        """
        pass
