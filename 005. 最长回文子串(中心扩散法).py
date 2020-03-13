# 005. 最长回文子串.py
'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

链接：https://leetcode-cn.com/problems/longest-palindromic-substring
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 中心扩散法
        length = len(s)
        self.res = ""

        def help(left, right):
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(length):
            s1 = help(i, i)
            s2 = help(i, i + 1)
            self.res = s1 if len(self.res) < len(s1) else self.res
            self.res = s2 if len(self.res) < len(s2) else self.res
            #self.res = max(s1, s2)
        return self.res
