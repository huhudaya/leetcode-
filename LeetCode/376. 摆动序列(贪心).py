'''
如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。
第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。

例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。
相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。

给定一个整数序列，返回作为摆动序列的最长子序列的长度。
通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。

示例 1:

输入: [1,7,4,9,2,5]
输出: 6
解释: 整个序列均为摆动序列。
示例 2:

输入: [1,17,5,10,13,15,10,5,16,8]
输出: 7
解释: 这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10,13,10,16,8]。
示例 3:

输入: [1,2,3,4,5,6,7,8,9]
输出: 2
进阶:
你能否用 O(n) 时间复杂度完成此题?
'''
'''
本题大家都很容易想到用动态规划来求解，求解的过程类似最长上升子序列，不过是需要判断两个序列。大家在实现动态规划的平方复杂度时，就会考虑如何优化到线性复杂度。

假设up[i]表示nums[0:i]中最后两个数字递增的最长摆动序列长度，down[i]表示nums[0:i]中最后两个数字递减的最长摆动序列长度，只有一个数字时默认为1。

接下来我们进行分类讨论：

nums[i+1] > nums[i]
假设down[i]表示的最长摆动序列的最远末尾元素下标正好为i，遇到新的上升元素后，up[i+1] = down[i] + 1，这是因为up一定从down中产生（初始除外），并且down[i]此时最大。
假设down[i]表示的最长摆动序列的最远末尾元素下标小于i，设为j，那么nums[j:i]一定是递增的，因为若完全递减，最远元素下标等于i，若波动，那么down[i] > down[j]。由于nums[j:i]递增，down[j:i]一直等于down[j]，依然满足up[i+1] = down[i] + 1。
nums[i+1] < nums[i]，类似第一种情况
nums[i+1] == nums[i]，新的元素不能用于任何序列，保持不变
'''

# 统计波峰的个数 贪心
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return n
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1
            if nums[i] < nums[i - 1]:
                down = up + 1
        return max(up, down)


# 动态规划未优化
class Solution(object):
    def wiggleMaxLength(self, nums):
        if len(nums) <= 1:
            return len(nums)
        # dp[i][0]是以 i 结尾的上升序列
        # dp[i][1]是以 i 结尾的下降序列
        dp = [[0] * 2 for _ in range(len(nums))]
        dp[0][1] = 1
        dp[0][0] = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    # 前一个需要是下降的，所以找到dp[i][1]的部分
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)
                #   dp[i][1] = max(dp[i][1], dp[i-1][1])
                elif nums[i] < nums[j]:
                    # 找到之前的上升的部分，然后进行比较
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)
                #    dp[i][0] = max(dp[i][0], dp[i-1][0])
                else:
                    dp[i] = dp[j]
        return max(dp[len(nums) - 1])


# 动态规划优化
'''
把dp[i] 定义为到第i+1个元素所得到的最大摆动长度， dp[i] 中还是有[up, down]两个满足条件的记录。

与第一种解法不同的是， 如果符合更新 up 的条件， 那么down 需要和上一个元素的down 一致， 反之亦然。

为什么只用看前一个元素， 因为前一个元素的结果可以囊括它之前单调递减或者单调递增的元素所有结果。
'''


class Solution(object):
    def wiggleMaxLength(self, nums):
        # 把dp[i] 定义为到第i+1个元素所得到的最大摆动长度
        dp = [[1] * 2 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i][0] = max(dp[i][0], dp[i - 1][1] + 1)
                dp[i][1] = max(dp[i][1], dp[i - 1][1])
            elif nums[i] < nums[i - 1]:
                dp[i][1] = max(dp[i][1], dp[i - 1][0] + 1)
                dp[i][0] = max(dp[i][0], dp[i - 1][0])
            else:
                dp[i] = dp[i - 1]
        return max(dp[len(nums) - 1])
