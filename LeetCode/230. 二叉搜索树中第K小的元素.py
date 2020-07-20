'''

给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3
进阶：
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？
'''
# 中序遍历
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return inorder(root)[k - 1]

# 中序迭代
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
# 分治
'''

如果不知道解法一中二叉搜索树的性质，用分治法也可以做，分享 这里 的解法。

我们只需要先计算左子树的节点个数，记为 n，然后有三种情况。

n 加 1 等于 k，那就说明当前根节点就是我们要找的。

n 加 1 小于 k，那就说明第 k 小的数一定在右子树中，我们只需要递归的在右子树中寻找第 k - n - 1 小的数即可。

n 加 1 大于 k，那就说明第 k 小个数一定在左子树中，我们只需要递归的在左子树中寻找第 k 小的数即可。
'''
'''
public int kthSmallest(TreeNode root, int k) {
    int n = nodeCount(root.left);  
    if(n + 1 == k) {
        return root.val;
    } else if (n + 1 < k) {
        return kthSmallest(root.right, k - n - 1);
    } else {
        return kthSmallest(root.left, k);
    }
}

private int nodeCount(TreeNode root) {
    if(root == null) {
        return 0;
    }
    return 1 + nodeCount(root.left) + nodeCount(root.right);
}

'''
# 剪枝
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 中序遍历迭代剪枝
        res = []
        cnt = k
        while root or res:
            if root:
                res.append(root)
                root = root.left
            else:
                tmp = res.pop()
                root = tmp.right
                cnt -= 1
                if cnt == 0:
                    return tmp.val
        return 0