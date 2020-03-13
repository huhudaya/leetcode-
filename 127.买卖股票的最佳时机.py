'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''

'''
如果反过来想，固定卖出时间 sell，向前穷举买入时间 buy，寻找 prices[buy] 最小的那天
是不是也能达到相同的效果？是的，而且这种思路可以减少一个 for 循环
'''
# 暴力法
'''
res = 0
for buy in range(len(price)):
    for sell in range(buy + 1, len(price)):
        res = max(res, price[sell] - price[buy])
return res 
'''


# O（N）
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 思想其实就是单调栈的思想
        res = 0
        cur_min = prices[0]
        n = len(prices)
        # 卖出时间必须从 1 开始,因为第一条肯定不能卖啊，还没买怎么卖
        # 固定卖出的时间，即用一个for循环，然后于卖出时间之前的最小值比较！ prices[i]表示当前i时刻卖出
        for i in range(1, n):
            cur_min = min(cur_min, prices[i])
            res = max(res, prices[i] - cur_min)
        return res