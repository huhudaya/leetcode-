'''

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2

限制：
1 <= 数组长度 <= 50000
'''
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if nums is None or nums == []:
            return -1
        n = len(nums)
        candidate = nums[0]
        cnt = 1
        for i in range(1, n):
            if nums[i] == candidate:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    cnt = 1
                    candidate = nums[i]
        return candidate