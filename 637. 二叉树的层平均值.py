# 637. 二叉树的层平均值.py
'''
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.

示例 1:

输入:
    3
   / \
  9  20
    /  \
   15   7
输出: [3, 14.5, 11]
解释:
第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].

链接：https://leetcode-cn.com/problems/average-of-levels-in-binary-tree
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode):
        # 双端队列
        res = []
        if root is None:
            return res
        queue = deque()
        queue.append(root)
        while queue:
            level = []
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(sum(level)/len(level))
        return res
