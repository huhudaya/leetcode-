'''
给定一棵二叉树，你需要计算它的直径长度。
一棵二叉树的直径长度是任意两个结点路径长度中的最大值。
这条路径可能穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

注意：两结点之间的路径长度是以它们之间边的数目表示。

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1

        # depth函数返回以root为根节点的最大长度
        def depth(root):
            if not root:
                return 0
            # divide&conquer
            L = depth(root.left)
            R = depth(root.right)
            self.ans = max(self.ans, L + R + 1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1


# java
'''
class Solution {
    int ans;
    public int diameterOfBinaryTree(TreeNode root) {
        ans = 1;
        depth(root);
        return ans - 1;
    }
    public int depth(TreeNode node) {
        if (node == null) return 0; // 访问到空节点了，返回0
        int L = depth(node.left); // 左儿子为根的子树的深度
        int R = depth(node.right); // 右儿子为根的子树的深度
        ans = Math.max(ans, L+R+1); // 计算d_node即L+R+1 并更新ans
        return Math.max(L, R) + 1; // 返回该节点为根的子树的深度
    }
}
'''

'''
遍历每一个节点，以每一个节点为中心点计算最长路径（左子树边长+右子树边长），更新全局变量max。

class Solution {
    int max = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        if (root == null) {
            return 0;
        }
        dfs(root);
        return max;
    }
    
    private int dfs(TreeNode root) {
        if (root.left == null && root.right == null) {
            return 0;
        }
        int leftSize = root.left == null? 0: dfs(root.left) + 1;
        int rightSize = root.right == null? 0: dfs(root.right) + 1;
        max = Math.max(max, leftSize + rightSize);
        return Math.max(leftSize, rightSize);
    }  
}
>>>>>>>>>>更新：雷同题目相同解法>>>>>>>>>>>>>

刚刚做了一道类似的题124. 二叉树中的最大路径和，虽然是Hard但解法和本题一毛一样～～
唯一的区别是：不是求边长，而是路径上节点的value之和，因为节点的value可能是负数，因此求左孩子右孩子的时候要int leftSum = Math.max(0, dfs(root.left));舍弃掉负数的结果。

class Solution {
    int max = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        dfs(root);
        return max;
    }

    private int dfs(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int leftSum = Math.max(0, dfs(root.left)); // 和上题唯一的区别在这里，如果左右孩子的结果是负数的话就舍弃。
        int rightSum = Math.max(0, dfs(root.right));
        max = Math.max(max, leftSum + rightSum + root.val);
        return Math.max(leftSum, rightSum) + root.val;
    }
} 
>>>>>>>>>>再更新：哎码又碰到了一样的题>>>>>>>>>>>>>

687. 最长同值路径和本题又一毛一样，遍历所有节点，以每个节点为中心点求最长路径（左右子树的边长之和），更新全局max。唯一的区别是，求出了左孩子的边长leftSize后，如果左孩子和当前节点不同值的话，那要把leftSize重新赋值成0。

class Solution {
    int max = 0;
    public int longestUnivaluePath(TreeNode root) {
        if (root == null) {
            return 0;
        }
        dfs(root);
        return max;
    }

    private int dfs(TreeNode root) {
        if (root.left == null && root.right == null) {
            return 0;
        }

        int leftSize = root.left != null? dfs(root.left) + 1: 0;
        int rightSize = root.right != null? dfs(root.right) + 1: 0;
        if (leftSize > 0 && root.left.val != root.val) {
            // 唯一的区别在这里，按照上题思路求出了左边边长后， 如果当前节点和左孩子节点不同值，就把边长重新赋值为0。
            leftSize = 0;
        }
        if (rightSize > 0 && root.right.val != root.val) {
            // 同上。
            rightSize = 0;
        }
        max = Math.max(max, leftSize + rightSize);
        return Math.max(leftSize, rightSize);
    }
}
'''
