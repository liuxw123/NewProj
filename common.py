# 作者 : lxw
# 文件 : common.py
# 日期 : 2019/12/2 11:48
# IDE : PyCharm
# Description : 这是本工程的一些公共设置的配置文件，
# Github : https://github.com/liuxw123


import os


# 解决操作系统之间的差异
if os.name == "nt":
    pass
else:
    pass


# 文件夹相关变量
# 原始数据文件夹
PATH_ORIG_DATA = "DataOprt/data/data"
PATH_POSITION_DATA = "data/position.txt"


# 采集参数有关
# AUserDectection输出的20个用户
NUM_DETECTION_USER = 20
# 采集位置点数
NUM_POINT = 264
# 每个位置点采集次数
NUM_TIMES = 10
# 天线数目
NUM_ANTENNA = 8
# 是个复数
IS_COMPLEX = 2

