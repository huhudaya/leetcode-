# 016最接近的三数之和.py
'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closet = []
        length = len(nums)
        for i,num in enumerate(nums[:-2]):
            l,r = i+1,length-1
            if num + nums[r] + nums[r-1] < target:
                closet.append(num+nums[r]+nums[r-1])
            elif nums[i] + nums[l] + nums[l+1] > target:
                closet.append(num+nums[l]+nums[l+1])
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
        closet.sort(key=lambda x:abs(x-target))
        return closet[0]
        
                        
                        
            