# 120. 三角形最小路径和.py
'''
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
链接：https://leetcode-cn.com/problems/triangle
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 动态规划4步法
        '''
        问题拆解.状态定义.递推公式推导.实现
        '''
        # 这里有从上到下，从下到上两种方式，需要分析
        # 递推公式：dp[i][j] = min(dp[i+1][j],dp[i+1][j+1]) + triangle[i][j]
        n = len(triangle)
        dp = [[0] * n for i in range(n)]
        lastRow = triangle[n-1]
        # base case 为最下面一层
        for i in range(n):
            dp[n-1][i] = lastRow[i]
        # 从下往上倒着遍历
        for i in range(n-2, -1, -1):
            row = triangle[i]
            for j in range(i+1):
                dp[i][j] = min(dp[i+1][j],dp[i+1][j+1]) + row[j]
        return dp[0][0]
