# 053. 最大子序和.py
'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解

链接：https://leetcode-cn.com/problems/maximum-subarray
'''

'''
求最大子数组和，非常经典的一道题目，这道题目有很多种不同的做法
而且很多算法思想都可以在这道题目上面体现出来
比如动态规划、贪心、分治，还有一些技巧性的东西，比如前缀和数组
这里还是使用动态规划的思想来解题，套路还是之前的四步骤：

问题拆解：

问题的核心是子数组，子数组可以看作是一段区间，因此可以由起始点和终止点确定一个子数组
两个点中，我们先确定一个点，然后去找另一个点
比如说，如果我们确定一个子数组的截止元素在 i 这个位置
这个时候我们需要思考的问题是 “以 i 结尾的所有子数组中，和最大的是多少？”
然后我们去试着拆解，这里其实只有两种情况：

   i 这个位置的元素自成一个子数组;

   i 位置的元素的值 + 以 i - 1 结尾的所有子数组中的子数组和最大的值

你可以看到，我们把第 i 个问题拆成了第 i - 1 个问题，之间的联系也变得清晰

状态定义

通过上面的分析，其实状态已经有了，dp[i] 就是 “以 i 结尾的所有子数组的最大值”

递推方程

拆解问题的时候也提到了，有两种情况，即当前元素自成一个子数组，另外可以考虑前一个状态的答案，于是就有了

dp[i] = Math.max(dp[i - 1] + array[i], array[i])
化简一下就成了：

dp[i] = Math.max(dp[i - 1], 0) + array[i]
实现

题目要求子数组不能为空，因此一开始需要初始化，也就是 dp[0] = array[0]
保证最后答案的可靠性，另外我们需要用一个变量记录最后的答案，因为子数组有可能以数组中任意一个元素结尾
'''
# dp[i] 就是 “以 i 结尾的所有子数组的最大值”
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp思想
        n = len(nums)
        # dp[i] 就是 “以 i 结尾的所有子数组的最大值”
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            # dp[i] = max(dp[i-1]+nums[i], nums[i])
            dp[i] = max(dp[i - 1], 0) + nums[i]
        res = max(dp)
        return res

    # 线性循环
    '''
     该算法更为简便之处是忽略了对子序列的寻找比较,而是根据规律直接找出最佳答案.

     对于含有正数的序列而言,最大子序列肯定是正数,所以头尾肯定都是正数.我们可以从第一个正数开始算起
     每往后加一个数便更新一次和的最大值;
     当 当前和成为负数时,则表明此前序列无法为后面提供最大子序列和,因此必须重新确定序列首项.
     意思就是我们将前面一大串的和视作一个头，如果头是负数，则一定是不满足的！！！！！，我们需要重新选择一个头

     上文引用来自https://www.cnblogs.com/sunnysola/p/4795691.html
    '''

    def maxSubArray(self, nums: List[int]) -> int:
        import sys
        n = len(nums)
        sum_i = 0
        res = -sys.maxsize
        for i in range(n):
            # 如果可以获取正向增益
            if sum_i > 0:
                sum_i += nums[i]
            else:
                sum_i = nums[i]
            res = max(sum_i, res)
        return res

import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = -sys.maxsize
        tmp = 0
        for i in range(n):
            if tmp < 0:
                tmp = 0
            tmp += nums[i]
            res = max(res, tmp)
        return res

'''
func maxSubArray(nums []int) int {
	ans := nums[0]
	cur := nums[0]
	if len(nums) == 1 {
		return nums[0]
	}
	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}
	for i := 1; i < len(nums); i++ {
		// 判断 cur是否大于0
		// 如果小于0,就舍弃之前的值，否则更新值
		cur = max(nums[i], cur+nums[i])
		ans = max(cur, ans)
	}
	return ans
}
'''