'''
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
'''
from typing import List
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 定义dp数组
        n = len(prices)
        dp = [[0, 0] for _ in range(n + 1)]
        # 定义base case
        dp[0][0] = 0
        dp[0][1] = -sys.maxsize
        for i in range(1, n + 1):
            if i - 2 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[0] #这里表示第一天买入
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1]) #当前卖出
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i - 1]) #当前买入
        return dp[n][0]
print(Solution().maxProfit([1,2]))