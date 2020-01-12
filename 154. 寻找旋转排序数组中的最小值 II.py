# 154. 寻找旋转排序数组中的最小值 II.py
'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

注意数组中可能存在重复的元素。

示例 1：

输入: [1,3,5]
输出: 1
示例 2：

输入: [2,2,2,0,1]
输出: 0
说明：

这道题是 寻找旋转排序数组中的最小值 的延伸题目。
允许重复会影响算法的时间复杂度吗？会如何影响，为什么
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
            	left = mid + 1
            elif nums[mid] < nums[right]:
            	right = mid
            else:
            	right = right - 1 # key
        return nums[left]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                left = mid
        if nums[left] <= nums[right]:
            return nums[left]
        else:
            return nums[right]


# 分治
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            raise Exception('程序出错')
        if size == 1:
            return nums[0]
        return self.__find_min(nums, 0, size - 1)

    def __find_min(self, nums, left, right):
        if left == right:
            return nums[left]
        if left + 1 == right:
            return min(nums[left], nums[right])
        # mid = left + (right - left) // 2
        mid = (left + right) >> 1
        return min(self.__find_min(nums, left, mid), self.__find_min(nums, mid + 1, right))
