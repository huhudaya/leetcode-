'''

给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

# 注意是 1 到 N
# 和全排列问题一样，这是一道使用回溯算法解决的经典问题。
# 而分析回溯问题，我们常常需要画图来帮助我们理清思路和寻找边界条件。
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 特判
        if n <= 0 or k <= 0 or k > n:
            return []
        res = []
        self.__dfs(1, k, n, [], res)
        return res

    def __dfs(self, start, k, n, pre, res):
        if len(pre) == k:
            res.append(pre[:])
            return

        # 注意：这里 i 的上限是归纳得到的  剪枝
        for i in range(start, n - (k - len(pre)) + 2):
            pre.append(i)
            self.__dfs(i + 1, k, n, pre, res)
            pre.pop()

# 未优化版
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 先把不符合条件的情况去掉
        if n <= 0 or k <= 0 or k > n:
            return []
        res = []
        self.__dfs(1, k, n, [], res)
        return res

    def __dfs(self, start, k, n, pre, res):
        # 当前已经找到的组合存储在 pre 中，需要从 start 开始搜索新的元素
        # 在第 k 层结算
        if len(pre) == k:
            res.append(pre[:])
            return

        for i in range(start, n + 1):
            pre.append(i)
            # 因为已经把 i 加入到 pre 中，下一轮就从 i + 1 开始
            # 注意和全排列问题的区别，因为按顺序选择，因此无须使用 used 数组
            self.__dfs(i + 1, k, n, pre, res)
            # 回溯的时候，状态重置
            pre.pop()

# 自己的版本
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0 or n < k:
            return []
        res = []
        self._dfs(n, k, 0, [], res)
        return res
    def _dfs(self, n, k, start, path, res):
        # 递归结束条件
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(start, n):
            # 选择列表
            path.append(i + 1)
            # 从当前元素之后开始遍历，不包括当前元素
            self._dfs(n, k , i + 1, path, res)
            # 撤销选择
            path.pop()



class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0 or n < k:
            return []
        res = []
        self._dfs(n, k, 0, [], res)
        return res
    def _dfs(self, n, k, start, path, res):
        # 递归结束条件
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(start, n - (k - len(path)) + 1):
            # 选择列表
            path.append(i + 1)
            # 从当前元素之后开始遍历，不包括当前元素
            self._dfs(n, k , i + 1, path, res)
            # 撤销选择
            path.pop()