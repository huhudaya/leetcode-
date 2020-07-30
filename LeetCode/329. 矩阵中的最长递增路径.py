'''
给定一个整数矩阵，找出最长递增路径的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

示例 1:

输入: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
输出: 4
解释: 最长递增路径为 [1, 2, 6, 9]。
示例 2:

输入: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
输出: 4
解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
'''

from functools import lru_cache
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        depath = []
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        memo = {}
        res = 0

        @lru_cache(None)
        def dfs(i, j):
            res = 1
            for di in directions:
                row = i + di[0]
                col = j + di[1]
                if row < 0 or row >= m or col < 0 or col >= n:
                    continue
                if matrix[i][j] < matrix[row][col]:
                    res = max(res, dfs(row, col) + 1)
            return res

        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res
        # 定义dfs(i, j)返回(i, j)为起点的最大长度
