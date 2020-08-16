'''
给定一个二叉树，在树的最后一行找到最左边的值。

示例 1:

输入:

    2
   / \
  1   3

输出:
1
 
示例 2:
输入:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7
输出:
7
注意: 您可以假设树（即给定的根节点）不为 NULL。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        def dfs(root, depth):
            if root is None:
                return
            if depth > self.maxdepth:
                self.maxdepth = depth
                self.res = root.val
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        self.maxdepth = -1
        self.res = 0
        dfs(root, 0)
        return self.res
