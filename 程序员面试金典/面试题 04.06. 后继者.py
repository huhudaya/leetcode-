'''
设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。

如果指定节点没有对应的“下一个”节点，则返回null。

示例 1:

输入: root = [2,1,3], p = 1

  2
 / \
1   3

输出: 2
示例 2:

输入: root = [5,3,6,2,4,null,null,1], p = 6

      5
     / \
    3   6
   / \
  2   4
 /
1

输出: null
通过次数8,007提交次数13,707
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 二分
class Solution:

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        res = None
        cur = root
        while cur:
            if cur.val <= p.val:
                cur = cur.right
            else:
                res = cur
                cur = cur.left
        return res


'''
所谓 p 的后继节点，就是这串升序数字中，比 p 大的下一个。

如果 p 大于当前节点的值，说明后继节点一定在 RightTree
如果 p 等于当前节点的值，说明后继节点一定在 RightTree
如果 p 小于当前节点的值，说明后继节点一定在 LeftTree 或自己就是
递归调用 LeftTree，如果是空的，说明当前节点就是答案
如果不是空的，则说明在 LeftTree 已经找到合适的答案，直接返回即可

'''


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if root:
            if p.val >= root.val:
                return self.inorderSuccessor(root.right, p)
            else:
                if self.inorderSuccessor(root.left, p) is None:
                    return root
                else:
                    return self.inorderSuccessor(root.left, p)
        return None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        res = None
        # 二分 找到第一个比 p 的值大的节点
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                res = root
                root = root.left
        return res