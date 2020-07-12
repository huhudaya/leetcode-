# 015三数之和.py 
'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        result = []
        if length < 3 or nums is None:
            return []
        for i in range(length):
            if nums[i] > 0:
                break
            # 去重,这里应该是continue，不能是break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            r = length - 1
            l = i + 1
            while l < r:
                _sum = nums[i] + nums[l] + nums[r]
                if _sum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    # 小剪枝 去重,注意必须先判断 l < r,否则会出现超出索引
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # 小剪枝
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    # 注意这里，每次循环必须移动指针，否则死循环
                    l += 1
                    r -= 1
                elif _sum < 0:
                    l += 1
                elif _sum > 0:
                    r -= 1
        return result
