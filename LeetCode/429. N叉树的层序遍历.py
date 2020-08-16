'''
给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
例如，给定一个 3叉树 :

返回其层序遍历:
[
     [1],
     [3,2,4],
     [5,6]
]

说明:
树的深度不会超过 1000。
树的节点总数不会超过 5000。
'''


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from collections import deque
from typing import List


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            tmp = []
            for i in range(size):
                node = queue.popleft()
                tmp.append(node.val)
                for i in node.children:
                    queue.append(i)
            res.append(tmp[:])
        return res
