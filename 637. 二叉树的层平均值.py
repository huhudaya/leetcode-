# 637. 二叉树的层平均值.py
'''
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.

示例 1:

输入:
    3
   / \
  9  20
    /  \
   15   7
输出: [3, 14.5, 11]
解释:
第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].

链接：https://leetcode-cn.com/problems/average-of-levels-in-binary-tree
'''
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Solution:
    def averageOfLevels(self, root: TreeNode):
        # 双端队列
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
            res.append(sum(level) / len(level))
        return res


# 深度优先搜索
'''
方法一：深度优先搜索
我们可以使用深度优先搜索遍历整颗二叉树。
我们使用两个数组 sum 存放树中每一层的节点数值之和
以及 count 存放树中每一层的节点数量之和。
在遍历时，我们需要额外记录当前节点所在的高度
并根据高度 h 更新数组元素 sum[h] 和 count[h]。
在遍历结束之后，res = sum / cnt 即为答案。

时间复杂度：O(N)，其中 N 是树中的节点个数。
空间复杂度：O(H)，其中 H 是树的高度，即为深度优先搜索中使用递归占用的栈空间。
'''
# Java
'''
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List < Double > averageOfLevels(TreeNode root) {
        List < Integer > count = new ArrayList < > ();
        List < Double > res = new ArrayList < > ();
        average(root, 0, res, count);
        for (int i = 0; i < res.size(); i++)
            res.set(i, res.get(i) / count.get(i));
        return res;
    }
    public void average(TreeNode t, int i, List < Double > sum, List < Integer > count) {
        if (t == null)
            return;
        if (i < sum.size()) {
            sum.set(i, sum.get(i) + t.val);
            count.set(i, count.get(i) + 1);
        } else {
            sum.add(1.0 * t.val);
            count.add(1);
        }
        average(t.left, i + 1, sum, count);
        average(t.right, i + 1, sum, count);
    }
}
'''
# dfs
class Solution:
    def averageOfLevels(self, root: TreeNode):
        res = []
        _sum = []

        def helper(root, depth):
            if not root:
                return
            if depth < len(res):
                res[depth] += 1
                _sum[depth] += 1
            else:
                res[depth].append(root.val * 1)
                _sum[depth].append(1)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)

        helper(root, 0)
