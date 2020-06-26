# 057. 插入区间.py
'''
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1:

输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]
示例 2:

输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

链接：https://leetcode-cn.com/problems/insert-interval
'''
'''
贪心算法一般用来解决需要 “找到要做某事的最小数量” 或 “找到在某些情况下适合的最大物品数量” 的问题，且提供的是无序的输入。

贪心算法的思想是每一步都选择最佳解决方案，最终获得全局最佳的解决方案。

标准解决方案具有 O(NlogN) 的时间复杂度且由以下两部分组成：

思考如何排序输入数据 O(NlogN) 的时间复杂度）。
思考如何解析排序后的数据 O(N) 的时间复杂度）
如果输入数据本身有序，则我们不需要进行排序，那么该贪心算法具有 O(N) 的时间复杂度。

如何证明你的贪心思想具有全局最优的效果：可以使用反证法来证明。
'''

from typing import List
# 类比合并区间!
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        res = []
        intervals.sort()
        for i in intervals:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(i[1], res[-1][1])
        return res

