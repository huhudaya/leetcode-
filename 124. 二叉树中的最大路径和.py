# 124二叉树中的最大路径和.py
'''
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class ResultType:
    def __init__(self,root2any,any2any):
        self.root2any = root2any
        self.any2any = any2any
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # any2any版本，需要resultType
        def help(root):
            if root is None:
                return ResultType(-sys.maxsize, -sys.maxsize)
            # divide
            left = help(root.left)
            right = help(root.right)
            # 注意这里的 0 的左右
            root2any = max(0, max(left.root2any, right.root2any)) + root.val
            any2any = max(0, left.any2any, right.any2any)
            tmp = max(left.root2any, 0) + max(right.root2any, 0) + root.val
            any2any = max(tmp, any2any)
            return ResultType(root2any, any2any)
        res = help(root)
        return res.root2any

    

