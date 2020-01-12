# 034. 在排序数组中查找元素的第一个和最后一个位置.py
'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
'''
# 典型的二分法
class Solution:
    import bisect
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 二分模板
        def findFirst(nums, target):
            if len(nums) == 0 or nums is None:
                return -1
            left = 0
            right = len(nums) - 1
            while left + 1 < right:
                mid = left + (right - left) // 2
                # 找到firstPosition
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else:
                return -1
        def findLast(nums, target):
            if len(nums) == 0 or nums is None:
                return -1
            left = 0
            right = len(nums) - 1
            while left + 1 < right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid
                else:
                    right = mid
            if nums[right] == target:
                return right
            elif nums[left] == target:
                return left
            else:
                return -1
        first = findFirst(nums, target)
        last = findLast(nums, target)
        return [first, last]
        # 调用库函数
        # if len(nums) == 0 or nums is None:
        #     return [-1,-1]
        # if target not in nums:
        #     return [-1, -1]
        # return [bisect.bisect_left(nums, target),bisect.bisect_right(nums, target) - 1]
