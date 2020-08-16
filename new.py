# 实现数据可视化中的数据平滑
import numpy as np
import matplotlib.pylab as plt
import csv
from collections import defaultdict
from collections import OrderedDict

import pandas as pd

pd.set_option('display.max_rows', None)


def mapping_cnt():
    data = pd.read_csv("a.csv")
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
mapping_cnt()
