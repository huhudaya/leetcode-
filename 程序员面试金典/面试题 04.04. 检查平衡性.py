'''
实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。


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
返回 false 。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 做好递归函数的定义,这里定义dfs(root)为以root为根节点的最大长度
        def dfs(root) -> int:
            if root is None:
                return True
            left = dfs(root.left)
            right = dfs(root.right)
            if left == -1 or right == -1:
                return -1
            if abs(left - right) >= 2:
                return -1
            return max(left, right) + 1

        return dfs(root) != -1


# 使用一个flag变量
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 做好递归函数的定义,这里定义dfs(root)为以root为根节点的最大长度
        self.flag = True

        def dfs(root) -> int:
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left - right) >= 2:
                self.flag = False
            return max(left, right) + 1

        dfs(root)
        return self.flag


# 最优解
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 做好递归函数的定义,这里定义dfs(root)为以root为根节点的最大长度
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
