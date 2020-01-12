# 044. 通配符匹配.py
'''
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输入: false

链接：https://leetcode-cn.com/problems/wildcard-matching
'''


'''
做多了，你发现这种问题其实都是一个套路，老样子
我们还是根据我们要求解的问题去看和其直接相关的子问题
我们需要求解的问题是 pattern(0…m) 和 str(0…n) 是否匹配
这里的核心依然是字符之间的比较，但是和之前不同的是
这个比较不仅仅是看两个字符相不相等，它还有了一定的匹配规则在里面
那我们就依次枚举讨论下：
1.
	pattern(m) == str(n):
	问题拆解成看子问题 pattern(0...m-1) 和 str(0...n-1) 是否匹配
2.
	pattern(m) == ?:
	问题拆解成看子问题 pattern(0...m-1) 和 str(0...n-1) 是否匹配
3.	
	pattern(m) == *:
	* 可以匹配空串、以及任意多个字符
		当 * 匹配空串时：问题拆解成看子问题 pattern(0…m-1) 和 str(0…n) 是否匹配
		当 * 匹配任意字符时：问题拆解成看子问题 pattern(0…m) 和 str(0…n-1) 是否匹配
		总:
		这里解释一下，匹配任意多个字符意味着之前的子问题也可以使用当前的
		也就是用 pattern(m) 来进行匹配
		因此，当前问题可以拆解成子问题 pattern(0…m) 和 str(0…n-1) 是否匹配
你发现弄来弄去，子问题依然是那三个：

pattern(0…m-1) 和 str(0…n-1) 是否匹配

pattern(0…m-1) 和 str(0…n) 是否匹配

pattern(0…m) 和 str(0…n-1) 是否匹配



不知道你是否发现了字符匹配类动态规划问题的共性
如果是画表格，你只需要关注当前格子的 左边、上边、左上 这三个位置的相邻元素
因为表格有实际数据做辅助，所以画表格有时可以帮助你找到问题与子问题之间的联系。

状态定义

还是老样子，dp[i][j] 表示的就是问题 pattern(0…i) 和 str(0…j) 的答案
直接说就是 pattern(0…i) 和 str(0…j) 是否匹配

递推方程

把之前 “问题拆解” 中的文字描述转换成状态的表达式就是递推方程：

pattern(i) == str(j) || pattern(i) == '?':
    dp[i][j] = dp[i - 1][j - 1]

pattern(i) == '*':
    dp[i][j] = dp[i - 1][j] || dp[i][j - 1]


实现

这类问题的状态数组往往需要多开一格，主要是为了考虑空串的情况，这里我就不赘述了。

我想说的是，关于初始化的部分，如果 str 是空的，pattern 最前面有 *，因为 * 是可以匹配空串的，因此这个也需要记录一下
反过来，如果 pattern 是空的，str 只要不是空的就无法匹配，这里就不需要特别记录。
'''

