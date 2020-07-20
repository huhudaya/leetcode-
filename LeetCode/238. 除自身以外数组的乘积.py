'''
给你一个长度为 n 的整数数组 nums，其中 n > 1
返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积
示例:
输入: [1,2,3,4]
输出: [24,12,8,6]

提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
'''
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 空间未优化
        n = len(nums)
        # 初始化为1，这是因为首部元素的前缀乘积可以是1，这样并不影响结果
        prefix_arr = [1] * n
        suffix_arr = [1] * n
        res = [0] * n
        # 总体思路就是构建两个前缀和后缀乘积数组
        for i in range(1, n):
            prefix_arr[i] = prefix_arr[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            suffix_arr[i] = suffix_arr[i + 1] * nums[i + 1]
        for i in range(n):
            res[i] = prefix_arr[i] * suffix_arr[i]
        return res


# 空间优化
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 空间优化版本
        n = len(nums)
        res = [1] * n
        n = len(nums)
        prefix = 1
        suffix = 1
        # 前缀数组
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        # 计算后缀乘积，同时更新res数组
        for i in range(n - 1, -1, -1):
            # 更新res的值
            res[i] = suffix * res[i]
            # 更新后缀的值
            suffix = suffix * nums[i]
        return res


