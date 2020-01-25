'''
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释:
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

链接：https://leetcode-cn.com/problems/edit-distance
'''
# 编辑距离.py
# https://mp.weixin.qq.com/s/4CrUawZtiD9ZQohKBgAx4Q
'''
	给定两个字符串s1和s2
	计算出将s1转换成s2的最少操作数
	你可以对一个字符串进行如下操作:
		插入
		删除
		替换
	示例:
		输入 s1 = 'horse' s2='ros'
		输出 3
		horse ->rorse (h->r)
		rorse->rose(删除r)
		rose->ros(删除e)
'''
'''
为什么说这个问题难呢，因为显而易见，它就是难，让人手足无措，望而生畏。

为什么说它实用呢，因为前几天我就在日常生活中用到了这个算法。之前有一篇公众号文章由于疏忽，写错位了一段内容，我决定修改这部分内容让逻辑通顺。但是公众号文章最多只能修改 20 个字，且只支持增、删、替换操作（跟编辑距离问题一模一样），于是我就用算法求出了一个最优方案，只用了 16 步就完成了修改。

再比如高大上一点的应用，DNA 序列是由 A,G,C,T 组成的序列，可以类比成字符串。编辑距离可以衡量两个 DNA 序列的相似度，编辑距离越小，说明这两段 DNA 越相似，说不定这俩 DNA 的主人是远古近亲啥的。

下面言归正传，详细讲解一下编辑距离该怎么算，相信本文会让你有收获
'''
'''
编辑距离问题就是给我们两个字符串s1和s2，只能用三种操作，让我们把s1变成s2，求最少的操作数。
需要明确的是，不管是把s1变成s2还是反过来，结果都是一样的，所以后文就以s1变成s2举例。

前文 最长公共子序列 说过，解决两个字符串的动态规划问题，一般都是用两个指针i,j分别指向两个字符串的最后，然后一步步往前走，缩小问题的规模。
'''


def minDistance(s1, s2) -> int:
    def dp(i, j):
        # base case
        if i == -1:
            # 插入剩下的j即可
            return j + 1
        if j == -1:
            # 删除剩下的i即可
            return i + 1
        if s1[i] == s2[j]:
            # 什么也不做
            return dp(i - 1, j - 1)
        else:
            return min(
                dp(i, j - 1) + 1,  # 插入
                dp(i - 1, j - 1) + 1,  # 替换
                dp(i - 1, j) + 1  # 删除
            )

    return dp(len(s1) - 1, len(s2) - 1)


'''
都说递归代码的可解释性很好，这是有道理的，只要理解函数的定义，就能很清楚地理解算法的逻辑。我们这里 dp(i, j) 函数的定义是这样的：

def dp(i, j) -> int
# 返回 s1[0..i] 和 s2[0..j] 的最小编辑距离
'''

'''
dp[i][j]的含义和之前的 dp 函数类似：

def dp(i, j) -> int
# 返回 s1[0..i] 和 s2[0..j] 的最小编辑距离

dp[i-1][j-1]
# 存储 s1[0..i] 和 s2[0..j] 的最小编辑距离
有了之前递归解法的铺垫，应该很容易理解。dp 函数的 base case 是i,j等于 -1，而数组索引至少是 0，所以 dp 数组会偏移一位，dp[..][0]和dp[0][..]对应 base case。。

既然 dp 数组和递归 dp 函数含义一样，也就可以直接套用之前的思路写代码，唯一不同的是，DP table 是自底向上求解，递归解法是自顶向下求解：
'''
'''
# 备忘录算法
	def minDistance(s1, s2) -> int:

    memo = dict() # 备忘录
    def dp(i, j):
        if (i, j) in memo: 
            return memo[(i, j)]
        ...

        if s1[i] == s2[j]:
            memo[(i, j)] = ...  
        else:
            memo[(i, j)] = ...
        return memo[(i, j)]

    return dp(len(s1) - 1, len(s2) - 1)
'''


# dp思想
# s1是对应i
# s2d
def minDistance(s1, s2) -> int:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    # dp = [0 for i in range(m+1) for j in range(n+1)]
    for i in range(m + 1):
        dp[i][0] = i
    for i in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i - 1], dp[j - 1] + 1
                )
    return dp[m][n]
