# 438. 找到字符串中所有字母异位词.py
'''
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
说明：
字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:
输入:
s: "cbaebabacd" p: "abc"
输出:
[0, 6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。

示例 2:
输入:
s: "abab" p: "ab"
输出:
[0, 1, 2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
'''
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 滑动窗口模板解决此类问题
        # s是原字符串，p是子串
        # ord("a") = 97
        sArr = [ord(i) - 97 for i in s]
        pArr = [ord(i) - 97 for i in p]
        hash = [0 for i in range(26)]
        m, n = len(s), len(p)
        # 构建hash映射数组
        for i in range(n):
            hash[pArr[i]] += 1
        l, r, count, res = 0, 0, 0, []
        while r < m:
            hash[sArr[r]] -= 1
            if hash[sArr[r]] >= 0:
                count += 1
            # 超过固定窗口大小，移动左指针
            if r > n - 1:
                # 移动左指针的时候需要维护好窗口内的数据
                hash[sArr[l]] += 1
                # 前面已经hash[left]+=1了，所以这里只要判断hash[left]是否大于0即可
                if hash[sArr[l]] > 0:
                    count -= 1
                l += 1
            if count == n:
                res.append(l)
            r += 1
        return res