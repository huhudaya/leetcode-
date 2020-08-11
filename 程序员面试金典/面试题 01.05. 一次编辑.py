'''

字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。
给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

示例 1:
输入:
first = "pale"
second = "ple"
输出: True


示例 2:
输入:
first = "pales"
second = "pal"
'''


# 一边遍历
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        m = len(first)
        n = len(second)
        if abs(m - n) > 1:
            return False
        # first是长度小的字符串
        if m > n:
            first, second = second, first
            m, n = n, m
        for i in range(m):
            if first[i] == second[i]:
                continue
            # 对应增和换
            return first[i:] == second[i + 1:] or first[i + 1:] == second[i + 1:]
        return True



# 编辑距离
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        m, n = len(first), len(second)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if first[i - 1] == second[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        return True if dp[m][n] == 0 or dp[m][n] == 1 else False
