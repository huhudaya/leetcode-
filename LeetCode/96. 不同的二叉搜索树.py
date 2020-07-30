'''
96. 不同的二叉搜索树
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
通过次数73,578提交次数106,495
'''


# 动态规划
'''
动态规划

假设n个节点存在二叉排序树的个数是G(n)，令f(i)为以i为根的二叉搜索树的个数

即有:G(n) = f(1) + f(2) + f(3) + f(4) + ... + f(n)

n为根节点，当i为根节点时，其左子树节点个数为[1,2,3,...,i-1]，右子树节点个数为[i+1,i+2,...n]，所以当i为根节点时，其左子树节点个数为i-1个，右子树节点为n-i，即f(i) = G(i-1)*G(n-i),

上面两式可得:G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)
'''

# 动态规划
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        # dp[i]为以 i 为根的二叉搜索树的个数
        for i in range(2, n + 1):
            # j 表示以 j 进行分割形成左右子树的个数，dp[i]为这些树加起来
            for j in range(1, i + 1):
                # 笛卡尔乘积
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]


# 递归
class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        res = 0
        for i in range(1, n + 1):
            res += self.numTrees(i - 1) * self.numTrees(n - i)
        return res


# 备忘录
class Solution:
    visited = dict()

    def numTrees(self, n: int) -> int:
        if n in self.visited:
            return self.visited.get(n)
        if n <= 1:
            return 1
        res = 0
        for i in range(1, n + 1):
            res += self.numTrees(i - 1) * self.numTrees(n - i)
        self.visited[n] = res
        return res


# 自己的版本
class Solution:
    def numTrees(self, n: int) -> int:
        # 动态规划
        # dp[i] 表示为有i个元素组成的二叉搜索树的个数
        dp = [0] * (n + 1)
        # base case
        dp[0] = 1
        for i in range(1, n + 1):
            # 按 j 分割
            for j in range(1, i + 1):
                # 这里是笛卡尔乘积
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]


# 使用lru_cache
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def numTrees(self, n: int) -> int:
        # 递归
        if n <= 1:
            return 1
        res = 0
        for i in range(1, n + 1):
            res += self.numTrees(i - 1) * self.numTrees(n - i)
        return res

# 备忘录优化
class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        def dp(n):
            # 备忘录优化
            res = 0
            if n <= 1:
                return 1
            if n in memo:
                return memo[n]
            # dp[i] 表示为有i个元素组成的二叉搜索树的个数
            for i in range(1, n + 1):
                res += dp(i - 1) * dp(n - i)
            # 计算结果添加到memo中
            memo[n] = res
            return res
        return dp(n)