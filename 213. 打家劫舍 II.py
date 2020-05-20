# 213. 打家劫舍 II.py
'''
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2:

输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。

链接：https://leetcode-cn.com/problems/house-robber-ii
'''
from typing import List

# 首先，首尾房间不能同时被抢，那么只可能有三种不同情况：
# 要么都不被抢；
# 要么第一间房子被抢最后一间不抢；
# 要么最后一间房子被抢第一间不抢。
'''
那就简单了啊，这三种情况，哪种的结果最大，就是最终答案呗！
不过，其实我们不需要比较三种情况，只要比较情况二和情况三就行了
因为这两种情况对于房子的选择余地比情况一大呀
房子里的钱数都是非负数，所以选择余地大，最优决策结果肯定不会小
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        res = max(self.rob1(nums[0: n - 1]), self.rob1(nums[1: n]))
        return res

    def rob1(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        n = len(nums)
        dp = [0 for i in range(n + 1)]
        dp[1] = nums[0]
        # 这里必须是小于n+1
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[n]
