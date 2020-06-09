# 137. 只出现一次的数字 II.py
'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,3,2]
输出: 3
示例 2:

输入: [0,1,0,1,0,1,99]
输出: 99

链接：https://leetcode-cn.com/problems/single-number-ii
'''

'''
观察发现，数组去重后的和 * 3跟原来的数组的和刚好相差要找元素的2倍。
'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums)) * 3 - sum(nums)) // 2


# 011
print(4 ^ 4 & (3))
