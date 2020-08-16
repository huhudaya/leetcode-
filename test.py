# 实现数据可视化中的数据平滑
import numpy as np
import matplotlib.pylab as plt
import pandas as pd

'''
其它的一些知识点：
raise：当程序发生错误，python将自动引发异常，也可以通过raise显示的引发异常
一旦执行了raise语句，raise语句后面的语句将不能执行
'''

# 实现数据可视化中的数据平滑
import numpy as np
import matplotlib.pylab as plt
import csv
from collections import defaultdict
from collections import OrderedDict

import pandas as pd

pd.set_option('display.max_rows', None)


def mapping_cnt(path):
    data = pd.read_csv(path)
    data1 = data["cnt"].values
    data_list = data1.tolist()
    hash = OrderedDict()
    for i in data_list:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1
    hash = sorted(hash.items(), key=lambda x: x[0])
    hash = OrderedDict(hash)
    hash = pd.DataFrame.from_dict(hash, orient='index', dtype=None, columns=None)
    return hash


def moving_average(interval, windowsize):
    window = np.ones(int(windowsize)) / float(windowsize)
    re = np.convolve(interval, window, 'same')
    return re


def LabberRing():
    # t = np.linspace(-4, 4, 100)  # np.linspace 等差数列,从-4到4生成100个数
    # print('t=', t)
    t = np.array(pd.read_csv("20200727.csv")["cnt"])
    # print(t)
    # np.random.randn 标准正态分布的随机数，np.random.rand 随机样本数值
    # y = np.sin(t) + np.random.randn(len(t)) * 0.1  # 标准正态分布中返回1个，或者多个样本值
    # print('y=', y)

    g = mapping_cnt("20200727.csv")
    p = mapping_cnt("20200726.csv")
    m = mapping_cnt("20200725.csv")
    plt.plot(t)
    # plt.plot(t, y, 'k')  # plot(横坐标，纵坐标， 颜色)
    # y_av = moving_average(y, 10)
    # print(y_av)
    # plt.plot(-y_av)
    # plt.plot(t, y_av, 'b')
    plt.xlabel('Time')
    plt.ylabel('Value')
    # plt.grid()  # 网格线设置
    plt.grid(True)
    plt.show()
    return


LabberRing()  # 调用函数
