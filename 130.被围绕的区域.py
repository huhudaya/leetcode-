'''

给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:

被围绕的区间不会存在于边界上
换句话说，任何边界上的 'O' 都不会被填充为 'X'。
任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。
如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
'''


# 分析
'''
分析:
本题可以用 DFS（深度优先搜索）解决。

找到所有被 X 围绕的区域不容易，但是其等价于找到所有没有没有被 X 围绕的区域（连接边界的区域），这样就可以从边界上的 O 开始进行深度优先搜索，

举个例子：

X X X X
X X O X
X O X X
X O X X
对于上面这张图的边界，只有第四行第二列的内容是 O，我们对其进行 DFS，即 DFS(3,1)
首先将它本身改为 #

X X X X
X X O X
X O X X
X # X X
之后对该位置的上下左右进行搜索，即分别尝试 DFS(2,1)，DFS(4,1)，DFS(3,0)，DFS(3,2)，如果越界或者内容不是 O 则停止搜索。

因为此位置左右是 X，下面超出数组下边界，只有上面是 O，所以继续进行 DFS(2,1)。

X X X X
X X O X
X # X X
X # X X
和之前一样，先将其本身改为 #，之后上下左右进行 DFS，而对于此坐标上下左右都不是 O，所以搜索结束。

最后遍历全图，将所有的#改为 O，所有的 O 改为 X 即可。

最终结果：

X X X X
X X X X
X O X X
X O X X
'''

from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        def dfs(i, j):
            board[i][j] = "B"
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                tmp_i = i + x
                tmp_j = j + y
                if 1 <= tmp_i < row and 1 <= tmp_j < col and board[tmp_i][tmp_j] == "O":
                    dfs(tmp_i, tmp_j)

        for j in range(col):
            # 第一行
            if board[0][j] == "O":
                dfs(0, j)
            # 最后一行
            if board[row - 1][j] == "O":
                dfs(row - 1, j)

        for i in range(row):
            # 第一列
            if board[i][0] == "O":
                dfs(i, 0)
            # 最后一列
            if board[i][col-1] == "O":
                dfs(i, col - 1)

        for i in range(row):
            for j in range(col):
                # O 变成 X
                if board[i][j] == "O":
                    board[i][j] = "X"
                # B 变成 O
                if board[i][j] == "B":
                    board[i][j] = "O"

# 这道题的核心思路就是转变条件，我们先从四条边界中的"O"开始DFS，如果找到一条路径，这证明这个"O"不能被包围，所以不能变成X
# 我们将不能变成X的"O"重写为"#"，遍历完之后，"#"恢复为"O"，其余的变成"X"

class Solution:
    # 上右下左的顺时针
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])
        def __dfs(i, j):
            board[i][j] = "#"
            for x, y in self.directions:
                tmp_i = i + x
                tmp_j = j + y
                # 一定要注意这里的逻辑，是大于等于1！！！！！ 因为不能包括边界
                if 1 <= tmp_i < row and 1 <= tmp_j < col and board[tmp_i][tmp_j] == "O":
                    dfs(tmp_i, tmp_j)
        for j in range(col):
            # 第一行
            if board[0][j] == "O":
                __dfs(0, j)
            # 最后一行
            if board[row - 1][j] == "O":
                __dfs(row - 1, j)
        for i in range(row):
            # 第一列
            if board[i][0] == "O":
                __dfs(i, 0 )
            # 最后一列
            if board[i][col - 1] == "O":
                __dfs(i, col - 1)
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    # 注意这里应该是 =，我写成了 == 。。。。。。。悲剧
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"