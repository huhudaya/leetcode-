'''
你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。

示例：

输入：
[
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]
输出： [1,2,4]
提示：

0 < len(land) <= 1000
0 < len(land[i]) <= 1000
'''
from typing import List


# DFS
class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        m = len(land)
        n = len(land[0])
        # 周围的8个方向（包括斜对角）
        directions = [(0, 1), (1, 0), (1, 1), (-1, -1), (0, -1), (-1, 0), (-1, 1), (1, -1)]
        res = []
        seen = [[False] * n for i in range(m)]

        def dfs(i, j):
            seen[i][j] = True
            res = 1
            for di in directions:
                row = i + di[0]
                col = j + di[1]
                if not (row >= 0 and row < m and col >= 0 and col < n):
                    continue
                if seen[row][col]:
                    continue
                if land[row][col] == 0:
                    res += dfs(row, col)
            return res

        cnt = 0
        for i in range(m):
            for j in range(n):
                if not seen[i][j] and land[i][j] == 0:
                    cnt += 1
                    res.append(dfs(i, j))
        res.sort()
        return res
