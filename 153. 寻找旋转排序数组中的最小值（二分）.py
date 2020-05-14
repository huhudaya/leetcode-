# 153. 寻找旋转排序数组中的最小值.py
'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1
示例 2:

输入: [4,5,6,7,0,1,2]
输出: 0

'''
'''
二分法, 二分法就是找与mid判断条件,这里我们选用right

当nums[mid] > nums[right]说明在mid左半边的递增区域, 说明最小元素在> mid区域

当nums[mid] <= nums[right说明在mid右半边的递增区域, 说明最小元素在<= mid区域

小技巧:

一般是这样,

当while left < right是循环外输出

当while left <= right是循环里输出

相关题型: 154. 寻找旋转排序数组中的最小值 II
'''
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


# 自己的版本
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #
        left = 0
        right = len(nums) - 1
        if not nums:
            return -1
        while left + 1 < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid
        if nums[right] < nums[left]:
            return nums[right]
        else:
            return nums[left]
