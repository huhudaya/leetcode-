'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
'''

# dp[i][j][K] ：表示到第 i 天为止，已经交易了 j 次，并且当前持股状态为 K 的最大收益。
from typing import List
import sys
import numpy as np


class Solution:
    # 使用递归 备忘录 会超时
    def maxProfit1(self, prices: List[int]) -> int:
        # n = len(prices)
        memo = dict()
        num = 2

        def dp(start, k):
            if start >= len(prices):
                return 0
            # 注意一定要判断k==0
            if k == 0:
                return 0
            if (start, k) in memo:
                return memo[(start, k)]
            res = 0
            curMin = prices[start]
            # 从start + 1开始卖股票
            for sell in range(start + 1, len(prices)):
                curMin = min(curMin, prices[sell])
                # 我特么这里sell + 1 写成了 start + 1，你敢信？？？
                res = max(dp(sell + 1, k - 1) + prices[sell] - curMin, res)
            memo[(start, k)] = res
            return res

        return dp(0, num)

    # 使用状态机
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        k = 2
        # dp数组 需要长度+1
        dp = np.zeros((n + 1, k + 1, 2), dtype=np.int)
        # dp = [[[0, 0, 0], [0, 0, 0]] for i in range(n)]
        # dp = [[[0] * 2 for _ in range(3)] for _ in range(n + 1)]
        # base case
        for j in range(k + 1):
            dp[0][j][0] = 0
            dp[0][j][1] = -sys.maxsize
        for i in range(n + 1):
            dp[i][0][0] = 0
            dp[i][0][1] = -sys.maxsize
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                print("src:"+"i=\t"+str(i)+'\t'+"j=\t"+str(j)+"\t"+"dp=\t"+str(dp[i][0][0]))
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i - 1])  # 当前卖出
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i - 1])  # 当前买入，所以消耗一次机会
                print("des:"+"i=\t"+str(i)+'\t'+"j=\t"+str(j)+"\t"+"dp=\t"+str(dp[i][0][0]))
        return int(dp[n][k][0])  # 这里需要转成int类型输出


print(Solution().maxProfit([1, 2, 3, 4, 5]))

'''
动态规划+股票交易+k=2:dp[i][k][0 or 1]表示第i天，最多可完成k笔交易时，是（1）否（0）持有股票时，的最大利润。
状态转移方程：
dp[i][k][0]=max(dp[i-1][k][0],dp[i-1][k][1]+prices[i]) ，第i天未持有：（1）第i-1天未持有，（2）第i-1天持有，第i天卖出,赚钱第i天利润
dp[i][k][1]=max(dp[i-1][k][1],dp[i-1][k-1][0]-prices[i]) ,第i天持有：（1）第i-1天持有，（2）第i-1天未持有，第i天买入，买入时需要消耗一次k，成本为prices[i]
k从1开始，因为dp[i][0][0 or 1]表示最多可进行0笔交易，不论什么时候结果都是0
初始化
dp[0][k][1]=dp[1][k][1]第0天不可能有一次交易,设为负无穷float("-inf")
时间复杂度：O（2n） ，每一天都要判断k=2次，一共n天
空间复杂度：O（2kn） ，dp一共要占用这么2kn个空间

class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        if n < 1:
            return 0
        dp = [[[0]*2 for _ in range(3)] for _ in range(n+1)]
        for k in range(3):
            dp[0][k][1] = float('-inf')
        for i in range(1, n+1):
            for k in range(1, 3):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1]+prices[i - 1])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0]-prices[i - 1])
        return dp[n][2][0]

卖出时算做交易
上面是在买入时减少k
如果直接修改成dp[i][k][0] = max(dp[i-1][k][0],dp[i-1][k-1][1]+prices[i-1])结果不对。
原因在于若买入不消耗交易次数，则可以在k=0时买入，需要对k=0多做一步初始化。其他不变，循环内部修改如下即可。

for i in range(1,n+1):
    for k in range(3):
        dp[i][0][0] = 0
        dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k-1][1]+prices[i-1]) 
        dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k][0]-prices[i-1])
return dp[n][2][0]
代码
class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        if n < 1:
            return 0
        dp = [[[0]*2 for _ in range(3)] for _ in range(n+1)]
        for k in range(3):
            dp[0][k][1] = float('-inf')
        for i in range(1, n+1):
            # 卖出时才算交易的话，意味着当k=0的时候，也是可以进行交易的
            for k in range(3):
                # 卖出时算一个交易次数
                dp[i][0][0] = 0
                dp[i][k][0] = max(dp[i-1][k][0],dp[i-1][k-1][1]+prices[i-1])
                dp[i][k][1] = max(dp[i-1][k][1],dp[i-1][k][0]-prices[i-1])
        return dp[n][2][0]





优化
dp[i]仅与dp[i-1]有关，可降维
dp[k][0] = max(dp[k][0],dp[k][1]+prices[i-1])
dp[k][1] = max(dp[k][1],dp[k-1][0]-prices[i-1])
时间复杂度：O（2n），空间复杂度：O（1），只需要6的常数空间。
代码
class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[0]*2 for _ in range(3)]
        for k in range(3):
            dp[k][1] = float('-inf')
        for i in range(1, n+1):
            for k in range(1,3):
                dp[k][0] = max(dp[k][0],dp[k][1]+prices[i-1])
                dp[k][1] = max(dp[k][1],dp[k-1][0]-prices[i-1])
        return dp[2][0]
'''
