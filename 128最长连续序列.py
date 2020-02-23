# 128最长连续序列.py
# 暴力法，大力出奇迹
'''
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
'''
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # ---------------------1 method---------------------
        # 暴力法..emmm 暴力法果然会超时。。
        n = len(nums)
        res = 0
        for num in nums:
            cnt = 1
            while num + 1 in nums:
                cnt += 1
                num = num + 1
            res = max(cnt, res)
        return res


# 排序法
# 排序法应该很容易想到，没思路的话先排序哈哈
class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        # ---------------------2 method---------------------
        # 排序O(NlogN)，不满足题意要求O(N),时间60ms,比使用hash的O(N)更快，看起来还行？
        # 使用set去重，然后排序
        nums = list(set(nums))
        nums.sort()
        print(nums)
        n = len(nums)
        # 注意这里res初始化为1 
        res = 1
        cnt = 1
        if n < 2:
            return n
        # 计数法
        for i in range(n - 1):
            if nums[i] + 1 == nums[i + 1]:
                cnt += 1
                res = max(cnt, res)
            else:
                cnt = 1
        return res


# 利用hash表
class Solution3:
    def longestConsecutive(self, nums: List[int]) -> int:
        # ---------------------3 method---------------------
        # 思考，题目要求是O(N)解决，联想到线性时间复杂度解决，应该可以想到使用hash表等辅助结构
        # 使用hash表 时间复杂度O(N),因为hashSet等结构的set,get都是O(1)
        hashSet = set()
        n = len(nums)
        res = 1
        # 构建hashSet
        if n < 2:
            return n
        for i in range(n):
            hashSet.add(nums[i])
        # 计数法
        for i in range(n):
            if nums[i] - 1 not in hashSet:
                cnt = 1
                tmp = nums[i]
                while tmp + 1 in hashSet:
                    cnt += 1
                    tmp += 1
                res = max(res, cnt)
        return res

    # 简约版 O(N)


class Solution3(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        res = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                res = max(res, y - x)
        return res
