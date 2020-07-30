'''
输入一个整数数组
实现一个函数来调整该数组中数字的顺序
使得所有奇数位于数组的前半部分
所有偶数位于数组的后半部分。

 

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。
 

提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10000
'''

from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        # 双指针
        if not nums:
            return []
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            # 指针交换法
            while left < right and nums[right] & 1 == 0:
                right -= 1
            while left < right and nums[left] & 1 == 1:
                left += 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        return nums


# 挖坑法
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        # 双指针
        if not nums:
            return []
        n = len(nums)
        left = 0
        right = n - 1
        tmp = nums[0]
        while left < right:
            # 挖坑法
            while left < right and nums[right] & 1 == 0:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] & 1 == 1:
                left += 1
            nums[right] = nums[left]
        nums[right] = tmp
        return nums