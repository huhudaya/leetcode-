'''
给定一个 N 叉树，返回其节点值的前序遍历。
例如，给定一个 3叉树 :
返回其前序遍历: [1,3,5,6,2,4]。
说明: 递归法很简单，你可以使用迭代法完成此题吗?
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # 递归
        if root is None:
            return []
        res = []
        res.append(root.val)
        for i in root.children:
            res.extend(self.preorder(i))
        return res

# 迭代
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])

        return output