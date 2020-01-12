# 102. 二叉树的层次遍历.py
'''
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 迭代
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        cur_level = [root]
        while cur_level:
            tmp = []
            next_level = []
            for node in cur_level:
                tmp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(tmp)
            cur_level = next_level
        return res
# 递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        
        def helper(root, depth):
            if not root: return 
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
        helper(root, 0)
        return res

# 方法 1：递归
# 算法
# 最简单的解法就是递归，首先确认树非空，然后调用递归函数 helper(node, level)，参数是当前节点和节点的层次。程序过程如下：
# 输出列表称为 levels，当前最高层数就是列表的长度 len(levels)。比较访问节点所在的层次 level 和当前最高层次 len(levels) 的大小，如果前者更大就向 levels 添加一个空列表。
# 将当前节点插入到对应层的列表 levels[level] 中。
# 递归非空的孩子节点：helper(node.left / node.right, level + 1)。
# 实现
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            
        helper(root, 0)
        return levels
# 复杂度分析

# 时间复杂度：O(N)，因为每个节点恰好会被运算一次。
# 空间复杂度：O(N)，保存输出结果的数组包含 N 个节点的值。
'''
方法 2：迭代
算法

上面的递归方法也可以写成迭代的形式。

我们将树上顶点按照层次依次放入队列结构中，队列中元素满足 FIFO（先进先出）的原则。在 Java 中可以使用 Queue 接口中的 LinkedList实现。在 Python 中如果使用 Queue 结构，但因为它是为多线程之间安全交换而设计的，所以使用了锁，会导致性能不佳。因此在 Python 中可以使用 deque 的 append() 和 popleft() 函数来快速实现队列的功能。

第 0 层只包含根节点 root ，算法实现如下：

初始化队列只包含一个节点 root 和层次编号 0 ： level = 0。
当队列非空的时候：
在输出结果 levels 中插入一个空列表，开始当前层的算法。
计算当前层有多少个元素：等于队列的长度。
将这些元素从队列中弹出，并加入 levels 当前层的空列表中。
将他们的孩子节点作为下一层压入队列中。
进入下一层 level++。
实现
'''
from collections import deque
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        level = 0
        queue = deque([root,])
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level 
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.val)
                
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # go to next level
            level += 1
        
        return levels

# 复杂度分析

# 时间复杂度：O(N)，因为每个节点恰好会被运算一次。
# 空间复杂度：O(N)，保存输出结果的数组包含 N 个节点的值。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 借用队列
        res = []
        if root is None:
            return res
        queue = deque()
        queue.append(root)
        while queue:
            level = []
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res