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


# 递归中序遍历
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.pre = None

        # 这种递归有点抽象，需要好好理解一下
        # pre的值得变换规律是按中序排序的，先左再中后右边
        def isBST(root):
            if not root:
                return True
            if not isBST(root.left):
                return False
            if self.pre and self.pre.val >= root.val:
                return False
            self.pre = root
            # print(root.val)
            return isBST(root.right)

        return isBST(root)


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


a = TreeNode(10)
b = TreeNode(2)
c = TreeNode(12)
d = TreeNode(3)
e = TreeNode(14)
a.left = b
a.right = c
c.left = d
c.right = e
print(Solution().isValidBST(a))
