'''
设想有个机器人坐在一个网格的左上角，网格 r 行 c 列。
机器人只能向下或向右移动，但不能走到一些被禁止的网格（有障碍物）。
设计一种算法，寻找机器人从左上角移动到右下角的路径。

网格中的障碍物和空位置分别用 1 和 0 来表示。

返回一条可行的路径，路径由经过的网格的行号和列号组成。左上角为 0 行 0 列。如果没有可行的路径，返回空数组。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: [[0,0],[0,1],[0,2],[1,2],[2,2]]
解释:
输入中标粗的位置即为输出表示的路径，即
0行0列（左上角） -> 0行1列 -> 0行2列 -> 1行2列 -> 2行2列（右下角）
说明：r 和 c 的值均不超过 100。
'''

# 回溯算法
# 用一个Boolean变量作为标记，如果找到一条路径就直接return，相当于提前剪枝
from typing import List


class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        directions = [[0, 1], [1, 0]]
        res = []
        marked = [[False] * n for i in range(m)]

        def dfs(i, j, path):
            marked[i][j] = True
            if obstacleGrid[i][j] == 1:
                return False
            # 使用回溯
            path.append([i, j])
            if i == m - 1 and j == n - 1:
                return True
            for di in directions:
                row = i + di[0]
                col = j + di[1]
                if not (0 <= row < m and 0 <= col < n):
                    continue
                if obstacleGrid[row][col] == 1 or marked[row][col]:
                    continue
                if dfs(row, col, path):
                    return True
            # 回溯 pop
            path.pop()
            return False

        dfs(0, 0, res)
        return res
