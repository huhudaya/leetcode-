# 055. 跳跃游戏.py
'''
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

链接：https://leetcode-cn.com/problems/jump-game
'''
'''
思路：尽可能到达最远位置（贪心）。
如果能到达某个位置，那一定能到达它前面的所有位置。

方法：初始化最远位置为0，然后遍历数组，如果当前位置能到达
并且当前位置+跳数>最远位置，就更新最远位置。最后比较最远位置和数组长度。

复杂度：时间复杂度O(n)，空间复杂度O(1)。
'''


# 贪心 局部最优 全局最优
class Solution:
    def canJump(self, nums):
        max_i = 0  # 初始化当前能到达最远的位置
        for i, jump in enumerate(nums):  # i为当前位置，jump是当前位置的跳数
            # 如果max_i 不大于 i，说明就到不了i这个位置
            if max_i >= i and i + jump > max_i:  # 如果当前位置能到达，并且当前位置+跳数>最远位置
                max_i = i + jump  # 更新最远能到达位置
        return max_i >= i



# 从后向前
class Solution:
    def canJump(self, nums) -> bool:
        lastindex = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if (i + nums[i] >= lastindex):
                lastindex = i
        return lastindex == 0


# 从前向后
class Solution:
    def canJump(self, nums) -> bool:
        max_bound = 0
        n = len(nums)
        end = 0
        for i in range(n):
            max_bound = max(max_bound, nums[i] + i)
            if (i == end): #更新边界
                end = max_bound
            if (end >= n - 1):
                return True
        return False


# 自己的版本
class Solution:
    def canJump(self, nums) -> bool:
        # 贪心
        max_bound = 0
        n = len(nums)
        end = 0
        for i in range(n):
            max_bound = max(max_bound, nums[i] + i)
            # 遇到边界，就更新边界
            if i == end:
                end = max_bound
            if end >= n - 1:
                return True
        return False


print(Solution().canJump([3, 2, 1, 0, 4]))
