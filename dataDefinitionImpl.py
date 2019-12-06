# 作者 : lxw
# 文件 : dataDefinitionImpl.py
# 日期 : 2019/12/6 下午5:49
# IDE : PyCharm
# Description : DataDefinition 实现类
# Github : https://github.com/liuxw123

from dataDefinition import DataDefinition
from modelConfig import DELIMITER


class DataDefinitionImplV0(DataDefinition):
    def toString(self):
        pass

    def details(self):
        pass

    def __init__(self) -> None:
        # TODO  right key
        super().__init__("hints")

    def checkKey(self, key: str):
        version1, sub1, _, dataVersion1 = key.split(DELIMITER)
        version2, sub2, _, dataVersion2 = self.key.split(DELIMITER)

        if version1 == version2 and sub1 == sub2 and dataVersion1 == dataVersion2:
            return
        else:
            raise ValueError("版本不匹配！ 程序退出.")

    def getData(self):
        pass
