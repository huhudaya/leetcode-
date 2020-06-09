'''
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

示例 1:

输入: [3,2,3]
输出: [3]
示例 2:

输入: [1,1,1,3,3,2,2,2]
输出: [1,2]
'''
# 摩尔投票算法
from typing import List

# 最多输出两个数， 反正法：如果超过3个，那么不满足题意！
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candiate1 = candiate2 = None
        cnt1 = cnt2 = 0
        for num in nums:
            if num == candiate1:
                cnt1 += 1
            elif num == candiate2:
                cnt2 += 1
            elif cnt1 == 0:
                candiate1 = num
                # cnt1 = 1
                cnt1 += 1
            elif cnt2 == 0:
                candiate2 = num
                # cnt2 = 1
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        '''
        最后会有这么几种可能：有2个大于n/3，有1个大于n/3，有0个大于n/3
        遍历结束后选出了两个候选人，但是这两个候选人是否满足>n/3
        还需要再遍历一遍数组，找出两个候选人的具体票数，因为题目没有像169题保证一定有一个大于一半的
        '''
        return [n for n in (candiate1, candiate2) if nums.count(n) > len(nums) // 3]

# 自己的版本
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 摩尔投票法 最多有两个数超过n//3，相当于摆两个擂台
        cnt1 = 0
        cnt2 = 0
        candiate1 = None
        candiate2 = None
        res = []
        size = len(nums) // 3
        for num in nums:
            if num == candiate1:
                cnt1 += 1
            elif num == candiate2:
                cnt2 += 1
            elif cnt1 == 0:
                candiate1 = num
                cnt1 += 1
            elif cnt2 == 0:
                candiate2 = num
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        p1 = nums.count(candiate1)
        p2 = nums.count(candiate2)
        if p1 > size:
            res.append(candiate1)
        if p2 > size:
            res.append(candiate2)
        return res
        # return [n for n in (candiate1, candiate2) if nums.count(n) > len(nums) // 3]