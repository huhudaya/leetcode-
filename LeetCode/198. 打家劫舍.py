# 198. 打家劫舍.py
'''
你是一个专业的小偷，计划偷窃沿街的房屋。
每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

链接：https://leetcode-cn.com/problems/house-robber
'''
'''
public int rob(int[] nums) {
    if (nums == null || nums.length == 0) {
        return 0;
    }

    int n = nums.length;

    int[] dp = new int[n + 1];

    dp[1] = nums[0];

    for (int i = 2; i <= n; ++i) {
        dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i - 1]);
    }

    return dp[n];
}
'''
from typing import List

# 这类动态规划的题目都有一个特点，就是需要找状态和选择！！！！！！
# 状态一般用for循环，选择的时候一般是max,min，或者别的一些比较
# 动态规划都是自底向上的，要有一种从底向上的思想，这就要求我们在定义dp数组函数的时候就要定义清楚了。

class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp
        if nums is None or len(nums) == 0:
            return 0
        n = len(nums)
        # dp[i] = x 表示：
        # 到第 i 间房子为止，最多能抢到的钱为 x
        # base case: dp[1] = 0
        # 定义dp数组，这里长度加1
        dp = [0 for _ in range(n + 1)]
        # base case
        dp[1] = nums[0] #第一天，最多能抢劫num[0]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1],#当前不抢劫，然后加上一家的状态
                        dp[i - 2] + nums[i - 1]#抢劫当前然后加上上一家的值
                        )
        return dp[n]

'''
这就是自顶向下的动态规划解法，我们也可以略作修改，写出自底向上的解法：

 int rob(int[] nums) {
    int n = nums.length;
    // dp[i] = x 表示：
    // 从第 i 间房子开始抢劫，最多能抢到的钱为 x
    // base case: dp[n] = 0
    int[] dp = new int[n + 2];
    //注意 这里是倒着遍历，因为这个时候的dp数组的定义是从第 i 间房子开始抢劫，最多能抢到的钱为 x
    for (int i = n - 1; i >= 0; i--) {
        dp[i] = Math.max(dp[i + 1], nums[i] + dp[i + 2]);
    }
    return dp[0];
}
我们又发现状态转移只和dp[i]最近的两个状态有关，所以可以进一步优化，将空间复杂度降低到 O(1)。

int rob(int[] nums) {
    int n = nums.length;
    // 记录 dp[i+1] 和 dp[i+2]
    int dp_i_1 = 0, dp_i_2 = 0;
    // 记录 dp[i]
    int dp_i = 0; 
    for (int i = n - 1; i >= 0; i--) {
        dp_i = Math.max(dp_i_1, nums[i] + dp_i_2);
        dp_i_2 = dp_i_1;
        dp_i_1 = dp_i;
    }
    return dp_i;
'''
