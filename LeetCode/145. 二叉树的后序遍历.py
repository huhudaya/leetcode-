# 145. 二叉树的后序遍历.py
'''
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
'''
from typing import List


# 递归
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            helper(root.right)
            res.append(root.val)

        helper(root)
        return res


from collections import deque


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 非递归
        stack = []
        # 这里使用一个双端队列，直接在首部O(1)的插入元素，避免逆序整个栈
        res = deque()
        if root is None:
            return []
        # 后序为左右中，前序为中左右，中序为前中右====>后序(左右中)=伪前序入栈(中右左)+出栈(左右中)
        stack.append(root)
        while stack:
            node = stack.pop()
            res.appendleft(node.val)
            # 先压左 在压右
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return list(res)
