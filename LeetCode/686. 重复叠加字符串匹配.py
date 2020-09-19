'''
给定两个字符串 A 和 B, 寻找重复叠加字符串A的最小次数
使得字符串B成为叠加后的字符串A的子串，如果不存在则返回 -1

举个例子，A = "abcd"，B = "cdabcdab"
答案为 3， 因为 A 重复叠加三遍后为 “abcdabcdabcd”，此时 B 是其子串
A 重复叠加两遍后为"abcdabcd"，B 并不是其子串

注意:
 A 与 B 字符串的长度在1和10000区间范围内。
'''

'''
不断叠加A，看B是否是子串
当叠加长度大于A和B相加的长度，说明B不是子串
注意:
A 与 B 字符串的长度在1和10000区间范围内。

满足条件的A的长度范围为[B, A+B]，原因是最糟糕的情况下，A的末尾字符刚好匹配上B的头部，这时可能需要A+B才能完成匹配，否则叠加再多的A也无法匹配。
'''
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        tmp = A
        for i in range(1, 10001):
            if B in tmp:
                return i
            if len(B) + len(A) < len(tmp):
                return -1
            tmp = tmp + A
