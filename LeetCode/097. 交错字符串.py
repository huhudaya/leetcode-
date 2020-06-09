# 097. 交错字符串.py
'''
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false

链接：https://leetcode-cn.com/problems/interleaving-string
'''
'''
题目的输入是三个字符串，问其中两个字符串是否能够交错合并组成第三个字符串，一个字符相对于其他字符的顺序在合并之后不能改变，这也是这道题的难点，不然的话你用一个哈希表就可以做了，三个字符串是否意味着要开三维的状态数组？还是四个步骤来看看：

问题拆解

在拆解问题之前，我们必须保证前两个字符串的字符的总数量必须正好等于第三个字符串的字符总数量
不然的话，再怎么合并也无法完全等同。这里有一个点，当我们考虑 str1(0…i) 和 str2(0…j) 的时候
其实第三个字串需要考虑的范围也就确定了，就是 str3(0…i+j)。
如果我们要求解问题 str1(0…m) 和 str2(0…n) 是否能够交错组成 str3(0…m+n)
还是之前那句话，字符串匹配问题的核心永远是字符之间的比较：

如果 str1(m) == str3(m+n)，问题拆解成考虑子问题 str1(0…m-1) 和 str2(0…n) 是否能够交错组成 str3(0…m+n-1)

如果 str2(n) == str3(m+n)，问题拆解成考虑子问题 str1(0…m) 和 str2(0…n-1) 是否能够交错组成 str3(0…m+n-1)

你可能会问需不需要考虑子问题 str1(0…m-1) 和 str2(0…n-1)？

在这道题目当中，不需要！

千万不要题目做多了就固定思维了，之前说到这类问题可以试着考虑三个相邻子问题是为了让你有个思路，能更好地切题，并不是说所有的字符串匹配问题都需要考虑这三个子问题，我们需要遇到具体问题具体分析。

状态定义

dp[i][j] 表示的是 str1(0…i) 和 str2(0…j) 是否可以交错组成 str3(0…i+j)
这里再补充说明下为什么我们不需要开多一维状态来表示 str3，其实很简单，str3 的状态是由 str1 str2 决定的
str1 str2 定了，str3 就定了

递推方程

把之前问题拆解中的文字描述转换成状态的表达式就是递推方程：

str1(i) == str3(i+j)
dp[i][j] |= dp[i - 1][j]

str2(j) == str3(i+j)
dp[i][j] |= dp[i - 1][j]
实现

初始化的时候需要考虑单个字符串能否组成 str3 对应的区间，这个比较简单，直接判断前缀是否相等即可。
'''
# dp[i][j] 表示的是 str1(0…i) 和 str2(0…j) 是否可以交错组成 str3(0…i+j)
# s_{1}s 
# s1的前i个字符和s2的前j个字符是否能构成s3的前i+j个字符
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1=len(s1)
        len2=len(s2)
        len3=len(s3)
        if(len1 + len2 != len3):
            return False
        dp=[[False]*(len2+1) for i in range(len1+1)]
        dp[0][0]=True
        # 初始化第一列，dp[i][0], 表示s1的前i位是否构成s3的前i位：前i-1位可以构成s3的前i-1位且s1的第i位s1[i-1]等于s3的第i位s3[i-1]
        for i in range(1,len1+1):
            dp[i][0] = (dp[i - 1][0] and s1[i - 1] == s3[i - 1])
        # 初始化第一行，dp[0][j], 表示s2的前j位是否能构成s3的前j位
        for i in range(1,len2+1):
            dp[0][i]=(dp[0][i - 1] and s2[i-1] == s3[i - 1])

        for i in range(1,len1+1):
            for j in range(1,len2+1):
                dp[i][j]=(dp[i][j-1] and s2[j-1]==s3[i+j-1]) or (dp[i-1][j] and s1[i-1]==s3[i+j-1])
        return dp[-1][-1]
'''
public boolean isInterleave(String s1, String s2, String s3) {
    int length1 = s1.length();
    int length2 = s2.length();
    int length3 = s3.length();

    if (length1 + length2 != length3) {
        return false;
    }

    boolean[][] dp = new boolean[length1 + 1][length2 + 1];

    dp[0][0] = true;
    char[] sArr1 = s1.toCharArray();
    char[] sArr2 = s2.toCharArray();
    char[] sArr3 = s3.toCharArray();
    for (int i = 1; i <= length1; ++i) {
        dp[i][0] = dp[i - 1][0] && sArr1[i - 1] == sArr3[i - 1];
    }
    for (int i = 1; i <= length2; ++i) {
        dp[0][i] = dp[0][i - 1] && sArr2[i - 1] == sArr3[i - 1];
    }
    for (int i = 1; i <= length1; ++i) {
        for (int j = 1; j <= length2; ++j) {
            if (sArr3[i + j - 1] == sArr1[i - 1]) {
                dp[i][j] |= dp[i - 1][j];
            } 
            if (sArr3[i + j - 1] == sArr2[j - 1]) {
                dp[i][j] |= dp[i][j - 1];
            }
        }
    }
    return dp[length1][length2];
}
'''


# 使用装饰器
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        import functools
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        @functools.lru_cache(None)
        def helper(i, j, k):
            if i == n1 and j == n2 and k == n3:
                return True
            if i < n1 and j < n2 and k < n3 and s1[i] == s2[j] == s3[k]:
                if helper(i + 1, j, k + 1) or helper(i, j + 1, k + 1):
                    return True
            elif i < n1 and k < n3 and s1[i] == s3[k]:
                if helper(i + 1, j, k + 1):
                    return True
            elif j < n2 and k < n3 and s2[j] == s3[k]:
                if helper(i, j + 1, k + 1):
                    return True
            return False
        return helper(0, 0, 0)