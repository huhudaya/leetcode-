'''
给定一棵二叉搜索树，请找出其中第k大的节点。

 

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
 

限制：

1 ≤ k ≤ 二叉搜索树元素个数
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # 使用中序遍历，传统中序遍历为左右中，所以改变一下，用右左中，这样就是从大到小排列的了
        res = []
        path = 0
        while root or res:
            # 因为要左右中，所以先压右边
            if root:
                res.append(root)
                root = root.right
            else:
                tmp = res.pop()
                path += 1
                if path == k:
                    return tmp.val
                root = tmp.left
        return -1
