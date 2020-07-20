'''
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

示例:

输入: 13
输出: 6
解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。
通过次数8,684提交次数23,868

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-digit-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 字典序
'''
我们知道，如果对[1..n]的数组按照字典顺序排列，我们构建一棵字典树即可。

假设 n=205，我们需要计算 [1..205] 总共包含多少个1，问题就转化为：

计算 205 在字典树的第几层（假设为d+1）
计算 205 在第几棵字典树上（假设为m）
计算到第 d+1 层，第 m-1 棵字典树为止的 1 的个数
递归地计算 205 减去第m-1棵字典树的最大值所后，所包含1的个数
其中，第 n+1 层的字典树所包含的1的个数可以由以下递推式得到：

f[n+1] = 10^n + (f[1]+f[2]+..+f[n])*9
其中 f[1] = 1, 表示 1..9 中包含一个1.

注意，如果当前 n 的值以1开头，需要特殊处理一下，我们只计算字典树中一部分当前层的1的个数。
'''
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        if n < 10:
            return 1

        k = n
        d = 0
        while k >= 10:
            k /= 10
            d += 1
        dp = [0] * d
        dp[0] = 1
        for i in range(1, d):
            s = 1
            for j in range(1, i):
                s += dp[j]
            s = s * 9 + 10 ** i
            dp[i] = s

        prev_layer = sum(dp)
        prev_num = n - 10 ** d + 1 if k == 1 else (10 ** d + prev_layer * (k - 1))

        return prev_layer + prev_num + self.countDigitOne(n - k * (10 ** d))
