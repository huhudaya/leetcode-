# 1004. 最大连续1的个数 III.py
'''
给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。
返回仅包含 1 的最长（连续）子数组的长度。
示例 1:
输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：
[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。
示例 2：

输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。
 
提示：
1 <= A.length <= 20000
0 <= K <= A.length
A[i] 为 0 或 1 
链接：https://leetcode-cn.com/problems/max-consecutive-ones-iii
'''
# 滑动窗口 O(N)
from collections import defaultdict
class Solution:
    def longestOnes(self, A, K: int) -> int:
        # 滑动窗口
        if A is None or len(A) == 0:
            return 0
        hash = defaultdict(int)
        n = len(A)
        maxCount = 0
        left = 0
        res = 0
        for right in range(n):
            hash[A[right]] += 1
            # 找到 1 的最大数量
            maxCount = max(maxCount, hash[1])
            if right - left + 1 - maxCount > K:
                hash[A[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))




