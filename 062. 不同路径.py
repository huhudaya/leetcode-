# 062. 不同路径.py
'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

例如，上图是一个7 x 3 的网格。有多少可能的路径？

说明：m 和 n 的值均不超过 100。

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28
链接：https://leetcode-cn.com/problems/unique-paths
'''
'''
给定一个矩阵，问有多少种不同的方式从起点(0,0) 到终点 (m-1,n-1)，并且每次移动只能向右或者向下，我们还是按之前提到的分析动态规划那四个步骤来思考一下：

问题拆解

题目中说了，每次移动只能是向右或者是向下，矩阵类动态规划需要关注当前位置和其相邻位置的关系，对于某一个位置来说，经过它的路径只能从它上面过来，或者从它左边过来，因此，如果需要求到达当前位置的不同路径，我们需要知道到达其上方位置的不同路径，以及到达其左方位置的不同路径

状态定义

矩阵类动态规划的状态定义相对来说比较简单，只需要看当前位置即可，问题拆解中，我们分析了当前位置和其邻居的关系，提到每个位置其实都可以算做是终点.
状态表示就是 “从起点到达该位置的不同路径数目”

递推方程

有了状态，也知道了问题之间的联系，其实递推方程也出来了，就是

dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

有了这些，这道题还没完，我们还要考虑状态数组的初始化问题，对于上边界和左边界的点，因为它们只能从一个方向过来，需要单独考虑，比如上边界的点只能从左边这一个方向过来，左边界的点只能从上边这一个方向过来，它们的不同路径个数其实就只有 1，提前处理就好。
'''
'''
//www.cxyxiaowu.com
public int uniquePaths(int m, int n) {
    int[][] dp = new int[m][n];

    for (int i = 0; i < m; ++i) {
        dp[i][0] = 1;
    }

    for (int j = 0; j < n; ++j) {
        dp[0][j] = 1;
    }

    for (int i = 1; i < m; ++i) {
        for (int j = 1; j < n; ++j) {
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        }
    }

    return dp[m - 1][n - 1];
}
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp思想
        # 注意拆解子问题
        dp = [[0]*n for i in range(m)]
        # base case
        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m-1][n-1]
