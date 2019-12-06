# 作者 : lxw
# 文件 : dataDefinition.py
# 日期 : 2019/12/3 17:30
# IDE : PyCharm
# Description : 定义模型标签，应注意所有定义情况，测试结果都应该记录该类中
# Github : https://github.com/liuxw123

from abc import abstractmethod, ABCMeta

from commonInterface import Common


class DataDefinition(Common, metaclass=ABCMeta):

    def __init__(self, key: str) -> None:
        super().__init__(key)

    @abstractmethod
    def getData(self):
        pass

    @abstractmethod
    def postProcess(self):
        pass