# java
'''
public boolean isMatch(String s, String p) {
    char[] sArr = s.toCharArray();
    char[] pArr = p.toCharArray();

    boolean[][] dp = new boolean[pArr.length + 1][sArr.length + 1];
	# base case 
    dp[0][0] = true;
    for (int i = 1; i <= pArr.length; ++i) {
        if (pArr[i - 1] != '*') {
            break;
        } else {
            dp[i][0] = true;
        }
    }

    for (int i = 1; i <= pArr.length; ++i) {
        for (int j = 1; j <= sArr.length; ++j) {
            if (sArr[j - 1] == pArr[i - 1] || pArr[i - 1] == '?') {
                dp[i][j] = dp[i - 1][j - 1];
            } else if (pArr[i - 1] == '*') {
                dp[i][j] = dp[i - 1][j] || dp[i][j - 1];
            }
        }
    }

    return dp[pArr.length][sArr.length];
}

'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        pattern(i) == str(j) || pattern(i) == '?':
        dp[i][j] = dp[i - 1][j - 1]

        pattern(i) == '*':
        dp[i][j] = dp[i - 1][j] || dp[i][j - 1]
        '''
        sArr = list(s)
        pArr = list(p)
        m, n = len(s), len(p)
        # dp[i][j] 表示的就是问题 pattern(0…i) 和 str(0…j) 的答案
        # 直接说就是 pattern(0…i) 和 str(0…j) 是否匹配
        # 注意是从0开始的,即(0..i),联想到回文子序列问题!
        dp = [[False] * (m + 1) for i in range(n + 1)]
        # base case
        dp[0][0] = True
        for i in range(1,n+1):
            # 因为test是空串，pattern必须匹配空串，不满足时就break
            if p[i-1] != "*":
                break
            else:
                dp[i][0] = True
        # 注意这里的i和j不同于别的子序列问题，这里类似回文子序列问题，相当于是指针匹配到的位置
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[j - 1] == p[i - 1] or p[i - 1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[i - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[n][m]

'''
思路:
思路一: 利用两个指针进行遍历。

在代码里解释.

时间复杂度为:O(mn)

思路二: 动态规划

dp[i][j]表示s到i位置,p到j位置是否匹配!

初始化:

dp[0][0]:什么都没有,所以为true
第一行dp[0][j],换句话说,s为空,与p匹配,所以只要p开始为*才为true
第一列dp[i][0],当然全部为False
动态方程:

如果(s[i] == p[j] || p[j] == "?") && dp[i-1][j-1] ,有dp[i][j] = true

如果p[j] == "*" && (dp[i-1][j] = true || dp[i][j-1] = true) 有dp[i][j] = true

​ note:

​ dp[i][j-1],表示*代表是空字符,例如ab,ab*

​ dp[i-1][j],表示*代表非空任何字符,例如abcd,ab*
'''
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = 0
        j = 0
        start = -1
        match = 0
        while i < len(s):
            # 一对一匹配,匹配成功一起移
            if j < len(p) and (s[i] == p[j] or p[j] == "?"):
                i += 1
                j += 1
            # 记录p的"*"的位置,还有s的位置
            elif j < len(p) and p[j] == "*":
                start = j
                match = i
                j += 1
            # j 回到 记录的下一个位置
            # match 更新下一个位置
            # 这不代表用*匹配一个字符
            elif start != -1:
                j = start + 1
                match += 1
                i = match
            else:
                return False
         # 将多余的 * 直接匹配空串
        return all(x == "*" for x in p[j:])


# 动态规划
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        pattern(i) == str(j) || pattern(i) == '?':
        dp[i][j] = dp[i - 1][j - 1]

        pattern(i) == '*':
        dp[i][j] = dp[i - 1][j] || dp[i][j - 1]
        '''
        sArr = list(s)
        pArr = list(p)
        m, n = len(s), len(p)
        # dp[i][j] 表示的就是问题 pattern(0…i) 和 str(0…j) 的答案
        # 直接说就是 pattern(0…i) 和 str(0…j) 是否匹配 
        # 注意是从0开始的,即(0..i),联想到回文子序列问题!
        dp = [[False] * (m + 1) for i in range(n + 1)]
        # base case 
        dp[0][0] = True
        for i in range(1,n+1):
            # 因为test是空串，pattern必须匹配空串，不满足时就break
            if p[i-1] != "*":
                break
            else:
                dp[i][0] = True
        # 注意这里的i和j不同于别的子序列问题，这里类似回文子序列问题，相当于是指针匹配到的位置
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[j - 1] == p[i - 1] or p[i - 1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[i - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[n][m]



# dp
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sn = len(s)
        pn = len(p)
        dp = [[False] * (pn + 1) for _ in range(sn + 1)]
        dp[0][0] = True
        # base case 处理边界问题
        for j in range(1, pn + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]

        for i in range(1, sn + 1):
            for j in range(1, pn + 1):
                if (s[i - 1] == p[j - 1] or p[j - 1] == "?"):
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]

