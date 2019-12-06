# 作者 : lxw
# 文件 : modelConfig.py
# 日期 : 2019/12/4 18:52
# IDE : PyCharm
# Description : model configuration
# Github : https://github.com/liuxw123

from common import *

DELIMITER = "-"

#  ---------------------v0--------------------------
"""
    version: v0-0-0-0
    description: v0版本主要思想是将264个点划分成N块区域，SUB_VERSION决定N取值，输入的数据是
                 每个点的响应数据，标签数据是对应所属区域的编号,具体划分请见dataDefinition.py文件
    input data:
        x: 16
        y: one-hot 3 classes
"""

# head version. priority is highest
VERSION = "v0"
# sub version. priority is 2nd
SUB_VERSION = "0"
# model version. use to definition nn model.
MODEL_VERSION = "0"
# data process version. specify how to handle data. 微调
DATA_PROCESS_VERSION = "0"
# Key
KEY = VERSION + DELIMITER + SUB_VERSION + DELIMITER + MODEL_VERSION + DELIMITER + DATA_PROCESS_VERSION

# data handle details
NUM_CLASS = [3, 4, 5]  # which num is decision by SUB_VERSION

# model definition
LAYER = [[NUM_ANTENNA * IS_COMPLEX, 32, 64, 128, 128, 48, 20, NUM_CLASS[int(DATA_PROCESS_VERSION)]]]

#  ---------------------v0--------------------------