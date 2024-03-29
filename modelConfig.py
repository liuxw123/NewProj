# 作者 : lxw
# 文件 : modelConfig.py
# 日期 : 2019/12/4 18:52
# IDE : PyCharm
# Description : model configuration
# Github : https://github.com/liuxw123

from values.values import NUM_ANTENNA, IS_COMPLEX
from values.strings import DELIMITER

#  ---------------------v0--------------------------

# description
# head version. priority is highest
VERSION = "v0"  # v0 是个简单的多分类模型
# sub version. priority is 2nd
SUB_VERSION = "3"  # 根据VERSION而定，此版本是个3分类
# model version. use to definition nn model.
MODEL_VERSION = "0"  # 指定model版本
# data process version. specify how to handle data. 微调
DATA_PROCESS_VERSION = "0"  # 处理数据的版本， 一般数据微调整更改
# Key
KEY = VERSION + DELIMITER + SUB_VERSION + DELIMITER + MODEL_VERSION + DELIMITER + DATA_PROCESS_VERSION

# 下面字段由KEY决定
NUM_CLASS = 3  # 3 分类
LAYER = [NUM_ANTENNA * IS_COMPLEX, 32, 64, 128, 128, 48, 20, NUM_CLASS]  # hidden layer

#  ---------------------v0--------------------------
