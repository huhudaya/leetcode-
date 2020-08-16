import numpy as np
import matplotlib.pylab as plt
import pandas as pd
from scipy.stats import normaltest
from scipy.stats import shapiro
from scipy.stats import kstest
if __name__ == '__main__':
    s = pd.read_csv('20200725.csv')["cnt"]
    print(s)
    # s = pd.DataFrame(np.array([1.998,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2.002]))
    #同过对数函数将偏态分布转换成正态分布
    # s=np.log(s)
    # u=0
    # δ = 1  # 标准差δ
    # s = pd.DataFrame(np.linspace(u - 4 * δ, u + 4 * δ, 30))
    # print(s)

    # s=transToNormal(s,np.mean(s),np.std(s))

    print("SKEW:%f" % s.skew())  # 偏度计算
    print("KERT:%f" % s.kurt())  # 峰度计算
    print("MEAN:%f" % np.mean(s))
    print("VAR:%f" % np.var(s))
    print("STD:%f" % np.std(s))

    # 绘制直方图
    fig = plt.figure(figsize=(16, 9))
    ax2 = fig.add_subplot(1, 1, 1)
    s.hist(bins=30, alpha=1, ax=ax2)
    s.plot(kind='kde', secondary_y=True, ax=ax2)
    plt.grid()
    plt.show()

    # 假设检验
    p = shapiro(s)
    print(normaltest(s))
    print(p)