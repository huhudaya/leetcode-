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


# 暴力法 利用前缀和 O(N2) 最后一个测试用例过不去
class Solution:
    def longestSubstring(self, s: str, k: int):
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


# 滑动窗口法
'''
我们可以通过枚举子串的不同字母的个数，来使用滑动窗口
因为字母最多是 26 个，这样复杂度就将到 O(n)。

具体实现

当子串为只有一个 不同 字母的最长子串，比如 s = "aaabbb", k = 3
结果是 3，因为最长的只含有一个字符的串长度为 3，比如 aaa或者bbb，

当子串有不同字符有二个呢，结果是 6了
'''


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        from collections import defaultdict
        if not s: return 0
        # 统计字符串字符的个数
        n = len(s)
        # 统计不同字符的数量
        max_num = len(set(s))

        # 当不同字符个数为num，最长字符为多少
        def cal(num):
            #
            left = 0
            # 目前不同字符的个数
            cur = 0
            # 大于等于k字符的个数
            ge_k = 0
            # 记录字符个数
            c = defaultdict(int)
            # 最长字符串
            res = 0
            for right in range(n):
                c[s[right]] += 1
                # 不同字符个数
                if c[s[right]] == 1:
                    cur += 1
                # 大于等于k个数
                if c[s[right]] == k:
                    ge_k += 1
                # 当字符串不同个数大于 num
                while cur > num:
                    if c[s[left]] == 1:
                        cur -= 1
                    if c[s[left]] == k:
                        ge_k -= 1
                    c[s[left]] -= 1
                    left += 1
                if ge_k == num:
                    res = max(res, right - left + 1)
            return res

        return max(cal(num) for num in range(1, max_num + 1))


# 分治法
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        # 找个字符串个数最少的字符
        t = min(set(s), key=s.count)
        # 最少字符的个数都大于等于k
        if s.count(t) >= k:
            return len(s)
        return max(self.longestSubstring(a, k) for a in s.split(t))


print(Solution().longestSubstring("aaabb", 3))
