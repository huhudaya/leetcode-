# 016最接近的三数之和.py
'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
'''
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closet = []
        length = len(nums)
        for i, num in enumerate(nums[:-2]):
            l, r = i + 1, length - 1
            # 可以提前结束遍历
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 最大值都比target小，直接加入枚举数组
            if num + nums[r] + nums[r - 1] < target:
                closet.append(num + nums[r] + nums[r - 1])
            # 最小值都比target大，直接加入枚举数组
            elif nums[i] + nums[l] + nums[l + 1] > target:
                closet.append(num + nums[l] + nums[l + 1])
            else:
                while l < r:
                    tmpsum = num + nums[l] + nums[r]
                    closet.append(tmpsum)
                    if tmpsum == target:
                        return target
                    elif tmpsum < target:
                        l += 1
                    elif tmpsum > target:
                        r -= 1
        # 排序 输出abs值最接近target的值
        closet.sort(key=lambda x: abs(x - target))
        return closet[0]


# 最接近的三数之和 双指针
def threeSumLosest(nums, target):
    if len(nums) < 3:
        return None
    nums.sort()
    min_diff = sum(nums[0:3]) - target
    for i in range(len(nums) - 2):
        # 避免i重复
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            diff = nums[i] + nums[l] + nums[r] - target
            if diff == 0:
                return target
            # 更新min_diff
            else:
                if abs(diff) < abs(min_diff):
                    min_diff = diff
                if diff < 0:
                    l += 1
                if diff > 0:
                    r -= 1
    return min_diff + target

import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) < 3:
            return -1
        nums.sort()
        n = len(nums)
        res = sys.maxsize
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            # 大剪枝
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            max_right = nums[i] + nums[right - 1] + nums[right]
            min_left = nums[i] + nums[left] + nums[left + 1]
            # 小剪枝
            if max_right < target:
                res = max_right if abs(res - target) > abs(max_right - target) else res
            elif min_left > target:
                res = min_left if abs(res - target) > abs(min_left - target) else res
            # 进行双指针判断
            else:
                while left < right:
                    tmp = nums[i] + nums[left] + nums[right]
                    if tmp > target:
                        right -= 1
                    elif tmp < target:
                        left += 1
                    else:
                        return tmp
                    if abs(res - target) > abs(tmp - target):
                        res = tmp
        return res
Solution().threeSumClosest([-1,2,1,-4],1)