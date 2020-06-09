'''
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List
# 递归
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root, depth):
            if root is None:
                return
            if len(res) == depth:
                res.append(0)
            res[depth] = root.val
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
        helper(root, 0)
        return res