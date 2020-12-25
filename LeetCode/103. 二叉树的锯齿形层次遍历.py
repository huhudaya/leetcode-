# 103. 二叉树的锯齿形层次遍历.py
'''
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 使用递归
from collections import deque
from typing import List


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # dfs
        res = deque()

        def helper(root, depth):
            if not root:
                return
            if len(res) == depth:
                # 使用双端队列
                res.append(deque())
            # 奇偶判断 depth & 1 == 0 为偶数 非0 为奇数
            if depth % 2 == 0:
                res[depth].append(root.val)
            else:
                res[depth].appendleft(root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
        res = list(map(list, res))
        helper(root, 0)
        return res
# 也可以直接按102题的bfs思路来做 不过在最后输出的时候按层数的奇偶性判断一下是否反转


# java
'''
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        travel(root, res, 0);
        return res;
    }

    private void travel(TreeNode cur, List<List<Integer>> res, int level) {
        if (cur == null)
            return;
        //如果res.size() <= level说明下一层的集合还没创建，所以要先创建下一层的集合
        if (res.size() <= level) {
            List<Integer> newLevel = new LinkedList<>();
            res.add(newLevel);
        }
        //遍历到第几层我们就操作第几层的数据
        List<Integer> list = res.get(level);
        //这里默认根节点是第0层，偶数层相当于从左往右遍历，
        // 所以要添加到集合的末尾，如果是奇数层相当于从右往左遍历，
        // 要把数据添加到集合的开头
        if (level % 2 == 0)
            list.add(cur.val);
        else
            list.add(0, cur.val);
        //分别遍历左右两个子节点，到下一层了，所以层数要加1
        travel(cur.left, res, level + 1);
        travel(cur.right, res, level + 1);
    }
'''

# go
'''
func zigzagLevelOrder(root *TreeNode) (ans [][]int) {
    if root == nil {
        return
    }
    queue := []*TreeNode{root}
    for level := 0; len(queue) > 0; level++ {
        vals := []int{}
        q := queue
        queue = nil
        for _, node := range q {
            vals = append(vals, node.Val)
            if node.Left != nil {
                queue = append(queue, node.Left)
            }
            if node.Right != nil {
                queue = append(queue, node.Right)
            }
        }
        // 本质上和层序遍历一样，我们只需要把奇数层的元素翻转即可
        if level%2 == 1 {
            for i, n := 0, len(vals); i < n/2; i++ {
                vals[i], vals[n-1-i] = vals[n-1-i], vals[i]
            }
        }
        ans = append(ans, vals)
    }
    return
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
func zigzagLevelOrder(root *TreeNode) [][]int {
  var ans [][]int
  dfs(root, 0, &ans)
  return ans
}

func dfs(root *TreeNode, depth int, ans *[][]int) {
	if root == nil {
		return
	}
	if depth >= len(*ans) {
		*ans = append(*ans, []int{})
	}
	if depth & 1 == 0 {
		(*ans)[depth] = append((*ans)[depth], root.Val)
	} else {
		// expensive operation
		(*ans)[depth] = append([]int{root.Val}, (*ans)[depth]...)
	}
	dfs(root.Left,  depth + 1, ans)
	dfs(root.Right, depth + 1, ans)
}
'''


#
'''
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func zigzagLevelOrder(root *TreeNode) [][]int {
	var res [][]int
	if root == nil {
		return res
	}
	queue := make([]*TreeNode, 0)
	queue = append(queue, root)l
	isLeftStart := true
	for len(queue) > 0 {
		l := len(queue)
		ans := make([]int, l)
		for i := 0; i < l; i++ {
			node := queue[i]
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
			if isLeftStart {
				ans[i] = node.Val
			} else {
				ans[l-i-1] = node.Val
			}
		}
		res = append(res, ans)
		isLeftStart = !isLeftStart
		queue = queue[l:]
	}
	return res
}
'''

# go双端队列
'''
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func zigzagLevelOrder(root *TreeNode) [][]int {
    var res [][]int
    if root == nil {
        return res
    }

    deque := list.New()
    deque.PushFront(root)
    h := 1

    for deque.Len() > 0 {
        curLen := deque.Len()
        cur := make([]int, curLen)

        for i:=0; i<curLen; i++{
            node := deque.Remove(deque.Back()).(*TreeNode)
            curKey := curLen-i-1
            if h%2 != 0{
                curKey = i
            }

            cur[curKey] = node.Val
            if node.Left != nil {
                deque.PushFront(node.Left)
            }
            if node.Right != nil {
                deque.PushFront(node.Right)
            }
        }
        res = append(res, cur)
        h++
    }

    return res
}
'''