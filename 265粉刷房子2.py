# 265粉刷房子2.py
'''
假如有一排房子，共 n 个，每个房子可以被粉刷成 k 种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。

当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x k 的矩阵来表示的。

例如，costs[0][0] 表示第 0 号房子粉刷成 0 号颜色的成本花费；costs[1][2] 表示第 1 号房子粉刷成 2 号颜色的成本花费，以此类推。请你计算出粉刷完所有房子最少的花费成本。

注意：

所有花费均为正整数。

示例：

输入: [[1,5,3],[2,9,4]]
输出: 5
解释: 将 0 号房子粉刷成 0 号颜色，1 号房子粉刷成 2 号颜色。最少花费: 1 + 4 = 5; 
     或者将 0 号房子粉刷成 2 号颜色，1 号房子粉刷成 0 号颜色。最少花费: 3 + 2 = 5.
'''


'''
上面那道题目的 follow up，现在不是三种油漆，而是 k 种油漆。

其实解题思路还是不变。

对于第 i 个房子的每种颜色，我们对比看第 i - 1 个房子的 k 种油漆，找到不相重的最小值就好，但是这里的时间复杂度是 O(n*k^2)。

其实这是可以优化的，我们只需要在第 i - 1 个位置的状态中找到最大值和次大值，在选择第 i 个房子的颜色的时候
我们看当前颜色是不是和最大值的颜色相重，不是的话直接加上最大值，
如果相重的话，我们就加上次大值，这样一来，我们把两个嵌套的循环，
拆开成两个平行的循环，时间复杂度降至 O(n*k)。
'''

# 优化前
'''
//@五分钟学算法
//www.cxyxiaowu.com
public int minCostII(int[][] costs) {
    if (costs.length == 0 || costs[0].length == 0) {
        return 0;
    }

    int n = costs.length, k = costs[0].length;
    int[][] dp = new int[n][k];

    for (int i = 1; i < n; ++i) {
        Arrays.fill(dp[i], Integer.MAX_VALUE);
    }

    for (int i = 0; i < k; ++i) {
        dp[0][i] = costs[0][i];
    }        

    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < k; ++j) {
            for (int m = 0; m < k; ++m) {
                if (m != j) {
                    dp[i][m] = Math.min(dp[i][m], dp[i - 1][j] + costs[i][m]);
                }
            }
        }
    }

    int result = Integer.MAX_VALUE;
    for (int i = 0; i < k; ++i) {
        result = Math.min(result, dp[n - 1][i]);
    }

    return result;
}
'''

# 优化后
'''

'''