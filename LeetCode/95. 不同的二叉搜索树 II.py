'''
给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。

 

示例：

输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

提示：

0 <= n <= 8
'''
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 动态规划
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n < 1:
            return []
        ans = []
        dp = [[[None]] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = [TreeNode(i + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                temp = []
                for k in range(i, j + 1):
                    rights = [None] if k == j else dp[k + 1][j]  # 最后一行下方需要一个None
                    for left in dp[i][k - 1]:
                        for right in rights:
                            root = TreeNode(k + 1)
                            root.left = left
                            root.right = right
                            temp.append(root)
                dp[i][j] = temp
        return dp[0][-1]


# 递归
# Definition for a binary tree node.

'''
二叉搜索树有以下几个特点：

左边的小于当前；
右边的大于当前；
没有重复的值。
为了符合二叉搜索树的这几个特点，我们需要知道当前的范围。（要知道开头和结尾；最开始是1和n）

首先定义一个字典保存已遍历的参数和结果以免重复。

特殊情况判断：如果n == 0，返回[]，如果不判断则会返回[None]（执行递归代码会直接返回，因为0<1）。

递归终止条件：

如果left > right则返回[None]。
以前已经遍历过当前节点则可以直接返回以前的结果。
当前的值可能是left……right，所以我们要把每一个都试一遍，每次循环都要这么做：
递归得到左和右，将返回列表增加它们的全部组合。（值：当前循环变量，左：当前左，右：当前右）

将元组(left，right)作为键，返回列表为值加入字典，然后返回。

作者：ting-ting-28
链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii/solution/python3-xiang-xi-di-gui-by-ting-ting-28/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        dct = {}

        def left_right(left: int, right: int) -> List[TreeNode]:
            if left > right:
                return [None]
            if (left, right) in dct:
                return dct[(left, right)]
            ret = []
            # 遍历left到right作为root节点
            for i in range(left, right + 1):
                left_lst = left_right(left, i - 1)
                right_lst = left_right(i + 1, right)
                # 进行笛卡尔乘积的组合
                for L in left_lst:
                    for R in right_lst:
                        app_Tree = TreeNode(i)
                        app_Tree.left = L
                        app_Tree.right = R
                        ret.append(app_Tree)
            dct[(left, right)] = ret
            return ret

        left_right(1, n)
        return left_right(1, n)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
获得所有可行的左子树和可行的右子树
那么最后一步我们只要从可行左子树集合中选一棵
再从可行右子树集合中选一棵拼接到根节点上
并将生成的二叉搜索树放入答案数组即可。
'''
import functools
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        @functools.lru_cache(None)
        def helper(start, end):
            res = []
            if start > end:
                res.append(None)
            # 遍历start到end的集合，将这个集合中的每一个值作为一个root节点
            for val in range(start, end + 1):
                # 左子树
                for left in helper(start, val - 1):
                    for right in helper(val + 1, end):
                        root = TreeNode(val)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res

        return helper(1, n)