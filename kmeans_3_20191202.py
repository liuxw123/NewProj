# 作者 : lxw
# 文件 : kmeans_3_20191202.py
# 日期 : 2019/12/2 19:12
# IDE : PyCharm
# Description : 使用K-Means算法，将数据分为3类
# Github : https://github.com/liuxw123

from sklearn.cluster import KMeans

from DataOprt.dataset import DataSet

import numpy as np

data = np.ndarray((200, 2))

for i in range(100):
    i1 = i*2
    y1 = i1*i1
    i2 = i
    y2 = i2*i2*i2
    data[2*i, 0] = i1
    data[2*i, 1] = y1

    data[2*i+1, 0] = i2
    data[2*i+1, 1] = y2


dataset = DataSet()

model = KMeans(n_clusters=10)
model.fit(dataset.getData())

predict = model.predict(dataset.getData())

model = KMeans(n_clusters=2)
model.fit(data)

allPred = model.predict(data)



