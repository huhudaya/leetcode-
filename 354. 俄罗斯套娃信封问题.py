# 354. 俄罗斯套娃信封问题.py
'''
给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

说明:
不允许旋转信封。

示例:

输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出: 3 
解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
链接：https://leetcode-cn.com/problems/russian-doll-envelopes
'''


# 暴力dp 时间复杂度O(N2)
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 转换为求最长递增子序列
        import functools
        length = len(envelopes)
        envelopes.sort(key=functools.cmp_to_key(self.sortEnvelopes))
        # 求LIS
        heigh = [envelope[1] for envelope in envelopes]
        return self.lengthOfLIS(heigh)

    def lengthOfLIS(self, heigh):
        length = len(heigh)
        if len(heigh) == 0:
            return 0
        dp = [1 for i in range(length)]
        for i in range(length):
            for j in range(i):
                if heigh[i] > heigh[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)

    def sortEnvelopes(self, cur, pre):
        return pre[1] - cur[1] if cur[0] == pre[0] else cur[0] - pre[0]


# 二分法
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        import bisect
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        arr = []
        for _, y in envelopes:
            loc = bisect.bisect_left(arr, y)
            arr[loc:loc + 1] = [y]
        return len(arr)


# 二分法
from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, arr: List[List[int]]) -> int:
        # sort increasing in first dimension and decreasing on second
        arr.sort(key=lambda x: (x[0], -x[1]))

        def lis(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)

        # extract the second dimension and run the LIS
        return lis([i[1] for i in arr])


# 自己的版本
class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        # 转换为求最长递增子序列
        import functools
        length = len(envelopes)
        # envelopes.sort(key = functools.cmp_to_key(self.sortEnvelopes))
        envelopes.sort(key=lambda x: x(x[0], -x[1]))
        # 求LIS
        # 得到tuple[1]的元素
        heigh = [envelope[1] for envelope in envelopes]
        return self.lengthOfLIS(heigh)

    # def lengthOfLIS(self, heigh):
    #     length = len(heigh)
    #     if len(heigh) == 0:
    #         return 0
    #     dp = [1 for i in range(length)]
    #     for i in range(length):
    #         for j in range(i):
    #             if heigh[i] > heigh[j]:
    #                 dp[i] = max(dp[j] + 1, dp[i])
    #     return max(dp)
    def lengthOfLIS(self, heigh):
        n = len(heigh)
        top = [0 for i in range(n + 1)]
        # 堆数
        piples = 0
        for i in range(n):
            # 要处理的扑克牌
            poker = heigh[i]
            left = 0
            right = piples
            target = 0
            # 找 left 边界
            while left + 1 < right:
                mid = left + (right - left) // 2
                if top[mid] >= poker:
                    right = mid
                else:
                    left = mid
            if top[left] >= poker:
                target = left
            elif top[right] >= poker:
                target = right
            else:
                target = right + 1
            if target == piples + 1:
                piples += 1
            # 更新牌顶
            top[target] = poker
        return piples

    def sortEnvelopes(self, cur, pre):
        return pre[1] - cur[1] if cur[0] == pre[0] else cur[0] - pre[0]
