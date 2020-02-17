'''
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.
链接：https://leetcode-cn.com/problems/word-search
'''
# 因为涉及到状态重置等等 所以一定是使用回溯法，而回溯又必须使用深度优先搜索算法
# 很明显这道题应该使用 回溯+DFS
# 时间复杂度是 O(m*n*m*n) 因为需要对每一个格子进行搜索
from typing import List

class Solution:
    directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    def exist(self, board, word):
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        marked = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # 不同于200题的岛屿数量，这里每一个格子都需要遍历一次，所以上一次的状态需要清除
                if self._search_word(board, word, 0, i, j, marked, m, n):
                    return True
        return False

    def _search_word(self, board, word, index, start_x, start_y, marked, m, n):
        # 回溯的递归终止条件
        if index == len(word) - 1:
            return board[start_x][start_x] == word[index]
        # 中间是否匹配
        if board[start_x][start_y] == word[index]:
            # 先占住位置，搜索不成功，就要释放掉
            marked[start_x][start_y] = True
            for direction in self.directions:
                new_x = start_x + direction[0]
                new_y = start_y + direction[1]
                # 注意：如果这一次 search word 成功的话，就返回
                if 0 <= new_x < m \
                        and 0 <= new_y < n \
                        and not marked[new_x][new_y] \
                        and self._search_word(board, word,index + 1,new_x, new_y,marked, m, n):
                    return True
            # 否则回溯的时候恢复为False
            marked[start_x][start_y] = False
        return False