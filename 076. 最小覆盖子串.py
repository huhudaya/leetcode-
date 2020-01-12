# 76. 最小覆盖子串.py
'''
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

链接：https://leetcode-cn.com/problems/minimum-window-substring
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #滑动窗口模板
        length_s = len(s)
        length_t = len(t)
        count = length_t
        hash = [0 for i in range(256)]
        right = 0
        left = 0
        #注意这里_max的取值需要+1
        _max = length_s+1
        res = ""
        if length_s < length_t:
            return ""
        #构建hash数组
        for i in range(length_t):
            hash[ord(t[i])] += 1
        #双指针 因为只扫原数组一次，所以时间复杂度是O(n)
        for right in range(length_s):
            hash[ord(s[right])] -= 1
            if hash[ord(s[right])] >= 0:
                count -= 1
            # 左指针移动条件，left指针始终指向子串中的一个元素
            while left < right and hash[ord(s[left])] < 0:
                hash[ord(s[left])] += 1
                left += 1
            if count == 0 and _max > right - left + 1:
                _max = right - left + 1
                res = s[left:right+1]
        return res