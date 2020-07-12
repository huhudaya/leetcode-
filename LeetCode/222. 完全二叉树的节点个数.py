'''
给出一个完全二叉树，求出该树的节点个数。

说明：

完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

示例:

输入:
    1
   / \
  2   3
 / \  /
4  5 6

输出: 6
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return left + right + 1


# 中序遍历
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        cnt = 0
        res = []
        while root or res:
            if root:
                res.append(root)
                root = root.left
            else:
                cnt += 1
                tmp = res.pop()
                root = tmp.right
        return cnt


# 前序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # 前序遍历
        cnt = 0
        res = []
        if not root:
            return 0
        res.append(root)
        while res:
            tmp = res.pop()
            cnt += 1
            if tmp.left:
                res.append(tmp.left)
            if tmp.right:
                res.append(tmp.right)
        return cnt


# O(log(n)^2)
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
class Solution {
    public int countNodes(TreeNode root) {
        if(root == null){
           return 0;
        } 
        int left = countLevel(root.left);
        int right = countLevel(root.right);
        if(left == right){
            return countNodes(root.right) + (1<<left);
        }else{
            return countNodes(root.left) + (1<<right);
        }
    }
    private int countLevel(TreeNode root){
        int level = 0;
        while(root != null){
            level++;
            root = root.left;
        }
        return level;
    }
}
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 递归
    def countNodes(self, root: TreeNode) -> int:
        # 有两种情况1.right低   2.left于right一样高
        # base case
        if root is None:
            return 0

        def count_level(root):
            cnt = 0
            while root:
                cnt += 1
                root = root.left
            return cnt

        left = count_level(root.left)
        right = count_level(root.right)
        if left == right:
            return self.countNodes(root.right) + 2 ** left
        if left > right:
            return self.countNodes(root.left) + 2 ** right
