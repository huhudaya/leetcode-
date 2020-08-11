'''

给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母在一个单词中不允许被重复使用。

示例:

输入:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]
说明:
你可以假设所有输入都由小写字母 a-z 组成。

提示:
你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。
什么样的数据结构可以有效地执行这样的操作？
散列表是否可行？为什么？ 前缀树如何？
如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。
'''
from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # trie树
        root = {}
        for word in words:
            trie = root
            for i in word:
                trie = trie.setdefault(i, {})
            trie["end"] = "1"
        m = len(board)
        n = len(board[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        marked = [[False] * n for i in range(m)]
        res = []
        def dfs(i, j, trie, path):
            # 剪枝
            if board[i][j] not in trie:
                return
            trie = trie[board[i][j]]
            if "end" in trie and trie["end"] == "1":
                res.append(path)
                # 防止重复加入
                trie["end"] = "0"
            # 注意，这个marked不能在最上面使用，否则直接return了，就不能回溯了
            marked[i][j] = True
            for di in directions:
                row = i + di[0]
                col = j + di[1]
                if not (row >= 0 and row < m and col >= 0 and col < n):
                    continue
                if marked[row][col] is True:
                    continue
                dfs(row, col, trie, path + board[row][col])
            marked[i][j] = False
        for i in range(m):
            for j in range(n):
                dfs(i, j, root, board[i][j])
        return res

Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"])