'''
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]
 

提示：

节点总数 <= 1000
通过次数24,413提交次数37,836
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


# dfs
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []

        def dfs(node, level):
            if not node:
                return
            if level == len(res):
                res.append([])
            res[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        # flatten
        for i in range(1, len(res)):
            res[0] += res[i]
        return res[0]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        # 递归
        if not root:
            return []
        res = [[root.val]]

        def dfs(root, level):
            if root.left is None and root.right is None:
                return
            if len(res) == level:
                res.append([])
            if root.left:
                res[level].append(root.left.val)
                dfs(root.left, level + 1)
            if root.right:
                res[level].append(root.right.val)
                dfs(root.right, level + 1)

        dfs(root, 1)
        ans = []
        for i in res:
            ans.extend(i)
        return ans


# bfs
import collections
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
