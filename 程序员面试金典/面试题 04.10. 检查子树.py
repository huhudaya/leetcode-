'''
检查子树。你有两棵非常大的二叉树：
T1，有几万个节点；T2，有几万个节点。
设计一个算法，判断 T2 是否为 T1 的子树。

如果 T1 有这么一个节点 n，其子树与 T2 一模一
，则 T2 为 T1 的子树，也就是说，从节点 n 处把树砍断，得到的树与 T2 完全相同。

示例1:

 输入：t1 = [1, 2, 3], t2 = [2]
 输出：true
示例2:

 输入：t1 = [1, null, 2, 4], t2 = [3, 2]
 输出：false
提示：

树的节点数目范围为[0, 20000]。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        def dfs(t1, t2) -> bool:
            if t2 is None:
                return True
            if t1 is None:
                return False
            return isSub(t1, t2) or dfs(t1.left, t2) or dfs(t1.right, t2)

        def isSub(t1, t2) -> bool:
            if t2 is None:
                return True
            if t1 is None:
                return False
            if t1.val != t2.val:
                return False
            return isSub(t1.left, t2.left) and isSub(t1.right, t2.right)

        return dfs(t1, t2)
