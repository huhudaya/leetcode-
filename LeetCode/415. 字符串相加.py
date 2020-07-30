'''
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        left = m - 1
        right = n - 1
        ca = 0
        res = ""
        while left >= 0 or right >= 0 or ca:
            if left >= 0:
                ca += int(num1[left])
                left -= 1
            if right >= 0:
                ca += int(num2[right])
                right -= 1
            res = str(ca % 10) + res
            ca = ca // 10
        return res
