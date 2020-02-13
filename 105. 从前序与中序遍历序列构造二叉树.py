'''
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
核心思想
如上文所提到的，先序遍历的顺序是 Root -> Left -> Right，这就能方便的从根开始构造一棵树。

首先，preorder 中的第一个元素一定是树的根，这个根又将 inorder 序列分成了左右两棵子树。
现在我们只需要将先序遍历的数组中删除根元素，然后重复上面的过程处理左右两棵子树。
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 前序 中序 ->树
        if len(inorder) == 0:
            return None
        # 注意 先序遍历的第一个元素一定是树的根，这个根又可以将中序遍历分为左右两颗子树
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        # preorder[1: mid + 1]这里相当于指定左边的数量
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root