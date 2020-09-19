'''
已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数
，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数

不要使用系统的 Math.random() 方法。

示例 1:

输入: 1
输出: [7]
示例 2:

输入: 2
输出: [8,4]
示例 3:

输入: 3
输出: [8,1,10]
 

提示:

rand7 已定义。
传入参数: n 表示 rand10 的调用次数。

进阶:
rand7()调用次数的 期望值 是多少 ?
你能否尽量少调用 rand7() ?

'''

from random import randint
def rand7():
    return randint(1, 7)

class Solution:
    def rand10(self):
        x = 50
        # 为什么要大于40，这是因为需要等概率！所以需要1-10，而我们得到的x的范围为1-49，需要拒绝40-49
        # 这样得到的数据就是0-39，然后对10取余，然后+1就可以得到rand10的等概率值
        while x > 40:
            x = (rand7() - 1) * 7 + rand7()
        return x % 10 + 1

