'''
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
# 复杂度比较高
def permuteUnique(nums):
    res = []
    def backtrack(nums, tmp):
        if not nums:
            res.append(tmp)
            return
        arr = []
        for i in range(len(nums)):
            if nums[i] not in arr:
                arr.append(nums[i])
            else:
                continue
            backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res

from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path.copy())
                return
            for i in range(size):
                if used[i] is False:
                    # 修改2：在used[i - 1]刚刚被撤销的时候剪枝，说明接下来会被选择，搜索一定会重复，故"剪枝"
                    # 思考这里不加user[i - 1]会怎么样？？
                    # 打断点调试分析一下 比如112，当运行到这里的时候，由于nums[i] == nums[i - 1]，所以即提前结束了，所以需要避免这种情况
                    # 思考，这里的 i > 0仅仅是为了有i-1存在，不同于90题，i > start是表示当前节点下的第二个分支
                    if i > 0 and nums[i] == nums[i - 1] and used[i - 1] is False:
                    # if i > 0 and nums[i] == nums[i - 1]:
                        continue
                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth + 1, path, used, res)
                    used[i] = False
                    path.pop()
        size = len(nums)


        if size == 0:
            return []
        # 必须要使用排序算法
        nums.sort()
        used = [False] * len(nums)
        res = []
        dfs(nums, size, 0, [], used, res)
        return res
print(Solution().permuteUnique([1,1,3]))