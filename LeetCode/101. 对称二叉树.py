'''

给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3


进阶：

你可以运用递归和迭代两种方法解决这个问题吗？
'''

'''
做递归思考三步：

递归的函数要干什么？
函数的作用是判断传入的两个树是否镜像。
输入：TreeNode left, TreeNode right
输出：是：true，不是：false
递归停止的条件是什么？
左节点和右节点都为空 -> 倒底了都长得一样 ->true
左节点为空的时候右节点不为空，或反之 -> 长得不一样-> false
左右节点值不相等 -> 长得不一样 -> false
从某层到下一层的关系是什么？
要想两棵树镜像，那么一棵树左边的左边要和二棵树右边的右边镜像，一棵树左边的右边要和二棵树右边的左边镜像
调用递归函数传入左左和右右
调用递归函数传入左右和右左
只有左左和右右镜像且左右和右左镜像的时候，我们才能说这两棵树是镜像的
调用递归函数，我们想知道它的左右孩子是否镜像，传入的值是root的左孩子和右孩子。这之前记得判个root==null。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 递归
        def check(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return left.val == right.val and check(left.left, right.right) and check(left.right, right.left, )

        return check(root, root)


# 递归Java
'''
class Solution {
    public boolean isSymmetric(TreeNode root) {
        return check(root, root);
    }

    public boolean check(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        }
        if (p == null || q == null) {
            return false;
        }
        return p.val == q.val && check(p.left, q.right) && check(p.right, q.left);
    }
}
'''
# 迭代Java
'''
class Solution {
    public boolean isSymmetric(TreeNode root) {
        return check(root, root);
    }

    public boolean check(TreeNode u, TreeNode v) {
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(u);
        q.offer(v);
        while (!q.isEmpty()) {
            u = q.poll();
            v = q.poll();
            if (u == null && v == null) {
                continue;
            }
            if ((u == null || v == null) || (u.val != v.val)) {
                return false;
            }

            q.offer(u.left);
            q.offer(v.right);

            q.offer(u.right);
            q.offer(v.left);
        }
        return true;
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
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def dfs(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return left.val == right.val and dfs(left.right, right.left) and dfs(left.left, right.right)

        return dfs(root.left, root.right)


# Java
'''
class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (null == root) return true;
        return helper(root.left, root.right);
    }
    private boolean helper(TreeNode left, TreeNode right){
        if (null == left && null == right) return true;
        if (null == left || null == right) return false;
        return left.val == right.val && helper(left.left, right.right) && helper(left.right, right.left);
    }
}
'''
