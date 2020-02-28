'''
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
例如，从根到叶子节点路径 1->2->3 代表数字 123。
计算从根到叶子节点生成的所有数字之和。
说明: 叶子节点是指没有子节点的节点。
示例 1:
输入: [1,2,3]
    1
   / \
  2   3
输出: 25
解释:
从根到叶子节点路径 1->2 代表数字 12.
从根到叶子节点路径 1->3 代表数字 13.
因此，数字总和 = 12 + 13 = 25.
示例 2:
输入: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
输出: 1026
解释:
从根到叶子节点路径 4->9->5 代表数字 495.
从根到叶子节点路径 4->9->1 代表数字 491.
从根到叶子节点路径 4->0 代表数字 40.
因此，数字总和 = 495 + 491 + 40 = 1026.
'''
'''
class Solution {
    private int ans = 0;
    private int tmp = 0;

    public int sumNumbers(TreeNode root) {
        dfs(root);
        return ans;
    }

    private void dfs(TreeNode node) {
        if (node == null) {
            return;
        }
        tmp = tmp * 10 + node.val;
        if (node.left == null && node.right == null) {
            ans += tmp;
        }
        if (node.left != null) {
            dfs(node.left);
        }
        if (node.right != null) {
            dfs(node.right);
        }
        tmp /= 10;
    }
}
'''
'''
class Solution {
    int result = 0;

    public int sumNumbers(TreeNode root) {
        if(root == null) return 0;
        helper(root, 0);
        return result;
    }

    public void helper(TreeNode root, int sb){
        sb = sb * 10 + root.val;
        if(root.left == null && root.right == null) {//到达叶子结点，把值加给result
            result += sb;
            return;
        }
        int temp = sb;//若左右子树都不为空，需要“一分为二”
        if(root.left != null) helper(root.left, sb);
        if(root.right != null) helper(root.right, temp);
    }
}
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 字符串拼接
def sumNumbers(self, root: TreeNode) -> int:
    self.res = 0

    def helper(root, tmp):
        if not root: return
        if not root.left and not root.right:
            self.res += int(tmp + str(root.val))
            return
        helper(root.left, tmp + str(root.val))
        helper(root.right, tmp + str(root.val))

    helper(root, "")
    return self.res


# 字符串拼接
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = []
        def dfs(root, tmp, res):
            if not root:
                return
            if root.right is None and root.left is None:
                res.append(int(tmp + str(root.val)))
                return
            tmp += str(root.val)
            if root.left:
                dfs(root.left, tmp, res)
            if root.right:
                dfs(root.right, tmp, res)
        dfs(root, "", res)
        return sum(res)


# 数学法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0

        def helper(root, val):
            if root is None:
                return
            tmp = val * 10 + root.val
            if root.left is None and root.right is None:
                self.res += tmp
            if root.left:
                helper(root.left, tmp)
            if root.right:
                helper(root.right, tmp)

        helper(root, 0)
        return self.res
