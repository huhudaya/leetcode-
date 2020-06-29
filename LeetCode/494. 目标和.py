'''
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
返回可以使最终数组和为目标数 S 的所有添加符号的方法数。
示例：
输入：nums: [1, 1, 1, 1, 1], S: 3
输出：5
解释：
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
一共有5种方法让最终目标和为3。

提示：
数组非空，且长度不会超过 20 。
初始的数组的和不会超过 1000 。
保证返回的最终结果能被 32 位整数存下
'''
# 递归
'''
public class Solution {
    int count = 0;
    public int findTargetSumWays(int[] nums, int S) {
        calculate(nums, 0, 0, S);
        return count;
    }
    public void calculate(int[] nums, int i, int sum, int S) {
        if (i == nums.length) {
            if (sum == S)
                count++;
        } else {
            calculate(nums, i + 1, sum + nums[i], S);
            calculate(nums, i + 1, sum - nums[i], S);
        }
    }
}
'''
# 递归
import functools
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # 递归
        if not nums:
            return -1
        n = len(nums)

        @functools.lru_cache(None)
        def dfs(i, target):
            res = 0
            if i == n:
                if target == 0:
                    return 1
                return 0
            res += dfs(i + 1, target - nums[i])
            res += dfs(i + 1, target + nums[i])
            return res

        return dfs(0, S)


print(Solution().findTargetSumWays([0, 38, 42, 31, 13, 10, 11, 12, 44, 16, 38, 17, 22, 28, 9, 27, 20, 35, 34, 39], 2))

# 注意 这道题和其他背包问题最大的不同就是这道题数组中的每一个数字都必须使用一次
# 迭代
from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # dp 注意这道题和其它背包问题的不同，这道题要求数组中的每一个元素都必须使用到
        if not nums:
            return -1
        # dp[i]表示当目标为 i 时有几种解法
        dp = defaultdict(int)
        dp[0] = 1
        # 每一轮num更新一次dp
        for num in nums:
            tmp = defaultdict(int)
            for k, v in dp.items():
                tmp[k - num] += v
                tmp[k + num] += v
            dp = tmp
        return dp[S]


# 动态规划
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if sum(nums) < S or (sum(nums) + S) % 2 == 1:
            return 0
        P = (sum(nums) + S) // 2
        dp = [1] + [0 for _ in range(P)]
        for num in nums:
            for j in range(P, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[P]
