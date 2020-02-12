# 287. 寻找重复数.py
'''
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次

链接：https://leetcode-cn.com/problems/find-the-duplicate-number
'''
# 二分
class Solution:
    #O(nlogn)算法
    def findDuplicate(self, nums: List[int]) -> int:
        start = 1
        end = len(nums) - 1
        #二分,相当于求解count(mid) > mid的FirstPosition
        while start + 1 < end:
            mid = start + (end-start) // 2
            count = sum(num <= mid for num in nums)
            if count <= mid:
                start = mid
            else:
                end = mid
        #如果
        if sum(num <= start for num in nums) > start:
            return start
        else:
            return end