'''
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。
'''

# PS：皇后可以攻击同一行、同一列、左上左下右上右下四个方向的任意单位。
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 初始化棋盘
        board = [['.'] * n for _ in range(n)]
        self.res = []
        self.helper(board, 0)
        return self.res

    def helper(self, board, row):
        size = len(board)
        # 遍历当前行的所有列
        if row == size:
            self.res.append(board)
            return
        for i in range(size):
            # 剪枝
            if not self.isValid(board, row, i):
                continue
            # 路径选择
            board[row][i] = "Q"
            # 递归
            self.helper(board, row + 1)
            # 撤销选择
            board[row][i] = "."

    def isValid(self, board, row, col):
        n = len(board)
        # 判断这列是否非法
        for i in range(0, row):
            if board[i][col] == "Q":
                return False
        # 判断右对角线
        tmp_row = row
        tmp_col = col
        while tmp_col < n and tmp_row >= 0:
            if board[tmp_row][tmp_col] == "Q":
                return False
            tmp_col += 1
            tmp_row -= 1
        # 判断左对角线
        tmp_row = row
        tmp_col = col
        while tmp_row >= 0 and tmp_col >= 0:
            if board[tmp_row][tmp_col] == "Q":
                return False
            tmp_col -= 1
            tmp_row -= 1
        return True
print(Solution().solveNQueens(4))