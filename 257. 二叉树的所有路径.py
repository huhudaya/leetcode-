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

# 找到二叉树的所有路径
# 注意下面两种pop方法的区别

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


# traverse方法
class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        if root is None:
            return []
        result = []  # 定义一个全局变量result[]
        # 其中的str[root.val]的信息其实在递归过程中会将结果压栈
        self.dfs(root, [str(root.val)], result)
        return result

    # 注意，这里的path其实相当于一个局部变量，在递归过程中会进行压栈处理
    def dfs(self, node, path, result):
        if node.left is None and node.right is None:
            result.append('->'.join(path))
            return
        # traverse,注意traverse是在递归之前的，是自顶向下  下面这两个操作即相当于是回溯,这里就相当于标准的回溯模板了！！！
        if node.left:
            path.append(str(node.left.val))  # path每次都更新，path+left
            self.dfs(node.left, path, result)
            path.pop()  # 这里注意思考为什么需要pop 这是由于path是一个局部变量，在dfs之前将path.append添加了一个left节点，所以当dfs处理完成之后，需要弹出当前元素，继续进行right部分的处理

        if node.right:
            path.append(str(node.right.val))
            self.dfs(node.right, path, result)
            path.pop()


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


# divide&conquer
class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [str(root.val)]
        # 相当于一个局部变量，每次都需要重新new一个
        paths = []
        for path in self.binaryTreePaths(root.left):
            paths.append(str(root.val) + '->' + path)

        for path in self.binaryTreePaths(root.right):
            paths.append(str(root.val) + '->' + path)

        return paths


# 不推荐使用traverse方法实现的DFS
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


# 其实就是后序遍历弹出
class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        if root is None:
            return []

        result = []
        self.dfs(root, [], result)
        return result

    def dfs(self, node, path, result):
        # 在这里一直使用的就是一个path，相当于是一个全局变量!
        # 直接加就好了
        path.append(str(node.val))

        # 这里先判断左右孩子
        if node.left is None and node.right is None:
            result.append('->'.join(path))
            path.pop()
            # 因为这里属于递归结束点，会提前结束，所以需要提前pop(),如果不提前return，就可以不使用pop()
            return  # 这里一定要return哦

        if node.left:
            self.dfs(node.left, path, result)

        if node.right:
            self.dfs(node.right, path, result)
        # 这里需要思考一下为什么需要pop()，这是因为当left和right都执行完之后，一定会弹出当前的值，即出栈!
        path.pop()
