# 567. 字符串的排列.py
'''
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
 

示例2:

输入: s1= "ab" s2 = "eidboaoo"
输出: False

链接：https://leetcode-cn.com/problems/permutation-in-string
'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        hash = defaultdict(int)
        m, n = len(s1), len(s2)
        if m > n:
            return False
        for i in range(m):
            hash[s1[i]] += 1
        right = 0
        left = 0
        count = 0
        while right < n:
            hash[s2[right]] -= 1
            if hash[s2[right]] >= 0:
                count += 1
            # 大于窗口,移动左指针
            if right > m - 1:
                hash[s2[left]] += 1
                if hash[s2[left]] > 0:
                    count -= 1
                left += 1
            right += 1            
            if count == m:
                return True
        return False

