# 114. 二叉树展开为链表.py
'''
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 前序遍历
    # 类变量
    # last_node = None
    # def flatten(self, root: TreeNode) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     if root is None:
    #         return
    #     if self.last_node is not None:
    #         self.last_node.left = None
    #         self.last_node.right = root
    #     self.last_node = root
    #     right = root.right
    #     self.flatten(root.left)
    #     self.flatten(root.right)

    # divide&conquer
    def flatten(self, root):
        self.helper(root)
    def helper(self,root):
        if root is None:
            return None
        left = self.helper(root.left)
        right = self.helper(root.right)
        # if !left:
        if left is not None:
            left.right = root.right
            root.right = root.left
            root.left = None
        # 因为要返回最后一个值
        if right is not None:
            return right
        if left is not None:
            return left
        return root
