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
import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ResultType:
    def __init__(self, root2any, any2any):
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


# 递归 traverse+divide&conquer
class TreeNode(object):
    """ Definition of a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0
            # max sum on the left and right sub-trees of node
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # the price to start a new path where `node` is a highest node
            price_newpath = node.val + left_gain + right_gain

            # update max_sum if it's better to start a new path
            # max_sum记录的是any2any和left2any,right2any的最大值
            max_sum = max(max_sum, price_newpath)

            # for recursion :
            # return the max gain if continue the same path
            return node.val + max(left_gain, right_gain)

        max_sum = float('-inf')
        max_gain(root)
        return max_sum


class Solution:
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0

            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)

            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            priceNewpath = node.val + leftGain + rightGain

            # 更新答案
            self.maxSum = max(self.maxSum, priceNewpath)

            # 返回节点的最大贡献值
            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum


# DFS 和二叉树的直径差不多，看看那道题！通过一个全局变量记录最好的结果
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # 注意这里的初始化的坑
        self.maxVal = root.val

        def dfs(root):
            if not root:
                return 0
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            self.maxVal = max(self.maxVal, root.val + left + right)
            return root.val + max(left, right)

        dfs(root)
        return self.maxVal

# java
'''
 * Definition for a binary tree node.
class Solution {
    int res;
    public int maxPathSum(TreeNode root) {
        res = root.val;
        dfs(root);
        return res;
    }
    private int dfs(TreeNode root){
        if (null == root) return 0;
        int left = Math.max(dfs(root.left), 0);
        int right = Math.max(dfs(root.right), 0);
        res = Math.max(res, left + right + root.val);
        return Math.max(left, right) + root.val;
    }
}
'''