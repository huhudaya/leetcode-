'''
您需要在二叉树的每一行中找到最大的值。

示例：

输入:

          1
         / \
        3   2
       / \   \
      5   3   9

输出: [1, 3, 9]
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# dfs
from typing import List


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []

        # dfs
        def dfs(root, depth):
            if root is None:
                return
            if len(res) == depth:
                res.append(root.val)
            res[depth] = max(res[depth], root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 0)
        return res


# bfs
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, cur = [], [root]
        while cur:
            nxt = []
            res.append(float("-inf"))
            for node in cur:
                res[-1] = max(res[-1], node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            cur = nxt
        return res
