'''
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

示例 1:

输入: [2,2,3,4]
输出: 3
解释:
有效的组合是:
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3
注意:

数组长度不超过1000。
数组里整数的范围为 [0, 1000]。
'''
from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # 有效三角形，任意两边之和大于第三边 a < b < c and (a + b) > c   ==> c - b < a and c - a < b
        # 排序之和双指针
        n = len(nums)
        if nums is None or n == 0:
            return 0
        # 先排序
        nums.sort()
        res = 0
        # 从后往前，判断前两个元素的值
        for i in range(n-1, 1, -1):
            l = 0
            r = i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    res += r - l
                    r -= 1
                else:
                    l += 1
        return res