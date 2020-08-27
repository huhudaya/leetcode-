'''

给定一棵二叉树，其中每个节点都含有一个整数数值(该值或正或负)。设计一个算法，打印节点数值总和等于某个给定值的所有路径的数量。注意，路径不一定非得从二叉树的根节点或叶节点开始或结束，但是其方向必须向下(只能从父节点指向子节点方向)。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

3
解释：和为 22 的路径有：[5,4,11,2], [5,8,4,5], [4,11,7]
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 前缀和+回溯
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict


class Solution:
    # 前缀和 + 回溯
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0
        hash = defaultdict(int)
        # 注意这里必须设置为1
        hash[0] = 1

        # 类似于560，使用hash优化前缀和的思想
        def dfs(root, cur, target):
            if root is None:
                return 0
            cur += root.val
            cnt = hash[cur - target]
            hash[cur] += 1
            left = dfs(root.left, cur, target)
            right = dfs(root.right, cur, target)
            hash[cur] -= 1
            return left + right + cnt

        return dfs(root, 0, sum)
