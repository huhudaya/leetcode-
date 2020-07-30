# 209. 长度最小的子数组.py
'''
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(nlog n) 时间复杂度的解法。

链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
'''
# 注意看清题目！！！！是N个正整数，而且是正整数s
'''
思路一：滑动窗口

时间复杂度：O(n)

思路二：前缀和 + 二分搜索

时间复杂度：O(nlogn)

直接看代码，很好理解，如有不明白的地方，欢迎留言！
'''
# 代码：
# 思路一：
# 双指针
from typing import List
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums : return 0
        left = 0
        cur = 0
        res = float("inf")
        # 快指针为right
        for right in range(len(nums)):
            cur += nums[right]
            # 慢指针 left 移动条件
            while cur >= s:
                res = min(res, right - left + 1)
                cur -= nums[left]
                left += 1
        return res if res != float("inf") else 0

# 思路二： 二分法
import bisect
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums : return 0
        # 求前缀和
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        #print(nums)
        # 总和都小于 s 时候
        if nums[-1] < s: return 0
        res = float("inf")
        nums = [0] + nums
        for i in range(1, len(nums)):
            if nums[i] - s >= 0:
                # 二分查找
                loc = bisect.bisect_left(nums, nums[i] - s)
                if nums[i] - nums[loc] >= s:
                    res = min(res, i - loc)
                    continue
                if loc > 0:
                    res = min(res, i - loc + 1)
        return res 



 # 自己的版本 双指针
import sys
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 双指针滑动窗口O(N)
        n = len(nums)
        left = 0
        res = sys.maxsize
        preSum = 0
        if nums is None or len(nums) < 1:
            return 0
        for right in range(n):
            preSum += nums[right]
            # 左指针移动
            while preSum >= s:
                res = min(right - left + 1, res)
                preSum -= nums[left]
                left += 1
        return res if res != sys.maxsize else 0