'''
给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。

网格中的格子水平和垂直方向相连（对角线方向不相连）。
整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。
格子是边长为 1 的正方形。
网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

示例 :
输入:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

输出: 16

解释: 它的周长是下面图片中的 16 个黄色的边：

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/island-perimeter
'''
'''
直接遍历，如果当前值为1，加4（四条边），如果左边有1，减2（两条边重合），上面有1，减2。
最后相加即可
'''
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += 4
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        res -= 2
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        res -= 2
        return res


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    # 看四个方向 边界或者 邻居是水 周长 + 1
                    for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        tmp_i, tmp_j = i + x, j + y
                        if not (0 <= tmp_i < row and 0 <= tmp_j < col) or grid[tmp_i][tmp_j] == 0:
                            res += 1
        return res

# dfs
'''
public int islandPerimeter(int[][] grid) {
    for (int r = 0; r < grid.length; r++) {
        for (int c = 0; c < grid[0].length; c++) {
            if (grid[r][c] == 1) {
                // 题目限制只有一个岛屿，计算一个即可
                return dfs(grid, r, c);
            }
        }
    }
    return 0;
}

int dfs(int[][] grid, int r, int c) {
    // 网格边界
    if (!(0 <= r && r < grid.length && 0 <= c && c < grid[0].length)) {
        return 1;
    }
    // 和水域连接
    if (grid[r][c] == 0) {
        return 1;
    }
    // 其他情况需要返回0
    if (grid[r][c] != 1) {
        return 0;
    }
    // 遍历过的需要置为2
    grid[r][c] = 2;
    return dfs(grid, r - 1, c)
        + dfs(grid, r + 1, c)
        + dfs(grid, r, c - 1)
        + dfs(grid, r, c + 1);
}
'''