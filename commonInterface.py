# 作者 : lxw
# 文件 : commonInterface.py
# 日期 : 2019/12/6 下午6:49
# IDE : PyCharm
# Description : TODO
# Github : https://github.com/liuxw123
from abc import ABCMeta, abstractmethod


class Common(metaclass=ABCMeta):

    def __init__(self, key: str) -> None:
        super().__init__()
        self.key = None
        self.setKey(key)

    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    @abstractmethod
    def checkKey(self, key: str):
        pass

    @abstractmethod
    def toString(self):
        pass

    @abstractmethod
    def details(self):
        pass

