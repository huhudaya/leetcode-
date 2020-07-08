'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''


# 暴力法 递归，是个很好的框架
def maxProfit(prices):
    res = 0
    for buy in range(len(prices)):
        for sell in range(buy + 1, len(prices)):
            res = max(res, maxProfit(prices[sell + 1:]) + prices[sell] - prices[buy])
    return res


# 备忘录 dp[i] 指从i开始交易最多能赚多少钱
def maxProfit(prices):
    n = len(prices)
    memo = [-1] * n

    def dp(start):
        if start >= n:
            return 0
        if memo[start] != -1:
            return memo[start]
        res = 0
        # 这个初始化赋值很重要
        curMin = prices[start]
        # 这里的for循环指固定 sell
        for sell in range(start + 1, n):
            curMin = min(curMin, prices[sell])
            # 这里指找到第一次卖出去的时候，然后后面的受益为dp[i+1]，递归的时候，需要有从上往下的思维，而动态规划是从底向上的思维
            res = max(res, dp(sell + 1) + prices[sell] - curMin)
            memo[start] = res
        return res

    return dp(0)


# 贪心
# 贪心算法是基于动态规划之上的一种特殊方法，对于某些特定问题可以比动态规划更高效
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心算法
        res = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res


# 动态规划
import sys


class Solution:
    # 动态规划
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp数组
        dp = [[0, 0] for _ in range(n + 1)]
        # base case 因为k是无限的，所以k次和k-1次效果一样
        dp[0][0] = 0
        dp[0][1] = -sys.maxsize
        # 标准dp模板
        for i in range(1, n + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])  # 当前卖出
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i - 1])  # 当前买入
        return dp[n][0]
