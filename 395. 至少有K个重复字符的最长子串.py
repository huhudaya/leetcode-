# 395. 至少有K个重复字符的最长子串.py
'''
找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。

示例 1:

输入:
s = "aaabb", k = 3

输出:
3

最长子串为 "aaa" ，其中 'a' 重复了 3 次。
示例 2:

输入:
s = "ababbc", k = 2

输出:
5

最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。

链接：https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters
'''


# 暴力法 利用前缀和
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        from collections import Counter
        c = Counter()
        n = len(s)
        prefix = [c.copy()]
        for i in range(n):
            c[s[i]] += 1
            prefix.append(c.copy())

        def check(tmp):
            for val in tmp.values():
                if val < k:
                    return False
            return True

        res = 0
        for i in range(n + 1):
            for j in range(i):
                if check(prefix[i] - prefix[j]):
                    res = max(res, i - j)
                    break
        return res


print(Solution.longestSubstring())
