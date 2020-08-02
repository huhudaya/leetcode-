'''
给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

注意：两个节点之间的路径长度由它们之间的边数表示。

示例 1:

输入:

              5
             / \
            4   5
           / \   \
          1   1   5
输出:

2
示例 2:

输入:

              1
             / \
            4   5
           / \   \
          4   4   5
输出:

2
注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。
'''

# java
'''
class Solution {
    int ans;
    public int longestUnivaluePath(TreeNode root) {
        ans = 0;
        arrowLength(root);
        return ans;
    }
    public int arrowLength(TreeNode node) {
        if (node == null) return 0;
        int left = arrowLength(node.left);
        int right = arrowLength(node.right);
        int arrowLeft = 0, arrowRight = 0;
        if (node.left != null && node.left.val == node.val) {
            arrowLeft += left + 1;
        }
        if (node.right != null && node.right.val == node.val) {
            arrowRight += right + 1;
        }
        ans = Math.max(ans, arrowLeft + arrowRight);
        return Math.max(arrowLeft, arrowRight);
    }
}
'''

'''
我们可以将任何路径（具有相同值的节点）看作是最多两个从其根延伸出的箭头。
具体地说，路径的根将是唯一节点，因此该节点的父节点不会出现在该路径中，而箭头将是根在该路径中只有一个子节点的路径。
然后，对于每个节点，我们想知道向左延伸的最长箭头和向右延伸的最长箭头是什么？我们可以用递归来解决这个问题。
算法
令 arrow_length(node) 为从节点 node 延伸出的最长箭头的长度。
    如果 node.Left 存在且与节点 node 具有相同的值，则该值就会是 1 + arrow_length(node.left)。
    在 node.right 存在的情况下也是一样。
当我们计算箭头长度时，候选答案将是该节点在两个方向上的箭头之和。
我们将这些候选答案记录下来，并返回最佳答案。
'''

'''
这题中，当前节点返回给父节点的值就是： 从当前节点出发，向下延伸与其值相同的最大深度 于是返回值分两种情况：
1.if( 如果当前节点与其左右节点都不相等)，那么深度为0，则返回0 2. else，这个最大深度就取其 左右子树返回值中的较大者 + 1

然后，在上面这个dfs的遍历过程中，还可以做一些其他的事情，这题做的就是 计算路径长度。由于子树的返回值已经确定了，所以需要额外的一个全局变量。
如何计算路径长度呢？其实知道了和自己数值相等的左右子树的最大高度了，那么 把左右子树返回的值相加 就是贯穿自己的最长路径了
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# divide&conquer的方式
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0
        # 返回以root为根节点的最大连续长度
        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            left_new = 0
            right_new = 0
            # 如果左节点和根相同，就更新长度
            if root.left and root.val == root.left.val:
                left_new = left + 1
            # 如果右节点和根相同，就更新长度
            if root.right and root.val == root.right.val:
                right_new = right + 1
            self.res = max(self.res, left_new + right_new)
            return max(left_new, right_new)
        dfs(root)
        return self.res


# traverse的方式计算任意以root为根的最大长度，注意，不能出现拐点
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0
        # traverse
        if root is None:
            return None
        def traverse(root, cur_len):
            self.res = max(self.res, cur_len)
            if root.left:
                if root.left.val == root.val:
                    traverse(root.left, cur_len + 1)
                else:
                    traverse(root.left, 0)
            if root.right:
                if root.right.val == root.val:
                    traverse(root.right, cur_len + 1)
                else:
                    traverse(root.right, 0)
        traverse(root, 0)
        return self.res
