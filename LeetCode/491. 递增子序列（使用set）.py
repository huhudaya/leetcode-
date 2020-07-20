'''
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
示例:
输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]

说明:
给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
'''
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        ans = set()
        res = []

        def feedback(tmp, nums, ix):
            if len(tmp) >= 2 and tuple(tmp) not in ans:
                ans.add(tuple(tmp[:]))
                res.append(tmp[:])

            for i in range(ix, len(nums)):
                if len(tmp) == 0 or (nums[i] >= tmp[-1]):
                    tmp.append(nums[i])
                    feedback(tmp, nums, i + 1)
                    tmp.pop()

        feedback([], nums, 0)
        return res


# 自己的版本
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # 直观的解法应该是回溯，如果是动态规划，一般是求最值
        # 直接套用回溯的模板
        res = []
        ans = set()

        def dfs(nums, start, path, res):
            # 这里用set进行判断
            if len(path) >= 2:
                if path[-1] >= path[-2] and tuple(path) not in ans:
                    ans.add(tuple(path[:]))
                    res.append(path[:])
            for i in range(start, n):
                # 剪枝 如果不满足条件就不继续了
                if len(path) > 0 and nums[i] < path[-1]:
                    continue
                path.append(nums[i])
                dfs(nums, i + 1, path, res)
                path.pop()

        dfs(nums, 0, [], res)
        return res


# 直接用set
# 使用set
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 2:
            return []
        n = len(nums)
        # 第一直观的解法应该是回溯(如果是动态规划，一般是求最优解比如最值或者最优个数)
        # 直接想到套用回溯的模板（这里要求不能有重复的组合，联想到排序之后剪枝，但是题目的特殊性不能排序，所以用set集合来去重）
        # 因为要求子序列，注意是子序列，所以这个数组不能被排序！
        ans = set()

        def dfs(nums, start, path):
            # 这里用set进行判断
            if len(path) >= 2:
                ans.add(tuple(path[:]))
            for i in range(start, n):
                # 剪枝 如果不满足条件就不继续了
                if len(path) > 0 and nums[i] < path[-1]:
                    continue
                path.append(nums[i])
                dfs(nums, i + 1, path)
                path.pop()

        dfs(nums, 0, [])
        return list(ans)
