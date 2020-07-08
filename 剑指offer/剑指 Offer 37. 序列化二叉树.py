# 297. 二叉树的序列化与反序列化.py
'''
序列化是将一个数据结构或者对象转换为连续的比特位的操作
进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境
采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。
这里不限定你的序列 / 反序列化算法执行逻辑
你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。
你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# traverse+divide&conquer
from collections import deque


class Codec:
    # traverse+divide&conquer
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "#!"
        # 先序遍历方式序列化
        res = str(root.val) + "!"
        res += self.serialize(root.left)
        res += self.serialize(root.right)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        queue = deque()
        values = data.split("!")
        n = len(values)
        for i in range(n):
            queue.append(values[i])
        return self.helper(queue)

    def helper(self, queue):
        # 每次从队列中弹出一个 这个时候就相当于前序遍历
        value = queue.popleft()
        if value == "#":
            return None
        head = TreeNode(value)
        head.left = self.helper(queue)
        head.right = self.helper(queue)
        return head
    # Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


# 思考
# 不要纠结细节，因为是按先序遍历的，画一画图，出队列的时候也按照先序的顺序出，就可以了。
# 遇见#就是None,就继续先序遍历
