'''
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true
限制：

0 <= 节点个数 <= 10000
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def dfs(p, q) -> bool:
            if q is None:
                return True
            if p is None:
                return False
            return isSub(p, q) or dfs(p.left, q) or dfs(p.right, q)

        def isSub(p, q) -> bool:
            if q is None:
                return True
            if p is None:
                return False
            if p.val != q.val:
                return False
            return isSub(p.left, q.left) and isSub(p.right, q.right)

        return dfs(A, B)


# 简洁版本
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def dfs(p, q) -> bool:
            if p is None or q is None:
                return False
            return isSub(p, q) or dfs(p.left, q) or dfs(p.right, q)

        def isSub(p, q) -> bool:
            if q is None: return True
            if p is None: return False
            if p.val != q.val: return False
            # 注意，这里一定是and,因为两个子树要完全相同
            return isSub(p.left, q.left) and isSub(p.right, q.right)

        return dfs(A, B)
