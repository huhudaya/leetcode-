'''
给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。

 

示例：

输入：[1,2,3,4,5,null,7,8]

        1
       /  \
      2    3
     / \    \
    4   5    7
   /
  8

输出：[[1],[2,3],[4,5,7],[8]]
通过次数7,122提交次数8,835
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import List


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        if tree is None:
            return []
        res = []

        def dfs(root, depth):
            if root is None:
                return
            if len(res) == depth:
                res.append(ListNode(root.val))
            else:
                head = ListNode(root.val)
                head.next = res[depth]
                res[depth] = head
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)

        dfs(tree, 0)
        return res
