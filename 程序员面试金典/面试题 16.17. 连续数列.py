'''
给定一个整数数组，找出总和最大的连续数列，并返回总和。

示例：

输入： [-2,1,-3,4,-1,2,1,-5,4]
输出： 6
解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶：

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
'''
import sys
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 计数法
        res = -sys.maxsize
        n = len(nums)
        cur_sum = 0
        for i in range(n):
            if cur_sum > 0:
                cur_sum += nums[i]
            else:
                cur_sum = nums[i]
            res = max(res, cur_sum)
        return res

