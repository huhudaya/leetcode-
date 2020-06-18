# 104二叉树的最大深度.py
'''
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# traverse
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.depth = 0

        def help(root, curDepth):
            # basecase
            if root is None:
                return
            # 先序遍历，相当于子顶向下
            self.depth = max(curDepth, self.depth)
            help(root.left, curDepth + 1)
            help(root.right, curDepth + 1)

        help(root, 1)
        return self.depth


# divide&conquer 相当于后序遍历
# 有返回值的递归一定要先写递归结束条件
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # 相当于后序遍历，自底向上
        res = max(left, right)
        return res + 1
# BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = deque([root])
        level = 0
        while q:
            n = len(q)
            level += 1
            for i in range(n):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return level