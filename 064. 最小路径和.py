# 064. 最小路径和.py
'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
链接：https://leetcode-cn.com/problems/minimum-path-sum
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp思想，类似于62题
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for i in range(m)]
        # base case
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for j in range(1, m):
            dp[j][0] = dp[j-1][0] + grid[j][0]
        # 递推
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[m-1][n-1]

        

