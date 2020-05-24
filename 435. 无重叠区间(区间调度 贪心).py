# 435. 无重叠区间.py
'''
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
示例 1:

输入: [ [1,2], [2,3], [3,4], [1,3] ]

输出: 1

解释: 移除 [1,3] 后，剩下的区间没有重叠。
示例 2:

输入: [ [1,2], [1,2], [1,2] ]

输出: 2

解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
示例 3:

输入: [ [1,2], [2,3] ]

输出: 0
解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
'''


'''
什么是贪心算法呢？贪心算法可以认为是动态规划算法的一个特例，相比动态规划，使用贪心算法需要满足更多的条件（贪心选择性质），但是效率比动态规划要高。
比如说一个算法问题使用暴力解法需要指数级时间，如果能使用动态规划消除重叠子问题，就可以降到多项式级别的时间，如果满足贪心选择性质，那么可以进一步降低时间复杂度，达到线性级别的。
什么是贪心选择性质呢，简单说就是：每一步都做出一个局部最优的选择，最终的结果就是全局最优。注意哦，这是一种特殊性质，其实只有一部分问题拥有这个性质。
比如你面前放着 100 张人民币，你只能拿十张，怎么才能拿最多的面额？显然每次选择剩下钞票中面值最大的一张，最后你的选择一定是最优的。
然而，大部分问题明显不具有贪心选择性质。比如打斗地主，对手出对儿三，按照贪心策略，你应该出尽可能小的牌刚好压制住对方，但现实情况我们甚至可能会出王炸。这种情况就不能用贪心算法，而得使用动态规划解决，参见前文「动态规划解决博弈问题」。
'''

from typing import List
# 对于区间问题的处理，一般来说第一步都是排序，相当于预处理降低后续操作难度
# 但是对于不同的问题，排序的方式可能不同，这个需要归纳总结
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 求需要移除的最小数量，即求可以组成无重叠区间的最大个数
        if intervals == None or len(intervals) == 0:
            return 0
        cnt = 1
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        end = intervals[0][1]
        for interval in intervals:
            start = interval[0]
            if start >= end:
                cnt += 1
                end = interval[1]
        return n - cnt
