'''
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

 

示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
 

提示：

1 <= arr.length <= 10^5
-100 <= arr[i] <= 100
注意：本题与主站 53 题相同：https://leetcode-cn.com/problems/maximum-subarray/

'''
from typing import List
import sys


class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        # 计数法
        res = -sys.maxsize
        _sum = 0
        n = len(nums)
        # 正向增益
        for i in range(n):
            if _sum >= 0:
                _sum += nums[i]
            else:
                # 重新选择首部
                _sum = nums[i]
            res = max(res, _sum)
        return res

    # 动态规划
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] 定义为以当前元素结尾的最大和
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)
