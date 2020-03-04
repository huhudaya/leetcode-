# 647. 回文子串的个数(中心扩散).py
'''
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".

链接：https://leetcode-cn.com/problems/palindromic-substrings
'''


class Solution:
    # 中心扩散法
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        self.res = 0

        def helper(left, right):
            while left >= 0 and right < length and s[left] == s[right]:
                # 中心扩散
                left -= 1
                right += 1
                self.res += 1

        for i in range(length):
            helper(i, i)
            helper(i, i + 1)
        return self.res
