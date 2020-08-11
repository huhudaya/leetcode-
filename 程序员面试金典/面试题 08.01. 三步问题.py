'''
三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

示例1:

 输入：n = 3
 输出：4
 说明: 有四种走法
示例2:

 输入：n = 5
 输出：13
提示:

n范围在[1, 1000000]之间
'''


# 备忘录递归
class Solution:
    def waysToStep(self, n: int) -> int:
        memo = {}
        memo[1] = 1
        memo[2] = 3
        memo[3] = 4

        def dfs(n):
            if n in memo:
                return memo[n]
            res = dfs(n - 1) + dfs(n - 2) + dfs(n - 3)
            memo[n] = res
            return res

        return dfs(n)


class Solution:
    def waysToStep(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000007
        return dp[n]
