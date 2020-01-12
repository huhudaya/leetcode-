# 094. 二叉树的中序遍历.py
'''
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 非递归
class Solution:
    def inorderTraversal(self, root: TreeNode):
        # 非递归 先压左，压到底
        if root is None:
            return None
        stack = []
        res = []
        while stack or root:
            # while root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                res.append(node.val)
                root = node.right
        return res


# 递归
class Solution:
    def inorderTraversal(self, root: TreeNode):
        res = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(root)
        return res
