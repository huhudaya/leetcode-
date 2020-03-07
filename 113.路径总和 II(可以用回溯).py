'''
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''


# 递归
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
    res = []
    if not root:
        return []

    def helper(root, sum, tmp):
        if not root:
            return
        if not root.left and not root.right and sum - root.val == 0:
            # 每次都新new一个列表是不是不好啊
            tmp += [root.val]
            res.append(tmp)
            return
        helper(root.left, sum - root.val, tmp + [root.val])
        helper(root.right, sum - root.val, tmp + [root.val])

    helper(root, sum, [])
    return res


# 非递归
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        stack = [([root.val], root)]
        res = []
        while stack:
            tmp, node = stack.pop()
            if not node.right and not node.left and sum(tmp) == sum:
                res.append(tmp)
            if node.right:
                stack.append((tmp + [node.right.val], node.right))
            if node.left:
                stack.append((tmp + [node.left.val], node.left))
        return res


# 回溯
'''
// 二叉树路径之和
/**
	给定一个二叉树，找出所有路径中各节点相加总和等于给定 目标值 的路径。

	一个有效的路径，指的是从根节点到叶节点的路径。
	
	Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.

	A valid path is from root node to any of the leaf nodes.
样例1:
输入:
{1,2,4,2,3}
5
输出: [[1, 2, 2],[1, 4]]
说明:
这棵树如下图所示：
	     1
	    / \
	   2   4
	  / \
	 2   3
对于目标总和为5，很显然1 + 2 + 2 = 1 + 4 = 5

样例2:
输入:
{1,2,4,2,3}
3
输出: []
说明:
这棵树如下图所示：
	     1
	    / \
	   2   4
	  / \
	 2   3
注意到题目要求我们寻找从根节点到叶子节点的路径。
1 + 2 + 2 = 5, 1 + 2 + 3 = 6, 1 + 4 = 5 
这里没有合法的路径满足和等于3.
*/
package Test;

import javax.swing.tree.TreeNode;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;

//traverse
public class BinaryTreePathSum {
    public List<List<Integer>> binaryTreePathSum(TreeNode root, int target) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (root == null) {
            return result;
        }
        ArrayList<Integer> paths = new ArrayList<Integer>();
        //此时paths中一定有一个根节点的值
        paths.add(root.val);
        help(root,paths,root.val,target,result);
        return result;
    }
    public void help(TreeNode root,ArrayList<Integer> path,int sum,int target,List<List<Integer>> result){
        // meet leaf 是叶子节点就停止
        if(root.left == null && root.right == null){
            if(sum == target){
        // 要用新的容器，因为path会变
                result.add(new ArrayList<Integer>(path));
            }
            return;
        }
        // go left
        if (root.left != null){
            //相当于先遍历，即自上而下的 traverse+divide&conquer
            path.add(root.left.val);
            help(root.left,path,sum+root.left.val,target,result);
            path.remove(path.size()-1);
        }
        // go right
        if (root.right != null){
            path.add(root.right.val);
            help(root.right,path,sum+root.right.val,target,result);
            path.remove(path.size()-1);
        }
    }
}
'''


# 自己的版本1
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        # traverse方法
        if root is None:
            return []
        res = []

        def helper(root, sum, tmp):
            if root is None:
                return
            sum -= root.val
            if root.left is None and root.right is None:
                if sum == 0:
                    tmp += [root.val]
                    res.append(tmp)
                return
            helper(root.left, sum, tmp + [root.val])
            helper(root.right, sum, tmp + [root.val])

        helper(root, sum, [])
        return res


# 自己的版本2
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        # traverse方法
        if root is None:
            return []
        res = []

        def helper(root, sum, tmp):
            if root is None:
                return
            sum -= root.val
            if root.left is None and root.right is None:
                if sum == 0:
                    res.append(tmp)
                return
            if root.left:
                helper(root.left, sum, tmp + [root.left.val])
            if root.right:
                helper(root.right, sum, tmp + [root.right.val])

        helper(root, sum, [root.val])
        return res


# 自己的版本3
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        # traverse方法
        if root is None:
            return []
        res = []

        def helper(root, sum, tmp):
            if root is None:
                return
            sum -= root.val
            if root.left is None and root.right is None:
                if sum == 0:
                    tmp += [root.val]
                    res.append(tmp)
                return
            if root.left:
                helper(root.left, sum, tmp + [root.val])
            if root.right:
                helper(root.right, sum, tmp + [root.val])

        helper(root, sum, [])
        return res


# 自己的版本回溯法，节省内存
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.res = []
        self.find_binary_tree_path_sum(root, [], sum, 0)
        return self.res

    def find_binary_tree_path_sum(self, root, tmp_res, target, cur_sum):
        # 这种方法其实不是很好，因为到了空节点才判断，所以这个时候就算了两遍相同的路径
        if root is None:
            # if not root:
            return
        # traverse 路径选择
        tmp_res.append(root.val)
        # 注意这里相当于回溯
        cur_sum += root.val
        if root.left == None and root.right == None:
            if target == cur_sum:
                self.res.append(tmp_res[:])
                # 下面这两行可以加也可以不加，最好加上，提前停止递归
                # tmp_res.pop()
                # return
        # divide&conquer
        self.find_binary_tree_path_sum(root.left, tmp_res, target, cur_sum)
        self.find_binary_tree_path_sum(root.right, tmp_res, target, cur_sum)
        # 这句话加不加其实都可以，因为上面cur_sum其实每次都是一个新的字符串！
        # cur_sum -= root.val
        tmp_res.pop()
