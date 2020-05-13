'''

给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。
一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
示例 1:
输入:
11110
11010
11000
00000
输出: 1

示例 2:
输入:
11000
11000
00100
00011
输出: 3
'''
from typing import List
# DFS
# 明白题的意思，其实就是上下左右相连，都算一个岛屿，相当于求图中有几个连通域问题，即并查集
# 按照 上，右，下，左来进行遍历
class Solution:
    # 方向数组，它表示了相对于当前位置的 4 个方向的横、纵坐标的偏移量，这是一个常见的技巧 定义一个类属性，在内部使用self.val来进行访问，也可以定义一个全局变量，在方法内部使用global val
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    def numIslands(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        # marked = [[False] * n for _ in range(m)]
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        # 从第 1 行、第 1 格开始，对每一格尝试进行一次 DFS 操作
        for i in range(m):
            for j in range(n):
                # 只要是陆地，且没有被访问过的，就可以使用 DFS 发现与之相连的陆地，并进行标记，否则就进行深度优先搜索，找到所有符合要求的路径
                if marked[i][j] is False and grid[i][j] == '1':
                    count += 1
                    self.__dfs(grid, i, j, m, n, marked)
            return count

    def __dfs(self, grid, i, j, m, n, marked):
        marked[i][j] = True
        for direct in self.directions:
            row = i + direct[0]
            column = j + direct[1]
            if 0 <= row < m and 0 <= column < n and marked[row][column] is False and grid[row][column] == '1':
                self.__dfs(grid, row, column, m, n, marked)


class Solution:
    #        x-1,y
    # x,y-1    x,y      x,y+1
    #        x+1,y
    # 方向数组，它表示了相对于当前位置的 4 个方向的横、纵坐标的偏移量，这是一个常见的技巧
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        # 特判
        if m == 0:
            return 0
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        # 从第 1 行、第 1 格开始，对每一格尝试进行一次 DFS 操作
        for i in range(m):
            for j in range(n):
                # 只要是陆地，且没有被访问过的，就可以使用 DFS 发现与之相连的陆地，并进行标记
                if marked[i][j] is False and grid[i][j] == '1':
                    # count 可以理解为连通分量，你可以在深度优先遍历完成以后，再计数，
                    # 即这行代码放在【位置 1】也是可以的
                    count += 1
                    self.__dfs(grid, i, j, m, n, marked)
                    # 【位置 1】
        return count

    def __dfs(self, grid, i, j, m, n, marked):
        marked[i][j] = True
        for direction in self.directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
                self.__dfs(grid, new_i, new_j, m, n, marked)


# BFS
# 所有加入队列的结点，都应该马上被标记为 “已经访问”，否则有可能会被重复加入队列。
from typing import List
from collections import deque
class Solution():
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    def numIslands(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        count = 0
        marked = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if marked[i][j] is False and grid[i][j] == '1':
                    # 标记第一个节点已经被访问过
                    marked[i][j] = True
                    # count记录岛屿的数量 只要没有标记过并且当前节点是1，就一定存在一个孤立的岛屿！
                    count += 1
                    queue = deque()
                    # 先入队
                    queue.append((i, j))
                    while queue:
                        # 出队
                        row, column = queue.popleft()
                        # 上下左右的顺序来bfs，标记完之后继续入队
                        for dir in self.directions:
                            row = row + dir[0]
                            column = column + dir[1]
                            if 0 <= row < m and 0 <= column < n and not marked[row][column] and grid[row][column] == '1':
                                queue.append((row, column))
                                marked[row][column] = True
        return count


from typing import List
from collections import deque


class Solution:
    #        x-1,y
    # x,y-1    x,y      x,y+1
    #        x+1,y
    # 方向数组，它表示了相对于当前位置的 4 个方向的横、纵坐标的偏移量，这是一个常见的技巧
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        # 特判
        if m == 0:
            return 0
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        # 从第 1 行、第 1 格开始，对每一格尝试进行一次 DFS 操作
        for i in range(m):
            for j in range(n):
                # 只要是陆地，且没有被访问过的，就可以使用 BFS 发现与之相连的陆地，并进行标记
                if not marked[i][j] and grid[i][j] == '1':
                    # count 可以理解为连通分量，你可以在广度优先遍历完成以后，再计数，
                    # 即这行代码放在【位置 1】也是可以的
                    count += 1
                    queue = deque()
                    queue.append((i, j))
                    # 注意：这里要标记上已经访问过
                    marked[i][j] = True
                    while queue:
                        cur_x, cur_y = queue.popleft()
                        # 得到 4 个方向的坐标
                        for direction in self.directions:
                            new_i = cur_x + direction[0]
                            new_j = cur_y + direction[1]
                            # 如果不越界、没有被访问过、并且还要是陆地，我就继续放入队列，放入队列的同时，要记得标记已经访问过
                            if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][
                                new_j] == '1':
                                queue.append((new_i, new_j))
                                # 【特别注意】在放入队列以后，要马上标记成已经访问过，语义也是十分清楚的：反正只要进入了队列，你迟早都会遍历到它
                                # 而不是在出队列的时候再标记
                                # 【特别注意】如果是出队列的时候再标记，会造成很多重复的结点进入队列，造成重复的操作，这句话如果你没有写对地方，代码会严重超时的
                                marked[new_i][new_j] = True
                    # 【位置 1】
        return count
