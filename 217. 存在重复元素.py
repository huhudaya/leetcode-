# 217. 存在重复元素.py
'''
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

链接：https://leetcode-cn.com/problems/contains-duplicate
'''

# set
def containsDuplicate(nums):
    return len(nums) != len(set(nums))

# 排序
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums: return False
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]: return True
        return False
# 哈希
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for num in nums:
            if num in visited:return True
            visited.add(num)
        return False
