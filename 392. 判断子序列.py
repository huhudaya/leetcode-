# 392. 判断子序列.py
'''
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1:
s = "abc", t = "ahbgdc"

返回 true.

示例 2:
s = "axc", t = "ahbgdc"

返回 false.

后续挑战 :

如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

'''
# import bisect
# # class Solution:
#     # # 暴力法
#     # def isSubsequence(self, s: str, t: str) -> bool:
#     #     i,j = 0,0
#     #     while i < len(s) and j < len(t):
#     #         if s[i] == t[j]:
#     #             i += 1
#     #         j += 1
#     #     return i == len(s)
#     # 二分法解决子序列问题
#     # def isSubsequence(self, s: str, t: str) -> bool:
#     #     # ord("a") = 97
#     #     hash = [[] for i in range(26)]
#     #     # 构建hash数组
#     #     for i in range(len(t)):
#     #         hash[ord(t[i])-97].append(i)
#     #     # 定义 j 为当前索引
#     #     j = 0        
#     #     for i in range(len(s)):
#     #         index = ord(s[i])-97
#     #         if len(hash[index]) == 0:
#     #             return False
#     #         pos = bisect.bisect_left(hash[index],j)
#     #         if pos == len(hash[index]):
#     #             return False
#     #         j = hash[index][pos] + 1
#     #     return True
class Solution(object):
    def isSubsequence(self,s, t):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        t = iter(t)
        return all(i in t for i in s)