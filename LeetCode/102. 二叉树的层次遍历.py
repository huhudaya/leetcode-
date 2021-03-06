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

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
            if not root:
                return
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)

        helper(root, 0)
        return res


# 自己的版本
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]

        def helper(root, depth):
            if not root.left and not root.right:
                return
            if len(res) == depth:
                res.append([])
            if root.left:
                # 如果孩子节点有值就提前就放进去
                res[depth].append(root.left.val)
                helper(root.left, depth + 1)
            if root.right:
                res[depth].append(root.right.val)
                helper(root.right, depth + 1)

        helper(root, 1)
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
        # 在最外层进行一次非空判断
        if not root:
            return levels

        def helper(node, level):
            # 如果递归函数外面进行了非空判断，里面就不用再进行非空判断了
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

'''
图解算法中的BFS算法的思想
1.创建一个队列，将要查找的人添加到队列中（先添加一度关系的）
2.从队列弹出一个人
3.检查判断是否找到，找到了即退出
4.没有找到就将这个人的朋友都添加到这个队列中（二度关系）

很重要的是：检查一个人之前，必须判断之前有没有检查过他，我们可以用一个列表来记录检查过的人
'''
from collections import deque


# 自己的版本 BFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 借用队列
        res = []
        if root is None:
            return res
        queue = deque()
        # bfs就是先添加一个元素到队里
        queue.append(root)
        while queue:
            level = []
            # 相当于一度关系
            size = len(queue)
            for i in range(size):
                # 从队列弹出一个元素
                node = queue.popleft()
                level.append(node.val)
                # 添加到队列中他的一度关系元素 在树中，是当前节点的左右节点
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res
# go
'''
func levelOrder(root *TreeNode) [][]int {
    ret := [][]int{}
    if root == nil {
        return ret
    }
    q := []*TreeNode{root}
    for i := 0; len(q) > 0; i++ {
        ret = append(ret, []int{})
        p := []*TreeNode{}
        for j := 0; j < len(q); j++ {
            node := q[j]
            ret[i] = append(ret[i], node.Val)
            if node.Left != nil {
                p = append(p, node.Left)
            }
            if node.Right != nil {
                p = append(p, node.Right)
            }
        }
        q = p
    }
    return ret
}
'''
'''
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
	//创建一个保存最终结果的二位切片
	var result [][]int

	//如果节点为空，直接返回
	if root == nil {
		return result
	}

	//创建一个队列，并把根节点从前端入队
	queue := list.New()
	queue.PushFront(root)

	for queue.Len() > 0 {
		//保存当前层数据的切片
		var curLevel []int
		//count：保存当前层节点个数
		count := queue.Len()

		for count > 0 {
			//从队列后端取出数据
			element := queue.Back()
			node := element.Value.(*TreeNode)
			curLevel = append(curLevel, node.Val)

			//把左右子节点依次从队列前端入队
			if node.Left != nil {
				queue.PushFront(node.Left)
			}
			if node.Right != nil {
				queue.PushFront(node.Right)
			}

			//删除节点，并把当前剩余节点数-1
			queue.Remove(element)
			count--
		}

		result = append(result, curLevel)
	}
	return result
}
'''

# dfs
'''
var res [][]int

func levelOrder(root *TreeNode) [][]int {
	res = [][]int{}
	dfs(root, 0)
	return res
}

func dfs(root *TreeNode, level int) {
	if root != nil {
		if len(res) == level {
			res = append(res, []int{})
		}
		res[level] = append(res[level], root.Val)
		dfs(root.Left, level+1)
		dfs(root.Right, level+1)
	}
}
'''


# 队列
'''
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
	var res [][]int
	if root == nil {
		return res
	}
	queue := make([]*TreeNode, 0)
	queue = append(queue, root)
	for len(queue) > 0 {
		l := len(queue)
		f := make([]int, 0)
		for i := 0; i < l; i++ {
			node := queue[i]
			ans = append(ans, node.Val)
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		res = append(res, ans)
		queue = queue[l:]
	}
	return res
}
'''