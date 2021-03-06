# 035. 搜索插入位置.py
'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

链接：https://leetcode-cn.com/problems/search-insert-position
'''
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 二分
        if len(nums) == 0 or nums is None:
            return -1
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            # 找到 >= target 的 firstPosition
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        if nums[left] >= target:
            return left
        if nums[right] >= target:
            return right


