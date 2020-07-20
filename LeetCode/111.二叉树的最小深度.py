'''

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
'''


# BFS用来解决最短路径问题，这类问题如果使用DFS时间复杂度会比较高
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import sys
from collections import deque
class Solution:
    # BFS
    def minDepth1(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = deque([root])
        level = 0
        res = sys.maxsize
        while q:
            n = len(q)
            level += 1
            for i in range(n):
                node = q.popleft()
                #/* 判断是否到达终点 */
                if not node.right and not node.left:
                    return level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
    # 递归
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        # 相当于后序遍历，自底向上
        if right == 0 or left == 0:
            res = left if right == 0 else right
        else:
            res = min(left, right)
        return res + 1

'''
class Solution {
    public int minDepth(TreeNode root) {
        if(root == null){
            return 0;
        }
        if(root.left != null && root.right !=null){
            return Math.min(minDepth(root.left),minDepth(root.right))+1;
        }
        return root.left!=null? minDepth(root.left)+1:minDepth(root.right)+1; 
    }
}
'''