'''
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
链接：https://leetcode-cn.com/problems/permutations
'''
'''
解决一个回溯问题，实际上就是一个决策树的遍历过程。你只需要思考 3 个问题：
1、路径：也就是已经做出的选择。
2、选择列表：也就是你当前可以做的选择。
3、结束条件：也就是到达决策树底层，无法再做选择的条件。
如果你不理解这三个词语的解释，没关系，我们后面会用「全排列」和「N 皇后问题」
这两个经典的回溯算法问题来帮你理解这些词语是什么意思，现在你先留着印象。
# 模板

result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择

其核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」，特别简单。


for 选择 in 选择列表:
    # 做选择
    将该选择从选择列表移除
    路径.add(选择)
    backtrack(路径, 选择列表)
    # 撤销选择
    路径.remove(选择)
    将该选择再加入选择列表
'''

from typing import List


class Solution:
    def permute(self, nums):
        # 回溯法
        res = []
        track = []
        n = len(nums)

        def helper(nums):
            # n叉树的遍历
            if len(track) == n:
                # 这里需要注意一下，track应该被新new,否则存放的都是track的引用,最后均为[]
                res.append(list(track))
                return
            for i in range(n):
                if nums[i] in track:
                    # 终止条件
                    continue
                # 做选择                
                track.append(nums[i])
                # 递归
                helper(nums)
                # 撤销选择
                track.pop()

        helper(nums)
        return res


# 方法二：
class Solution:
    def permute(self, nums):
        res = []

        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                # 一种太讨巧的方法了吧AHHHH.. i like it 
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res


# 链接：https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-by-powcai-2/


# 作者：liweiwei1419
# 通用的做法是使用一个布尔数组来表示是否添加过
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path)
                return
            for i in range(size):
                if used[i] is False:
                    used[i] = True
                    path.append(nums[i])
                    # 注意这里的depth只是用来记录当前的层次
                    dfs(nums, size, depth + 1, path, used, res)
                    used[i] = False
                    path.pop()

        size = len(nums)
        if len(nums) == 0:
            return []
        used = [False for _ in range(size)]
        res = []
        dfs(nums, size, 0, [], used, res)
        return res