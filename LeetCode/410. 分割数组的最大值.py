'''
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。
设计一个算法使得这 m 个子数组各自和的最大值最小。

注意:
数组长度 n 满足以下条件:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
示例:

输入:
nums = [7,2,5,10,8]
m = 2

输出:
18

解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
'''
'''
2019-03-25
首先分析题意，可以得出结论，结果必定落在【max（nums）,sum（nums）】这个区间内
因为左端点对应每个单独的元素构成一个子数组，右端点对应所有元素构成一个子数组。

然后可以利用二分查找法逐步缩小区间范围，当区间长度为1时，即找到了最终答案。

每次二分查找就是先算一个mid值，这个mid就是代表当前猜测的答案，然后模拟一下划分子数组的过程，可以得到用这个mid值会一共得到的子区间数cnt，然后比较cnt和m的关系，来更新区间范围。

本题跟1014 875 非常类似。
'''


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # max(nums), sum(nums)
        if len(nums) == m:
            return max(nums)

        lo, hi = max(nums), sum(nums)
        while (lo < hi):
            mid = (lo + hi) // 2  # 最大和

            # ------以下在模拟划分子数组的过程
            temp, cnt = 0, 1
            for num in nums:
                temp += num
                # cnt += 1
                if temp > mid:  # 说明当前这个子数组的和已经超过了允许的最大值mid，需要把当前元素放在下一个子数组里
                    temp = num
                    cnt += 1
            # print temp, cnt, mid
            # ------以上在模拟划分子数组的过程

            if cnt > m:  # 说明分出了比要求多的子数组，多切了几刀，说明mid应该加大，这样能使子数组的个数减少
                lo = mid + 1
            elif cnt <= m:
                hi = mid

        return lo


from typing import List

# 时间复杂度O(Nlog(Nsum(arr))
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # 理清楚一个关系,如果每个子数组之和不超过limit的个数越多,则可以划分的数组越少
        # 正因为成反比的情况，所以可以求得分组的个数大于等于m的first位置，此时分组的和的max即分割数组的最大值
        n = len(nums)

        def get_num(limit):
            cur_sum = 0
            cnt = 1
            for num in nums:
                if cur_sum + num > limit:
                    cnt += 1
                    cur_sum = 0
                cur_sum += num
            return cnt

        left = max(nums)
        right = sum(nums)
        while left + 1 < right:
            mid = left + (right - left) // 2
            if get_num(mid) <= m:
                right = mid
            else:
                left = mid
        if get_num(left) <= m:
            return left
        if get_num(right) <= m:
            return right
        return -1

# 动态规划
'''
思路

这个问题满足无后向性的特点。我们可以用动态规划来解决它。

无后向性的特点意味着，一旦当前状态确定了，它就不会被之后的状态影响。在这个问题里面，如果我们在将 nums[0..i] 分成 j 份时得到了当前最小的分割数组的最大值，不论后面的部分怎么分割这个值不会受到影响。

算法

首先我们把 f[i][j] 定义为将 nums[0..i] 分成 j 份时能得到的最小的分割子数组最大值。

对于第 j 个子数组，它为数组中下标 k + 1 到 i 的这一段。因此，f[i][j] 可以从 max(f[k][j - 1], nums[k + 1] + ... + nums[i]) 这个公式中得到。遍历所有可能的 k，会得到 f[i][j] 的最小值。

整个算法那的最终答案为 f[n][m]，其中 n 为数组大小。
'''

# Java
'''
class Solution {
    public int splitArray(int[] nums, int m) {
        int n = nums.length;
        int[][] f = new int[n + 1][m + 1];
        int[] sub = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                f[i][j] = Integer.MAX_VALUE;
            }
        }
        for (int i = 0; i < n; i++) {
            sub[i + 1] = sub[i] + nums[i];
        }
        f[0][0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                for (int k = 0; k < i; k++) {
                    // 首先我们把 f[i][j] 定义为将 nums[0..i] 分成 j 份时能得到的最小的分割子数组最大值。
                    f[i][j] = Math.min(f[i][j], Math.max(f[k][j - 1], sub[i] - sub[k]));
                }
            }
        }
        return f[n][m];        
    }
}
'''

# DP
def splitArray(self, nums: List[int], m: int) -> int:
    length = len(nums)
    if length <= m:
        return max(nums)

    # dp[i][j] 表示 nums[:i + 1] 分成 j + 1 份时的最小和
    # dp[i][j] = min(dp[i][j], max(dp[k][j - 1], sum(nums[k + 1:i + 1]))), 0 <= k < i
    # 状态转移方程中，dp[k][j - 1] 表示前 k 个数字(包括第 k 个数字)已分成 j 份时的最小和，
    # 由于新加了一个数字 nums[i]，数组就分成了 "已经被分成 j 份的 num[:k + 1]" 和 "第 j + 1 份的 num[k + 1:i + 1]"
    # 这时候的最小和就是前半部分和后半部分数字和的最大值，即为 max(dp[k][j - 1], sum(nums[k + 1:i + 1])), 0<= k < i
    dp = [[float('inf')] * m for _ in range(length)]

    for i in range(length):
        # 不用考虑1个数字分成2份，2个数字分成3份的情况
        for j in range(min(i + 1, m)):
            if i == 0:
                # 只有一个数字时，无论分几份，最小和都是这个数
                dp[0][j] = nums[0]
            elif j == 0:
                # 只分成1份时，无论有几个数，最小和都是这些数的和
                dp[i][0] = nums[i] + dp[i - 1][0]
            else:
                # 因为不用考虑1个数字分成2份，2个数字分成3份的情况，所以 k 从 j - 1 开始遍历即可
                for k in range(j - 1, i + 1):
                    # 相当于是考虑最后一个子数组
                    # 因为 dp[i][0] 就是 sum(num[:i + 1])，
                    # 所以状态转移方程中的 sum(nums[k + 1:i + 1])) 可以改为 dp[i][0] - dp[k][0]
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], dp[i][0] - dp[k][0]))

    return dp[-1][-1]
