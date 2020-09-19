'''

从左向右遍历一个数组，通过不断将其中的元素插入树中可以逐步地生成一棵二叉搜索树。
给定一个由不同节点组成的二叉搜索树，输出所有可能生成此树的数组。


示例：
给定如下二叉树

        2
       / \
      1   3
返回：
[
   [2,1,3],
   [2,3,1]
]



        2
       / \
      1   4
         /
        3
返回
[
   [2,1,4,3],
   [2,4,1,3],
   [2,4,3,1]
]
'''

'''
使用一个queue存储下个所有可能的节点
然后选择其中一个作为path的下一个元素
递归直到queue元素为空
将对应的path加入结果中
由于二叉搜索树没有重复元素, 而且每次递归的使用元素的顺序都不一样, 所以自动做到了去重
'''


# 题意
# 数组的第一个元素，必定对应于二叉搜索树的树根。
# 一个节点对应的子节点在序列上必定在父节点元素之后，如上图子节点1、3在输出的序列中必定在父节点2之后。
# 猜想：各个序列的差异主要是子树的插入顺序不同，例如此例子可以对应先插左子树后插右子树，或者是先插右子树再插左子树。
# 意思就是某个节点的儿子节点在数组中的位置都必须在它的父亲节点的后面

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [[]]
        res = []

        def findPath(cur, q, path):
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            if not q:
                res.append(path)
                return
            for i, nex in enumerate(q):
                newq = q[:i] + q[i + 1:]
                findPath(nex, newq, path + [nex.val])

        findPath(root, [], [root.val])
        return res
