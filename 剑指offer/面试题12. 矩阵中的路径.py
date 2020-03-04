'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

 

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
提示：

1 <= board.length <= 200
1 <= board[i].length <= 200
注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/

'''
from typing import List

# 好的解题思路
# https://leetcode-cn.com/problems/word-search/solution/zai-er-wei-ping-mian-shang-shi-yong-hui-su-fa-pyth/
class Solution:
    directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        marked = [[False] * n for i in range(m)]
        # 对每一个格子进行遍历，注意到这与200题的不同
        for i in range(m):
            for j in range(n):
                if self._dfs(board, word, 0, i, j, marked, m, n):
                    return True
        return False

    def _dfs(self, board, word, index, start_x, start_y, marked, m, n):
        # 回溯递归终止条件
        if index == len(word) - 1:
            return board[start_x][start_y] == word[index]
        # 中间是否匹配
        if board[start_x][start_y] == word[index]:
            # 先占住位置，搜索不成功，就要释放掉
            marked[start_x][start_y] = True
            # N叉树递归
            for direction in self.directions:
                new_x = start_x + direction[0]
                new_y = start_y + direction[1]
                if 0 <= new_x < m and 0 <= new_y < n and not marked[new_x][new_y] and self._dfs(board, word, index + 1,
                                                                                                new_x, new_y, marked, m,
                                                                                                n):
                    return True
            # 四个方向遍历完之后，需要回溯，重置标志位
            marked[start_x][start_y] = False
        return False
