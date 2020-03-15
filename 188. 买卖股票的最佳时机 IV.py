'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2:

输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
'''
# 暴力
class Solution:
    from typing import List
    def maxProfit(self, k, prices: List[int]) -> int:
        # n = len(prices)
        memo = dict()
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
        return dp(0, k)

'''
递归其实是符合我们思考的逻辑的，一步步推进，遇到无法解决的就丢给递归，一不小心就做出来了，可读性还很好。
缺点就是一旦出错，你也不容易找到错误出现的原因。比如上篇文章的递归解法，肯定还有计算冗余，但确实不容易找到。

而这里，我们不用递归思想进行穷举，而是利用「状态」进行穷举。

看看总共有几种「状态」，再找出每个「状态」对应的「选择」。
我们要穷举所有「状态」，穷举的目的是根据对应的「选择」更新状态。看图，就是这个意思。
'''