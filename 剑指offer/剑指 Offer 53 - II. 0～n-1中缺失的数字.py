'''
一个长度为n-1的递增排序数组中的所有数字都是唯一的，
并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

 

示例 1:

输入: [0,1,3]
输出: 2
示例 2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8
 

限制：

1 <= 数组长度 <= 10000
'''
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 使用减法的思想
        n = len(nums)
        res = n
        for i in range(n):
            tmp = nums[i] - i
            res -= tmp
        return res


# 二分
# 核心思路，找到右边子数组的首位元素
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 二分
        n = len(nums)
        left = 0
        right = n - 1
        # 右子数组的首位元素
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
        print(left, right)
        if nums[left] != left:
            return left
        elif nums[right] != right:
            return right
        else:
            return right + 1