'''

给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字）
并返回该子数组所对应的乘积。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
'''
from typing import List
import sys


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 动态规划
        n = len(nums)
        # dp[i]为以 i 结尾的位数的最大乘积
        dp = [[0] * 2 for _ in range(n)]
        res = -sys.maxsize
        # base case
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        for i in range(1, n):
            if nums[i] > 0:
                # 最大值
                dp[i][0] = max(dp[i - 1][0] * nums[i], nums[i])
                # 最小值
                dp[i][1] = min(dp[i - 1][1] * nums[i], nums[i])
            else:
                # 最大值
                dp[i][0] = max(dp[i - 1][1] * nums[i], nums[i])
                # 最小值
                dp[i][1] = min(dp[i - 1][0] * nums[i], nums[i])
        print(dp)
        for i in range(n):
            res = max(res, dp[i][0])
        return res


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums_reverse = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1  # or 1的作用是，当nums[i - 1]==0时，nums[i]乘等自身
            nums_reverse[i] *= nums_reverse[i - 1] or 1
        return max(max(nums), max(nums_reverse))


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums_reverse = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1  # or 1的作用是，当nums[i - 1]==0时，nums[i]乘等自身
            nums_reverse[i] *= nums_reverse[i - 1] or 1
        return max(max(nums), max(nums_reverse))
