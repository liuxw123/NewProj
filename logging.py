# 作者 : lxw
# 文件 : logging.py
# 日期 : 2019/12/9 上午11:38
# IDE : PyCharm
# Description : 记录训练相关信息
# Github : https://github.com/liuxw123
from abc import ABCMeta, abstractmethod

from commonInterface import Common


class ResultLog(Common, metaclass=ABCMeta):

    def details(self):
        pass

    @abstractmethod
    def logging(self):
        pass
