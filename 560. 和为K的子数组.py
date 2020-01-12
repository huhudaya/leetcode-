# 560. 和为K的子数组.py
'''
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
'''
# hash优化版本
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和思想
        n = len(nums)
        preSum = dict()
        # base case
        preSum[0] = 1
        sum_i = 0
        res = 0
        for i in range(n):
            sum_i += nums[i]
            sum_j = sum_i - k
            if sum_j in preSum:
                res += preSum.get(sum_j)
            preSum[sum_i] = preSum.get(sum_i,0) + 1
        return res