'''
返回与给定的前序和后序遍历匹配的任何二叉树。

 pre 和 post 遍历中的值是不同的正整数。

 

示例：

输入：pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
输出：[1,2,3,4,5,6,7]
 

提示：

1 <= pre.length == post.length <= 30
pre[] 和 post[] 都是 1, 2, ..., pre.length 的排列
每个输入保证至少有一个答案。如果有多个答案，可以返回其中一个。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructFromPrePost(self, pre, post):
        if not pre:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root

        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:L + 1], post[:L])
        root.right = self.constructFromPrePost(pre[L + 1:], post[L:-1])
        return root


# 自己的版本
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        # 递归
        # 注意到后序遍历的特点，后序遍历的最后一个节点为根节点
        # 前序遍历的第一个节点为根节点
        # 后序遍历是先左后右
        if len(post) == 0:
            return None
        n = len(pre)
        root = TreeNode(pre[0])
        # 如果pre[1]不存在，就返回pre[0]作为root
        if n == 1:
            return root
        L = post.index(pre[1])
        # L + 2 - 1 == L + 1  这里是将后序遍历的左节点的个数转换为前序遍历的个数，从而对应为数组的索引
        root.left = self.constructFromPrePost(pre[1:L + 2], post[:L + 1])
        root.right = self.constructFromPrePost(pre[L + 2:], post[L + 1:-1])
        return root