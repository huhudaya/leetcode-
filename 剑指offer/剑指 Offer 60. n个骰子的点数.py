'''
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。
输入n，打印出s的所有可能的值出现的概率。

 

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

 

示例 1:

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例 2:

输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
 

限制：

1 <= n <= 11
'''
from typing import List

'''
下面思路可能更容易理解。
n个骰子，一共有6**n种情况
n=1, 和为s的情况有 F(n,s)=1 s=1,2,3,4,5,6
n>1 , F(n,s) = F(n-1,s-1)+F(n-1,s-2) +F(n-1,s-3)+F(n-1,s-4)+F(n-1,s-5)+F(n-1,s-6)
可以看作是从前(n-1)个骰子投完之后的状态转移过来。
其中F（N,S）表示投第N个骰子时，点数和为S的次数
'''


#####动态规划未优化版本
class Solution:
    def twoSum(self, n: int) -> List[float]:
        # dp[i][j] 表示第 i 个阶段点数 j 出现的次数
        dp = [[0 for _ in range(6 * n + 1)] for _ in range(n + 1)]
        for i in range(1, 7):
            dp[1][i] = 1
        # 遍历n个骰子，相当于遍历nums数组，i表示第i个骰子
        for i in range(2, n + 1):
            # 相当于遍历target，j代表当前值的和
            for j in range(i, i * 6 + 1):
                # k代表当前骰子的值
                for k in range(1, 7):
                    if j >= k + 1:
                        # 状态转移方程： i个骰子和为j += i-1个骰子和为j-k + 第i个骰子值为k
                        dp[i][j] += dp[i - 1][j - k]
        res = []
        for i in range(n, n * 6 + 1):
            res.append(dp[n][i] * 1.0 / 6 ** n)
        return res


# 相当于组合背包的组合问题
# 这道题相当于是顺序不同，组合不同的01背包的组合问题，只能使用一次
# 优化的时候要把nums数组放在里面
# 这里的nums数组即[1:n+1]
# 这里的target数组即[n, 6*n+1]
class Solution:
    def twoSum(self, n: int) -> List[float]:
        dp = [0 for _ in range(6 * n + 1)]  # 索引0不取，后面取到最大索引6*n

        for i in range(1, 7):  # 初始化dp，第一轮的抛掷
            dp[i] = 1
        for i in range(2, n + 1):  # 从第二轮抛掷开始算
            # 01背包需要倒着遍历
            for j in range(6 * n, i - 1, -1):  # 第二轮抛掷最小和为2，从大到小更新对应               ##的抛掷次数
                dp[j] = 0  # 每次投掷要从0更新dp[j]大小，点数和出现的次数要重新计算
                for cur in range(1, 7):  # 每次抛掷的点数
                    if j - cur < i - 1:
                        break  # 意思为上一轮的最小点数为i-1
                    dp[j] += dp[j - cur]  # 根据上一轮来更新当前轮数据
        sum_ = 6 ** n  # 一共抛掷了6**n次
        res = []
        for i in range(n, 6 * n + 1):
            res.append(dp[i] * 1.0 / sum_)  # 最终计算结果
        return res


class Solution:
    def twoSum(self, n: int) -> List[float]:
        def diceN(n):
            if n == 1:
                return [0] + [1] * 6
            cnts = diceN(n - 1) + [0] * 6
            for i in range(6 * n, 0, -1):
                cnts[i] = sum(cnts[max(0, i - 6):i])
            return cnts

        return filter(lambda a: a > 0, list(map(lambda a: a / 6 ** n, diceN(n))))