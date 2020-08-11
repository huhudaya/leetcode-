'''

在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:

输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return 0, 0
            # 左子树偷&不偷的结果
            left = helper(node.left)
            # 右子树偷&不偷的结果
            right = helper(node.right)
            # 偷当前节点，左右子树不能偷
            robbed = node.val + left[1] + right[1]
            # 不偷当前节点，左右子树,可偷，可不偷，选大的
            notrob = max(left) + max(right)
            return robbed, notrob
        return max(helper(root))

# java
'''
public class Solution {

    // 树的后序遍历

    public int rob(TreeNode root) {
        int[] res = dfs(root);
        return Math.max(res[0], res[1]);
    }

    private int[] dfs(TreeNode node) {
        if (node == null) {
            return new int[]{0, 0};
        }

        // 分类讨论的标准是：当前结点偷或者不偷
        // 由于需要后序遍历，所以先计算左右子结点，然后计算当前结点的状态值
        int[] left = dfs(node.left);
        int[] right = dfs(node.right);

        // dp[0]：以当前 node 为根结点的子树能够偷取的最大价值，规定 node 结点不偷
        // dp[1]：以当前 node 为根结点的子树能够偷取的最大价值，规定 node 结点偷
        int[] dp = new int[2];

        dp[0] = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        dp[1] = node.val + left[0] + right[0];
        return dp;
    }
}
'''
# 需要记忆化递归，否则超时
class Solution:
    def rob(self, root: TreeNode) -> int:
        self.res = 0
        # dfs定义为以root为根的最大价值
        memo = {}
        def dfs(root):
            if root is None:
                return 0
            if root in memo:
                return memo[root]
            left = dfs(root.left)
            right = dfs(root.right)
            res1 = 0
            res2 = 0
            left_1 = left_2 = 0
            right_1 = right_2 = 0
            if root.left:
                left_1 = dfs(root.left.left)
                right_1 = dfs(root.left.right)
                res1 = left_1 + right_1
            if root.right:
                left_2 = dfs(root.right.left)
                right_2 = dfs(root.right.right)
                res2 = left_2 + right_2
            self.res = max(res1 + res2 + root.val, left + right)
            memo[root] = self.res
            return self.res
        dfs(root)
        return self.res