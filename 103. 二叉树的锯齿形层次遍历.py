# 103. 二叉树的锯齿形层次遍历.py
'''
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 使用递归
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # dfs
        res = deque()
        def helper(root, depth):
            if not root: return 
            if len(res) == depth:
                # 使用双端队列
                res.append(deque())
            # 奇偶判断 depth & 1 == 0 为偶数 非0 为奇数
            if depth % 2 == 0:
                res[depth].append(root.val)
            else: 
                res[depth].appendleft(root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
        helper(root, 0)
        return res




# 也可以直接按102题的bfs思路来做 不过在最后输出的时候按层数的奇偶性判断一下是否反转
