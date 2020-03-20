'''
给定一个包含了一些 0 和 1的非空二维数组 grid 
一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合
你可以假设二维矩阵的四个边缘都被水包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。

注意: 给定的矩阵grid 的长度和宽度都不超过 50。
'''

# 官方
from typing import List
class Solution:
    def dfs(self, grid, cur_i, cur_j):
        # 有返回值的递归一定要先写递归结束条件
        if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
            return 0
        grid[cur_i][cur_j] = 0
        ans = 1
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i, next_j = cur_i + di, cur_j + dj
            ans += self.dfs(grid, next_i, next_j)
        return ans

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                ans = max(self.dfs(grid, i, j), ans)
        return ans

# java
'''
class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int res = 0; 
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 1) {
                    res = Math.max(res, dfs(i, j, grid));
                }
            }
        } 
        return res;
    }
    // 每次调用的时候默认num为1，进入后判断如果不是岛屿，则直接返回0，就可以避免预防错误的情况。
    // 每次找到岛屿，则直接把找到的岛屿改成0，这是传说中的沉岛思想，就是遇到岛屿就把他和周围的全部沉默。
    // ps：如果能用沉岛思想，那么自然可以用朋友圈思想。有兴趣的朋友可以去尝试。
    private int dfs(int i, int j, int[][] grid) {
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[i].length || grid[i][j] == 0) { 
            return 0;
        } 
        grid[i][j] = 0;
        int num = 1;
        num += dfs(i + 1, j, grid);
        num += dfs(i - 1, j, grid);
        num += dfs(i, j + 1, grid);
        num += dfs(i, j - 1, grid);
        return num;
        
    }
}
'''

class Solution:
    # 上右下左4个方向
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid and not grid[0]:
            return -1
        m = len(grid)
        n = len(grid[0])
        # 使用marked数组
        marked = [[0] * n for i in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if marked[i][j] == 0 and grid[i][j] == 1:
                    res = max(self.dfs(grid, i, j, m, n, marked), res)
        return res
    def dfs(self, grid, i, j, m, n, marked):
        res = 1
        # 标记marked数组
        marked[i][j] = 1
        for di_x, di_y in self.directions:
            row = i + di_x
            col = j + di_y
            # 如果未使用
            if 0 <= row < m and 0 <= col < n and marked[row][col] == 0 and grid[row][col] == 1:
                res += self.dfs(grid, row, col, m, n, marked)
            # else:
            #     res += 0
        return res
print(Solution().maxAreaOfIsland([[1,1],[1,0]]))