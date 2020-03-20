'''
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的
'''

'''
# 伪码框架
def coinChange(coins: List[int], amount: int):
    # 定义：要凑出金额 n，至少要 dp(n) 个硬币
    def dp(n):
        # 做选择，选择需要硬币最少的那个结果
        for coin in coins:
            res = min(res, 1 + dp(n - coin))
        return res
    # 我们要求的问题是 dp(amount)
    return dp(amount)
最后明确 base case，显然目标金额为 0 时，所需硬币数量为 0；当目标金额小于 0 时，无解，返回 -1：
时间复杂度分析：子问题总数 x 每个子问题的时间。
子问题总数为递归树节点个数，这个比较难看出来，是 O(n^k)，总之是指数级别的。每个子问题中含有一个 for 循环，复杂度为 O(k)。所以总时间复杂度为 O(k * n^k)，指数级别
'''
# 暴力递归
from typing import List


def coinChange(coins: List[int], amount: int):
    def dp(n):
        # base case
        if n == 0:
            return 0
        if n < 0:
            return -1
        # 求最小值，所以初始化为正无穷
        res = float('INF')
        for coin in coins:
            subproblem = dp(n - coin)
            # 子问题无解，跳过
            if subproblem == -1:
                continue
            res = min(res, 1 + subproblem)

        return res if res != float('INF') else -1

    return dp(amount)


# 备忘录
def coinChange(coins: List[int], amount: int):
    # 备忘录
    memo = dict()

    def dp(n):
        # 查备忘录，避免重复计算
        if n in memo:
            return memo[n]

        if n == 0:
            return 0
        if n < 0:
            return -1
        res = float('INF')
        for coin in coins:
            subproblem = dp(n - coin)
            if subproblem == -1:
                continue
            res = min(res, 1 + subproblem)
        # 记入备忘录
        memo[n] = res if res != float('INF') else -1
        return memo[n]

    return dp(amount)


# dp[i] = x表示，当目标金额为i时，至少需要x枚硬币。
'''
PS：为啥dp数组初始化为amount + 1呢
因为凑成amount金额的硬币数最多只可能等于amount（全用 1 元面值的硬币）
所以初始化为amount + 1就相当于初始化为正无穷，便于后续取最小值
'''
# 动态规划
class Solution:
    def coinChange(self, coins: List[int], amount: int):
        # 初始化为 amount + 1
        dp = [amount + 1 for i in range(amount + 1)]
        dp[0] = 0
        # 计算dp的每一个值 从dp[i] i=0开始
        for i in range(amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if dp[amount] != amount + 1 else -1
