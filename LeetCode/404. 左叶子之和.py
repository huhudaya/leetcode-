'''
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root):
            if root is None:
                return
            if root.left is None and root.right is None:
                return
            if root.left:
                if root.left.left is None and root.left.right is None:
                    self.res += root.left.val
                dfs(root.left)
            if root.right:
                dfs(root.right)

        dfs(root)
        return self.res
