# 300. 最长上升子序列.py
'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
'''
'''
我们的定义是这样的：dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度。

至此，这道题就解决了，时间复杂度 O(N^2)。总结一下动态规划的设计流程：
首先明确 dp 数组所存数据的含义。这步很重要，如果不得当或者不够清晰，会阻碍之后的步骤
然后根据 dp 数组的定义，运用数学归纳法的思想，假设 dp[0...i-1] 都已知，想办法求出 dp[i]
一旦这一步完成，整个题目基本就解决了
但如果无法完成这一步，很可能就是 dp 数组的定义不够恰当，需要重新定义 dp 数组的含义
或者可能是 dp 数组存储的信息还不够，不足以推出下一步的答案，需要把 dp 数组扩大成二维数组甚至三维数组
最后想一想问题的 base case 是什么，以此来初始化 dp 数组，以保证算法正确运行
'''
from typing import List


class Solution:
    def lengthOfLIS(self, nums):
        if nums is None or nums == []:
            return 0
        # dp思想
        n = len(nums)
        # base case为1
        dp = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)


# 二分
'''
public int lengthOfLIS(int[] nums) {
    int[] top = new int[nums.length];
    // 牌堆数初始化为 0
    int piles = 0;
    for (int i = 0; i < nums.length; i++) {
        // 要处理的扑克牌
        int poker = nums[i];

        /***** 搜索左侧边界的二分查找 *****/
        int left = 0, right = piles;
        while (left < right) {
            int mid = (left + right) / 2;
            if (top[mid] >= poker) {
                right = mid;
            } else if (top[mid] < poker) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        /*********************************/   
        // 没找到合适的牌堆，新建一堆
        if (left == piles) piles++;
        // 把这张牌放到牌堆顶
        top[left] = poker;
    }
    // 牌堆数就是 LIS 长度
    return piles;
}
'''
from bisect import bisect_left

a = [1, 1, 2, 2, 4]


# print(bisect_left(a, 2))


# 二分法
# 核心思路是找见第一个大于等于当前元素的索引
# Dynamic programming + Dichotomy.
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        tails = [0] * len(nums)
        res = 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else:
                    j = m
            tails[i] = num
            if j == res:
                res += 1
        return res


import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        q = [-float('inf')]
        for i in nums:
            if i > q[-1]:
                q += [i]
            else:
                q[bisect.bisect_left(q, i)] = i
        return len(q) - 1

# 自己的版本
# 二分 O(NlogN)
# 核心思路是找见第一个大于等于当前元素的索引
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        top = [-float('inf') for _ in range(n)]
        piples = 0
        for i in range(n):
            poker = nums[i]
            left = 0
            right = piples
            # 当前 i 要进入的堆的索引
            index = 0
            # log(N) 找左边界
            while left + 1 < right:
                mid = left + (right - left) // 2
                if top[mid] >= poker:
                    right = mid
                else:
                    left = mid
            if top[left] >= poker:
                index = left
            else:
                index = right
            # 否则新建一个堆  注意这里的piples实际上是right = len(nums),一般我们做题的时候应该是right = len(nums)-1
            if index == piples:
                piples += 1
            top[index] = poker
        return piples


# 二分 O(NlogN)
class Solution:
    def lengthOfLIS1(self, nums: List[int]) -> int:
        n = len(nums)
        top = [0 for _ in range(n)]
        piples = 0
        for i in range(n):
            poker = nums[i]
            left = 0
            right = piples
            # 当前 i 要进入的堆的索引
            index = 0
            # log(N) 找左边界
            while left + 1 < right:
                mid = left + (right - left) // 2
                if top[mid] >= poker:
                    right = mid
                else:
                    left = mid
            if top[left] >= poker:
                index = left
            else:
                index = right
            # 否则新建一个堆
            if index == piples:
                piples += 1
            top[index] = poker
        return piples

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # 牌堆，默认值为最小值
        top = [-float('inf') for _ in range(n)]
        piples = 0
        for i in range(n):
            # 当前牌
            poker = nums[i]
            left = 0
            right = piples
            # 当前 i 要进入的堆的索引
            index = 0
            # log(N) 找左边界
            while left + 1 < right:
                mid = left + (right - left) // 2
                if top[mid] >= poker:
                    right = mid
                else:
                    left = mid
            if top[left] >= poker:
                index = left
            elif top[right] >= poker:
                index = right
            # 否则新建一个堆  注意这里的piples实际上是right = len(nums),一般我们做题的时候应该是right = len(nums)-1
            else:
                index = right
                piples += 1
            top[index] = poker
        return piples
print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
