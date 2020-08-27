'''
给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差

示例：

输入：{1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
输出： 3，即数值对(11, 8)
提示：

1 <= a.length, b.length <= 100000
-2147483648 <= a[i], b[i] <= 2147483647
正确结果在区间[-2147483648, 2147483647]内
'''

# 母题系列
# https://leetcode-cn.com/problems/smallest-difference-lcci/solution/wo-shi-ni-de-ma-ma-ya-di-yi-qi-by-fe-lucifer/
from typing import List


class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        n = len(a)
        m = len(b)
        # 先对两个数组进行排序
        a.sort()
        b.sort()
        res = float('inf')
        i = j = 0
        # 双指针，谁小移动谁
        while i < n and j < m:
            res = min(res, abs(a[i] - b[j]))
            if a[i] < b[j]:
                i += 1
            else:
                j += 1
        return res
