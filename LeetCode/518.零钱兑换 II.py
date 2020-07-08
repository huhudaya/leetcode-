'''
给定不同面额的硬币和一个总金额。
写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 
示例 1:
输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
示例 2:
输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。
示例 3:
输入: amount = 10, coins = [10]
输出: 1
注意:
你可以假设：
0 <= amount (总金额) <= 5000
1 <= coin (硬币面额) <= 5000
硬币种类不超过 500 种
结果符合 32 位符号整数
'''
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        '''
        第二步要明确dp数组的定义。
        首先看看刚才找到的「状态」，有两个，也就是说我们需要一个二维dp数组。
        dp[i][j]的定义如下：
        若只使用前i个物品，当背包容量为j时，有dp[i][j]种方法可以装满背包。
        换句话说，翻译回我们题目的意思就是：
        若只使用coins中的前i个硬币的面值，若想凑出金额j，有dp[i][j]种凑法。
        '''
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        # 相当于nums数组在外循环
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] >= 0:
                    # 注意这里和0/1背包的区别，完全背包中的元素是可以重复利用的，所以这里不用算dp[i-1],用dp[i]就可以
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][amount]

print(Solution().change(4, [1,2,3]))
# 3

class Solution:
    # 状态未压缩
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        '''
        第二步要明确dp数组的定义。
        首先看看刚才找到的「状态」，有两个，也就是说我们需要一个二维dp数组。
        dp[i][j]的定义如下：
        若只使用前i个物品，当背包容量为j时，有dp[i][j]种方法可以装满背包。
        '''
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] >= 0:
                    # 不同于01背包问题，这里物品是可以无限选择的，所以如果这次选择了这个物品，上一个状态也可以选择这个物品的
                    # 这个信息体现在当使用压缩的滚动数组后，可以从前向后，不用非得从后向前
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][amount]

    # 状态压缩
    def change2(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for i in range(n):
            for j in range(1, amount + 1):
                if j - coins[i] >= 0:
                    # 因为i是从0开始的，所以不用coins[i-1]
                    dp[j] = dp[j] + dp[j - coins[i]]
        print(dp)
        return dp[amount]




# 可以使用的一个模板，注意，因为反正加的都是同一行的左边，所以不用倒序就可以了
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[amount]


# 回溯
'''
import java.util.Arrays;

public class Solution {

    // 该解法超时，问题规模小的时候可用

    private int res = 0;

    public int change(int amount, int[] coins) {
        int len = coins.length;
        Arrays.sort(coins);

        backtracking(amount, coins, 0, len);
        return res;
    }

    private void backtracking(int residue, int[] coins, int start, int len) {
        if (residue == 0) {
            res++;
            return;
        }

        for (int i = start; i < len; i++) {
            if (residue - coins[i] < 0) {
                break;
            }
            backtracking(residue - coins[i], coins, i, len);
        }
    }
}
'''
