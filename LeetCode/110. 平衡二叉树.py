'''
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.depth(root) != -1

    def depth(self, root):
        if root is None:
            return 0
        left = self.depth(root.left)
        if left == -1:
            return -1
        right = self.depth(root.right)
        if right == -1:
            return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left == -1 or right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            # 返回高度
            return max(left, right) + 1

        return dfs(root) != -1
