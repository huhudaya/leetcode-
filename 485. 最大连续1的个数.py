# 485. 最大连续1的个数.py
'''
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：

输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。
'''

from typing import List
# 计数法
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for num in nums:
            if num == 1:
                # Increment the count of 1's by one.
                count += 1
            else:
                # Find the maximum till now.
                max_count = max(max_count, count)
                # Reset count of 1.
                count = 0
        return max(max_count, count)


'''
使用 splits 函数在 0 处分割将数组转换成字符串。
在获取子串的最大长度就是最大连续 1 的长度。
'''


def findMaxConsecutiveOnes(self, nums):
    return max(map(len, ''.join(map(str, nums)).split('0')))


# 双指针
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        left = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                left = i + 1
            res = max(res, i - left + 1)
        return res
