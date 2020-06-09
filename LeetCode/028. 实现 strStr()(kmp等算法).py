# 028. 实现 strStr().py
'''
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

链接：https://leetcode-cn.com/problems/implement-strstr
'''


# 使用库函数
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


# 暴力算法
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 子串是needle,主串是haystack
        n = len(haystack)
        m = len(needle)
        if needle == "":
            return 0
        for i in range(0, n - m + 1):
            index = i
            for j in range(m):
                if haystack[index] == needle[j]:
                    index += 1
                else:
                    break
            if j == m - 1:
                return i
        return -1


# 简练的方法
class Solution:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


from collections import Counter

a = ["a", "asdf", "asfaf"]
print(Counter(a))
