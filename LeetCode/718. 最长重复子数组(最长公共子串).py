# 718. 最长重复子数组.py
"""
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例 1:

输入:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出: 3
解释:
长度最长的公共子数组是 [3, 2, 1]。
说明:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

链接：https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray
"""
'''
动态规划思路:
1.明确dp数组的含义
2.明确base case
3.找状态转义方程
'''
from typing import List
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        # 最长公共子串
        m, n = len(A), len(B)
        # dp[i][j]定义为以i，j结尾的最长子串
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(dp[i][j], res)
        return res
