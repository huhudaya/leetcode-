'''
给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。

示例 1：

输入: s1 = "abc", s2 = "bca"
输出: true
示例 2：

输入: s1 = "abc", s2 = "bad"
输出: false
说明：

0 <= len(s1) <= 100
0 <= len(s2) <= 100
'''


# set
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        return m == n and set(s1) == set(s2)


# 位运算
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        length_1 = len(s1)
        if length_1 != len(s2):
            return False

        result = 0
        for i in range(length_1):
            result += 1 << ord(s1[i])
            result -= 1 << ord(s2[i])

        return result == 0
