# 003无重复最长子串.py
class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     #利用滑动窗口模板
    #     if s is None or len(s) == 0:
    #         return 0
    #     length = len(s)
    #     charArr = [0 for i in range(length)]
    #     res = 1
    #     left = 0
    #     for i in range(length):
    #         charArr[i] = ord(s[i])
    #     hash = [0 for i in range(257)]
    #     for right in range(length):
    #         # 构建hash数组
    #         hash[charArr[right]] += 1
    #         # 左指针移动的条件，左指针指向不重复
    #         while hash[charArr[right]] != 1:
    #             hash[charArr[left]] -= 1
    #             left += 1
    #         res = max(res,right - left + 1)
    #     return res
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        length = len(s)
        from collections import defaultdict
        result = 0
        # 默认初始化value为0
        hash = defaultdict(int)
        l = 0
        for r in range(length):
            hash[s[r]] += 1
            while hash[s[r]] != 1:
                hash[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result
