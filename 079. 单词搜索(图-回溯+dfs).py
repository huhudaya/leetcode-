'''
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成
其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用

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
        # 因为涉及到回溯，所以一定是用DFS
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
            # 先占住位置，搜索不成功，就要释放掉，路径选择
            marked[start_x][start_y] = True
            for direction in self.directions:
                new_x = start_x + direction[0]
                new_y = start_y + direction[1]
                # 注意：如果这一次 search word 成功的话，就返回
                if 0 <= new_x < m \
                        and 0 <= new_y < n \
                        and not marked[new_x][new_y] \
                        and self._search_word(board, word, index + 1, new_x, new_y, marked, m, n):
                    return True
            # 否则回溯的时候恢复为False，撤销选择
            marked[start_x][start_y] = False
        return False


# 标准回溯模板
class Solution(object):
    # 定义上下左右四个行走方向
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        mark = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    # 即第一次已经将该元素标记为已使用，所以可以使用标准的回溯模板，如果第一次，即调用dfs之前并没有标记使用，这个时候需要在dfs递归函数中的for循环外面先进行一次标记使用
                    # 类比于257题目中，在调用dfs之前使用了helper(root, [str(root.val)], result)，这就相当于在dfs之前使用了root.val,所以可以使用标准的回溯模板，如果调用dfs之前传入的是helper(root, [], result)，那么在dfs内部for循环外面需要进行一次判断
                    mark[i][j] = 1
                    if not True != self.backtrack(i, j, mark, board, word[1:]):
                        return True
                    else:
                        # 回溯
                        mark[i][j] = 0
        return False

    def backtrack(self, i, j, mark, board, word):
        if len(word) == 0:
            return True

        for direct in self.directs:
            cur_i = i + direct[0]
            cur_j = j + direct[1]

            if cur_i >= 0 and cur_i < len(board) and cur_j >= 0 and cur_j < len(board[0]) and board[cur_i][cur_j] == \
                    word[0]:
                # 如果是已经使用过的元素，忽略
                if mark[cur_i][cur_j] == 1:
                    continue
                # 将该元素标记为已使用
                mark[cur_i][cur_j] = 1
                if self.backtrack(cur_i, cur_j, mark, board, word[1:]) == True:
                    return True
                else:
                    # 回溯
                    mark[cur_i][cur_j] = 0
        return False
