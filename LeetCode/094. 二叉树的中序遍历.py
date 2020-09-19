# 094. 二叉树的中序遍历.py
'''
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 非递归
class Solution:
    def inorderTraversal(self, root: TreeNode):
        # 非递归 先压左，压到底
        if root is None:
            return None
        stack = []
        res = []
        while root or stack:
            # while root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                res.append(node.val)
                root = node.right
        return res


# 递归
class Solution:
    def inorderTraversal(self, root: TreeNode):
        res = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(root)
        return res


# java
'''
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        inorder(root, res);
        return res;
    }

    public void inorder(TreeNode root, List<Integer> res) {
        if (root == null) {
            return;
        }
        inorder(root.left, res);
        res.add(root.val);
        inorder(root.right, res);
    }
}
'''
# go
'''
func inorderTraversal(root *TreeNode) (res []int) {
	var inorder func(node *TreeNode)
	inorder = func(node *TreeNode) {
		if node == nil {
			return
		}
		inorder(node.Left)
		res = append(res, node.Val)
		inorder(node.Right)
	}
	inorder(root)
	return
}



func inorderTraversal(root *TreeNode) []int {
	var result []int

	var inOrder func(root *TreeNode) []int
	inOrder = func(root *TreeNode) []int {
		if root == nil {
			return result
		}
		inOrder(root.Left)
		result = append(result, root.Val)
		inOrder(root.Right)
		return result
	}

	inOrder(root)
	return result
}
'''



# 非递归
# go
'''
func inorderTraversal(root *TreeNode) (res []int) {
	stack := []*TreeNode{}
	for root != nil || len(stack) > 0 {
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}
		root = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		res = append(res, root.Val)
		root = root.Right
	}
	return
}
'''
# java
'''
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        Deque<TreeNode> stk = new LinkedList<TreeNode>();
        while (root != null || !stk.isEmpty()) {
            while (root != null) {
                stk.push(root);
                root = root.left;
            }
            root = stk.pop();
            res.add(root.val);
            root = root.right;
        }
        return res;
    }
}
'''


# go
'''
解法一、递归法
解题思路
1、先将当前节点加入结果
2、中序遍历左节点
3、中序遍历右节点
4、返回结果
代码

func inorderTraversal(root *TreeNode) []int {
	var result []int

	var inOrder func(root *TreeNode) []int
	inOrder = func(root *TreeNode) []int {
		if root == nil {
			return result
		}
		inOrder(root.Left)
		result = append(result, root.Val)
		inOrder(root.Right)
		return result
	}

	inOrder(root)
	return result
}
或者把inOrder方法独立出来写


func inorderTraversal(root *TreeNode) []int {
	var result []int
	inOrder(root, &result)
	return result
}

func inOrder(root *TreeNode, result *[]int) {
	if root == nil {
		return
	}
	inOrder(root.Left, result)
	*result = append(*result, root.Val)
	inOrder(root.Right, result)
}
解法二、迭代法
解法
参考官方的迭代法

1、方法一的递归函数，在进行递归的时候，隐式地维护了一个栈
2、我们在迭代的时候需要显式地将这个栈模拟出来
3、每到一个节点root，先将其入栈。然后遍历左子树，接着访问root，最后遍历右子树
4、访问完root后，其就可以出栈了。因为root和其左子树都已经访问完成
代码

func inorderTraversal(root *TreeNode) []int {
	var stack []*TreeNode
	var result []int

	for root != nil || len(stack) != 0 {
		// 遍历左节点
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}
		// 拿到当前节点
		root = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		result = append(result, root.Val)
		// 遍历右节点
		root = root.Right
	}
	return result
}
解法三、颜色标记法
解题思路
参考hzhu212大佬的解法：

1、使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色。
2、如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子节点依次入栈。
为什么入栈顺序是右 -> 自身 -> 左？

因为出栈的时候就会变成左 -> 自身 -> 右，符合中序遍历顺序。

3、如果遇到的节点为灰色，则将节点的值输出。
代码

type colorNode struct {
	Color int
	Node  *TreeNode
}

func inorderTraversal(root *TreeNode) []int {
	if root == nil {
		return nil
	}
	white, gray := 0, 1
	var result []int
	var stack []*colorNode
	stack = append(stack, &colorNode{Color: white, Node: root})
	for len(stack) != 0 {
		top := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if top.Node == nil {
			continue
		}
		if top.Color == gray {
			result = append(result, top.Node.Val)
			continue
		}
		stack = append(stack, &colorNode{Color: white, Node: top.Node.Right})
		stack = append(stack, &colorNode{Color: gray, Node: top.Node})
		stack = append(stack, &colorNode{Color: white, Node: top.Node.Left})
	}
	return result
}
又或者，按照该题解的评论区思路，white对应TreeNode数据类型，gray对应int数据类型


func inorderTraversal(root *TreeNode) []int {
	var result []int
	var stack []interface{}
	stack = append(stack, root)
	for len(stack) != 0 {
		top := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		switch top.(type) {
		case int:
			result = append(result, top.(int))
		case *TreeNode:
		    // 防止遇到空指针
			if value, ok := top.(*TreeNode); ok && value != nil {
				stack = append(stack, value.Right)
				stack = append(stack, value.Val)
				stack = append(stack, value.Left)
			}

		}
	}
	return result
}
'''