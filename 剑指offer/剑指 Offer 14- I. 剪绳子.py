'''
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
提示：

2 <= n <= 58
注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。
'''


# 暴力递归
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        res = 0
        for i in range(1, n):
            res = max(res, max(i * self.integerBreak(n - i), i * (n - i)))
        return res


# 备忘录优化
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        res = 0
        for i in range(1, n):
            res = max(res, max(i * self.integerBreak(n - i), i * (n - i)))
        return res


# 动态规划
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 1)
        # dp[i] 定义为数字i的子序列分解得到的最大值
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(j * dp[i - j], j * (i - j), dp[i])
        return dp[n]


# 完全背包问题
import sys
class Solution:
    def integerBreak(self, n: int) -> int:
        # 完全背包的的恰好装满的最值问题
        dp = [-sys.maxsize for i in range(n + 1)]
        # basecase 可以将二维dp压缩到一维，然后看最后一行的初始值即为一维dp的base case
        dp[0] = 0
        # 完全背包，所以正序遍历
        for i in range(1, n):
            for j in range(i, n + 1):
                dp[j] = max(dp[j], dp[j - i] * i, (j - i) * i)
        return dp[n]
