'''
给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。

示例 1:

输入: [0,1,2,4,5,7]
输出: ["0->2","4->5","7"]
解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间
示例 2:

输入: [0,2,3,4,6,8,9]
输出: ["0","2->4","6","8->9"]
解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间
'''
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        n = len(nums)
        if n == 1:
            return [str(nums[0])]
        res = []
        left = 0
        for i in range(1, n):
            if nums[i] != nums[i - 1] + 1:
                if i - left == 1:
                    res.append(str(nums[left]))
                else:
                    res.append(str(nums[left]) + "->" + str(nums[i - 1]))
                left = i
            if i == n - 1:
                if i == left:
                    res.append(str(nums[left]))
                else:
                    res.append(str(nums[left]) + "->" + str(nums[i]))
        return res


Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9])
