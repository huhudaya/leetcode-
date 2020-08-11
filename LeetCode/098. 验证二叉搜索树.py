# 098. 验证二叉搜索树.py
'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

链接：https://leetcode-cn.com/problems/validate-binary-search-tree
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归 中序遍历的方式
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(root)
        return res == sorted(res) and len(set(res)) == len(res)


# 中序遍历迭代的方式 迭代
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        p = root
        pre = None
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            if pre and p.val <= pre.val:
                return False
            pre = p
            p = p.right
        return True


# 递归中序遍历+剪枝
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 使用一个变量存储上一个值
        self.pre = None

        def dfs(root):
            if root is None:
                return True
            # 中序遍历
            if dfs(root.left) is False:
                return False
            # 这个时候是中序遍历！！
            if self.pre and root.val <= self.pre.val:
                return False
            # 否则更新pre
            self.pre = root
            return dfs(root.right)

        return dfs(root)


# 自己版本的递归
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 递归
        self.pre = None
        def dfs(root):
            if root is None:
                return True
            left = dfs(root.left)
            if self.pre and root.val <= self.pre.val:
                return False
            self.pre = root
            right = dfs(root.right)
            return left and right
        return dfs(root)

# 最大最小值
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isBST(root, min_val, max_val):
            if root == None:
                return True
            # print(root.val)
            if root.val >= max_val or root.val <= min_val:
                return False
            return isBST(root.left, min_val, root.val) and isBST(root.right, root.val, max_val)

        return isBST(root, float("-inf"), float("inf"))
