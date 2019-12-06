# 作者 : lxw
# 文件 : dataDefinitionImpl.py
# 日期 : 2019/12/6 下午5:49
# IDE : PyCharm
# Description : DataDefinition 实现类
# Github : https://github.com/liuxw123

from dataDefinition import DataDefinition
from modelConfig import DELIMITER


class DataDefinitionImplV0(DataDefinition):

    def checkKey(self, key: str):
        version1, sub1, _, dataVersion1 = key.split(DELIMITER)
        version1, sub1, _, dataVersion1 = self.key.split(DELIMITER)

    def getData(self):
        pass
