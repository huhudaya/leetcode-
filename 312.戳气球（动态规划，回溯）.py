'''
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

求所能获得硬币的最大数量。

说明:

你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
示例:

输入: [3,1,5,8]
输出: 167
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
'''
# 回溯的思路
'''
我们前文多次强调过，很显然只要涉及求最值，没有任何奇技淫巧，一定是穷举所有可能的结果，然后对比得出最值。

所以说，只要遇到求最值的算法问题，首先要思考的就是：如何穷举出所有可能的结果？

穷举主要有两种算法，就是回溯算法和动态规划，前者就是暴力穷举，而后者是根据状态转移方程推导「状态」。

如何将我们的扎气球问题转化成回溯算法呢？这个应该不难想到的，我们其实就是想穷举戳气球的顺序，不同的戳气球顺序可能得到不同的分数，我们需要把所有可能的分数中最高的那个找出来，对吧。

那么，这不就是一个「全排列」问题嘛，我们前文 回溯算法框架套路详解 中有全排列算法的详解和代码，其实只要稍微改一下逻辑即可，伪码思路如下：

int res = Integer.MIN_VALUE;
/* 输入一组气球，返回戳破它们获得的最大分数 */
int maxCoins(int[] nums) {
    backtrack(nums, 0);
    return res;
}
/* 回溯算法的伪码解法 */
void backtrack(int[] nums, int socre) {
    if (nums 为空) {
        res = max(res, score);
        return;
    }
    for (int i = 0; i < nums.length; i++) {
        int point = nums[i-1] * nums[i] * nums[i+1];
        int temp = nums[i];
        // 做选择
        在 nums 中删除元素 nums[i]
        // 递归回溯
        backtrack(nums, score + point);
        // 撤销选择
        将 temp 还原到 nums[i]
    }
}
回溯算法就是这么简单粗暴，但是相应的，算法的效率非常低。
这个解法等同于全排列，所以时间复杂度是阶乘级别，非常高
题目说了nums的大小n最多为 500，所以回溯算法肯定是不能通过所有测试用例的。
'''

# 动态规划
# dp[i][j] = x表示，戳破气球i和气球j之间（开区间，不包括i和j）的所有气球，可以获得的最高分数为x。
# 那么根据这个定义，题目要求的结果就是dp[0][n+1]的值，而 base case 就是dp[i][j] = 0，其中0 <= i <= n+1, j <= i+1，因为这种情况下，开区间(i, j)中间根本没有气球可以戳。
# 不就是想求戳破气球i和气球j之间的最高分数吗，如果「正向思考」，就只能写出前文的回溯算法；我们需要「反向思考」，想一想气球i和气球j之间最后一个被戳破的气球可能是哪一个？
# 其实气球i和气球j之间的所有气球都可能是最后被戳破的那一个，不防假设为k。
# 回顾动态规划的套路，这里其实已经找到了「状态」和「选择」：i和j就是两个「状态」，最后戳破的那个气球k就是「选择」。

# 你不是要最后戳破气球k吗？那得先把开区间(i, k)的气球都戳破，再把开区间(k, j)的气球都戳破；
# 最后剩下的气球k，相邻的就是气球i和气球j，这时候戳破k的话得到的分数就是points[i]*points[k]*points[j]。
#
# 那么戳破开区间(i, k)和开区间(k, j)的气球最多能得到的分数是多少呢？
# 就是dp[i][k]和dp[k][j]，这恰好就是我们对dp数组的定义嘛！
# c++
'''
int maxCoins(int[] nums) {
    int n = nums.length;
    // 添加两侧的虚拟气球
    int[] points = new int[n + 2];
    points[0] = points[n + 1] = 1;
    for (int i = 1; i <= n; i++) {
        points[i] = nums[i - 1];
    }
    // base case 已经都被初始化为 0
    int[][] dp = new int[n + 2][n + 2];
    // 开始状态转移
    // i 应该从下往上
    for (int i = n; i >= 0; i--) {
        // j 应该从左往右
        for (int j = i + 1; j < n + 2; j++) {
            // 最后戳破的气球是哪个？
            for (int k = i + 1; k < j; k++) {
                // 择优做选择
                dp[i][j] = Math.max(
                    dp[i][j], 
                    dp[i][k] + dp[k][j] + points[i]*points[j]*points[k]
                );
            }
        }
    }
    return dp[0][n + 1];
}
'''
# https://mp.weixin.qq.com/s/I0yo0XZamm-jMpG-_B3G8g
from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        points = [0 for i in range(n + 2)]
        points[0] =  1
        points[-1] = 1
        for i in range(n):
            points[i + 1] = nums[i]
        # 动态规划
        # dp[i][j] = x表示，戳破气球i和气球j之间（开区间，不包括i和j）的所有气球，可以获得的最高分数为x。
        # 定义最后戳破气球为k，那得先把开区间(i, k)的气球都戳破，再把开区间(k, j)的气球都戳破；
        # 1.定义dp数组
        dp = [[0] * (n + 2 ) for _ in range(n + 2)]
        # 2.定义base case 已经初始化为0
        # 3.开始状态转移
        # i 应该从下往上
        for i in range(n + 2, -1, -1):
            # j 应该从左往右
            for j in range(i + 1, n + 2):
                # 找最大的
                for k in range(i + 1, j):
                    a = dp[i][j]
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + points[i] * points[k] * points[j])
        return dp[0][n + 1]
print(Solution().maxCoins([3,1,5,8]))