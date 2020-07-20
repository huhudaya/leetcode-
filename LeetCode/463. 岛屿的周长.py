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


# 直接遍历
# 只看左边和上边 遇见岛屿相邻或者就减2
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 如果找见了一个grip为1，则一定从这里入口，因为题目规定了只有一个岛屿
                if grid[i][j] == 1:
                    res += 4
                    # 这里判断一下左边和上边，如果是岛屿和岛屿连接，则减去2
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        res -= 2
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        res -= 2
        return res


# dfs
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        for i in range(row):
            for j in range(col):
                # 因为题目说只有一个岛屿
                if grid[i][j] == 1:
                    # 看四个方向 边界或者 邻居是水 周长 + 1
                    for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        tmp_i, tmp_j = i + x, j + y
                        # 水域边界或者是网格边界 + 1
                        if not (0 <= tmp_i < row and 0 <= tmp_j < col) or grid[tmp_i][tmp_j] == 0:
                            res += 1
                # 这里直接return就可以了，因为只有一个岛屿
                return res
        return res


# DFS
# // 将这个“相邻关系”对应到 DFS 遍历中，就是：每当在 DFS 遍历中，从一个岛屿方格走向一个非岛屿方格，就将周长加 1。代码如下：
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

// 将这个“相邻关系”对应到 DFS 遍历中，就是：每当在 DFS 遍历中，从一个岛屿方格走向一个非岛屿方格，就将周长加 1。代码如下：
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


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 顺时针
        direcitons = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        if not grid or not grid[0]:
            return -1
        m = len(grid)
        n = len(grid[0])
        res = 0
        # 直接遍历
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for di in direcitons:
                        row = i + di[0]
                        col = j + di[1]
                        # 如果是网格边界或者和水域连接，返回0
                        if not (0 <= row < m and 0 <= col < n) or grid[row][col] == 0:
                            res += 1
        return res
