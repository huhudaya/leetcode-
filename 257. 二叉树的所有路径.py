# 257. 二叉树的所有路径.py
'''
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

链接：https://leetcode-cn.com/problems/binary-tree-paths
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


# 这里Python用的其实就是回溯法，注意这里的添加选择和撤销选择两部分，为什么Java不用选择和撤销呢？这是因为在Java程序中每次都传了一个新的str
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # # 直接dfs
        # # divide&conquer 实际上就是后序遍历
        # if root is None:
        #     return []
        # if root.left is None and root.right is None:
        #     return [str(root.val)]
        # paths = []
        # for path in self.binaryTreePaths(root.left):
        #     paths.append(str(root.val) + "->" + path)
        # for path in self.binaryTreePaths(root.right):
        #     paths.append(str(root.val) + "->" + path)
        # return paths

        # traverse 实际上就是前序遍历
        if root is None:
            return []
        result = []

        def helper(root, path, result):
            if root.left is None and root.right is None:
                result.append("->".join(path))
                return
                # 前序遍历 + 后序遍历 类似于回溯法中的决策树，下面这两个就相当于多叉树的标准的回溯模板
            if root.left:
                # 选择
                path.append(str(root.left.val))
                helper(root.left, path, result)
                # 撤销选择
                path.pop()
            if root.right:
                path.append(str(root.right.val))
                helper(root.right, path, result)
                path.pop()

        helper(root, [str(root.val)], result)
        return result


# java
'''
public class Solution {
    /**
     * @param root the root of the binary tree
     * @return all root-to-leaf paths
     */
    public List<String> binaryTreePaths(TreeNode root) {
    	// 定义一个局部变量paths用来存放返回的结果值。这里需要注意，一般分治法会定义一个局部变量，而遍历法会定义一个全局变量作为变化的值，return一般不返回
        List<String> paths = new ArrayList<>();
        if (root == null) {
            return paths;
        }
        List<String> leftPaths = binaryTreePaths(root.left);
        List<String> rightPaths = binaryTreePaths(root.right);
        // 相当于merge&sort的思想，先divide，然后conquer，这里不要考虑太多，从整体出发，相当于先划分为两半，先得到左边的路径，然后得到右边的路径，然后考虑怎么将两则和根节点串连起来。大象装冰箱问题，需要几步？需要三步:1,打开冰箱。2,放进去大象。3,关山冰箱门。
        // 千万不要纠结细节
        for (String path : leftPaths) {
            paths.add(root.val + "->" + path);
        }
        for (String path : rightPaths) {
            paths.add(root.val + "->" + path);
        }
        // root is a leaf 说明是叶子节点
        if (paths.size() == 0) {
            paths.add("" + root.val);
        }  
        return paths;
    }
}
'''
