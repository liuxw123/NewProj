# 作者 : lxw
# 文件 : modelDefinitionImpl.py
# 日期 : 2019/12/9 上午9:53
# IDE : PyCharm
# Description : TODO
# Github : https://github.com/liuxw123

from modelDefinition import ModelInterface
from modelConfig import DELIMITER, LAYER
from values.strings import VERSION_NOT_SUPPORTED

from torch import nn


class PstModelV0(ModelInterface, nn.Module):
    # TODO 输入正确的key
    KEY = "v0-0-0-0"

    def creatModel(self, key: str) -> None:
        self.checkKey(key)

        hidden = LAYER
        part = []

        for i in range(len(hidden) - 2):
            inChn = hidden[i]
            outChn = hidden[i + 1]
            part.append(nn.Linear(inChn, outChn))
            part.append(nn.ReLU())

        part.append(nn.Linear(hidden[-2], hidden[-1]))
        part.append(nn.Softmax())

        self.model = nn.ModuleList(part)

    def checkKey(self, key: str) -> None:

        version1, sub1, modelVersion1, _ = key.split(DELIMITER)
        version2, sub2, modelVersion2, _ = PstModelV0.KEY.split(DELIMITER)

        # TODO check key
        if version1 == version2 and sub1 == sub2 and modelVersion1 == modelVersion2:
            return
        else:
            raise ValueError(VERSION_NOT_SUPPORTED)

    def details(self):
        # TODO
        pass

    def forward(self, x):

        for layer in self.model:
            x = layer(x)

        return x
