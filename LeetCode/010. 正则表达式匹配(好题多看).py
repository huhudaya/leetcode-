# 010. 正则表达式匹配.py
'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false

链接：https://leetcode-cn.com/problems/regular-expression-matching
'''

'''
我选择使用「备忘录」递归的方法来降低复杂度。
有了暴力解法，优化的过程及其简单，就是使用两个变量 i, j 记录当前匹配到的位置
从而避免使用子字符串切片，并且将 i, j 存入备忘录，避免重复计算即可。
'''

'''
第一步，我们暂时不管正则符号，如果是两个普通的字符串进行比较，如何进行匹配？我想这个算法应该谁都会写：
bool isMatch(string text, string pattern) {
    if (text.size() != pattern.size()) 
        return false;
    for (int j = 0; j < pattern.size(); j++) {
        if (pattern[j] != text[j])
            return false;
    }
    return true;
}



然后，我稍微改造一下上面的代码，略微复杂了一点，但意思还是一样的，很容易理解吧：
bool isMatch(string text, string pattern) {
    int i = 0; // text 的索引位置
    int j = 0; // pattern 的索引位置
    while (j < pattern.size()) {
        if (i >= text.size()) 
            return false;
        if (pattern[j++] != text[i++])
            return false;
    }
    // 相等则说明完成匹配
    return j == text.size();
}

如上改写，是为了将这个算法改造成递归算法（伪码）：
def isMatch(text, pattern) -> bool:
    if pattern is empty: return (text is empty?)
    first_match = (text not empty) and pattern[0] == text[0]
    return first_match and isMatch(text[1:], pattern[1:])


二、处理点号「.」通配符
点号可以匹配任意一个字符，万金油嘛，其实是最简单的，稍加改造即可：
def isMatch(text, pattern) -> bool:
    if not pattern: return not text
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    return first_match and isMatch(text[1:], pattern[1:])

三、处理「*」通配符
星号通配符可以让前一个字符重复任意次数，包括零次。那到底是重复几次呢？这似乎有点困难，不过不要着急，我们起码可以把框架的搭建再进一步：
def isMatch(text, pattern) -> bool:
    if not pattern: return not text
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    if len(pattern) >= 2 and pattern[1] == '*':
        # 发现 '*' 通配符
    else:
        return first_match and isMatch(text[1:], pattern[1:])


星号前面的那个字符到底要重复几次呢？这需要计算机暴力穷举来算，假设重复 N 次吧。前文多次强调过，写递归的技巧是管好当下，之后的事抛给递归。具体到这里，不管 N 是多少，当前的选择只有两个：匹配 0 次、匹配 1 次。所以可以这样处理：
if len(pattern) >= 2 and pattern[1] == '*':
    return isMatch(text, pattern[2:]) or \
            first_match and isMatch(text[1:], pattern)
# 解释：如果发现有字符和 '*' 结合，
    # 或者匹配该字符 0 次，然后跳过该字符和 '*'
    # 或者当 pattern[0] 和 text[0] 匹配后，移动 text


# 带备忘录的递归
def isMatch(text, pattern) -> bool:
    memo = dict() # 备忘录
    def dp(i, j):
        if (i, j) in memo: return memo[(i, j)]
        if j == len(pattern): return i == len(text)

        first = i < len(text) and pattern[j] in {text[i], '.'}

        if j <= len(pattern) - 2 and pattern[j + 1] == '*':
            ans = dp(i, j + 2) or \
                    first and dp(i + 1, j)
        else:
            ans = first and dp(i + 1, j + 1)

        memo[(i, j)] = ans
        return ans

    return dp(0, 0)

# 暴力递归
def isMatch(text, pattern) -> bool:
    if not pattern: return not text

    first = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return isMatch(text, pattern[2:]) or \
                first and isMatch(text[1:], pattern)
    else:
        return first and isMatch(text[1:], pattern[1:])
'''


# 备忘录
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp思想->备忘录
        memo = {}

        # 使用两个变量 i, j 记录当前匹配到的位置:  i表示字符串s,j表示匹配模式p
        def dp(i, j):
            if (i, j) in memo: return memo[(i, j)]
            if j == len(p): return i == len(s)
            # 这里必须是<len(s)
            first = i < len(s) and p[j] in {".", s[i]}
            if j <= len(p) - 2 and p[j + 1] == "*":
                # 或者当前匹配0次，则匹配模式前进两次，即忽略掉".*"
                # 或者当前匹配1次,则匹配模式串不动，字符串s前进一下
                ans = dp(i, j + 2) or (first and dp(i + 1, j))
            else:
                ans = first and dp(i + 1, j + 1)
            # 更新备忘录
            memo[(i, j)] = ans
            return ans

        return dp(0, 0)


'''
思路一（动态规划）:
解题思路：
按照动态规划的标准流程解题。

状态定义：

设动态规划网格 dp
dp[i][j] 代表字符串 s 中前 i 个字符和 p 中前 j 个字符是否匹配，值为 true 或 false。
记 s 第 i 个字符记为 s[m] == s[i - 1]；p 第 j 个字符记为 p[n] == p[j - 1]。
记 s 和 p 长度分别为 ls，lp。
初始状态：
行索引是 匹配串
列索引是 字符串
初始化第一行：dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'；
Tips: p 第 j 个字符记为 '*' 且 dp[0][j - 2] 为 True

转移方程：

1.当第 p[n] 为 '*' 时：
    1.	
        当 p[n-1]为 '.' 或 s[m] == p[n−1] 时:
            dp[i][j] = dp[i-1][j];
        Tips: 此两种情况代表 s[m]和 p[n−1] 可以匹配，等价于无 s[m] 的状态 dp[i-1][j];
    2.
        否则： 
            dp[i][j] = dp[i][j-2]；
    Tips: 此情况代表 s[m] 和 p[n−1] 无法匹配,p[n−1] p[n]p[n] 的组合必须出现 0 次，等价于没有 p[n-1] p[n] 时的状态 dp[i][j-2]；
2.否则
    1.
        当 p[n]为 '.' 或 s[m]==p[n] 时：
            dp[i][j] = dp[i-1][j-1]；
        Tips: 此情况代表 s[m] 和 p[n] 直接匹配，当前状态等价于未匹配此两字符前的状态 dp[i-1][j-1]。

返回值：
字符串 s 中前 ls 个字符和 p 中前 lp 个字符是否匹配，即：dp[ls][lp]。
复杂度分析：
时间复杂度 O(MN): 设 MM, NN 分别为 s,p 长度，即为填充整个动态规划网格 dpdp 所需时间。
空间复杂度 O(MN): 动态规划网格 dpdp 占用 O(MN) 的额外空间。

'''


# dp算法
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls, lp = len(s), len(p)
        # dp = [[False for _ in range(lp + 1)] for _ in range(ls + 1)]
        dp = [[False] * (lp + 1) for i in range(ls + 1)]
        dp[0][0] = True
        # base case 初始化第一行
        for j in range(2, lp + 1):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'
        for i in range(1, ls + 1):
            for j in range(1, lp + 1):
                m, n = i - 1, j - 1
                if p[n] == '*':
                    # 匹配1次
                    if s[m] == p[n - 1] or p[n - 1] == '.':
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                    # 匹配0次
                    else:
                        dp[i][j] = dp[i][j - 2]
                elif s[m] == p[n] or p[n] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[-1][-1]


'''
# 初始化条件，base case
s和p都为空""，一定为True：dp[0][0] = 1
s为空串""时dp[0][i+1]若要为True
只能是之前都为True，所以需要根据之前dp[0][i]是否匹配来判断
例如
p == '*'，s = 'a' 匹配；
p == '**'，s = 'a' 匹配；
p == 'c*'，s = 'a' 不匹配；
p == 'a*'，s = 'a' 匹配： 
    for i in range(len(p)): 
        if p[i] == '*': 
            dp[0][i + 1] = dp[0][i]

自底向上
直接上动态方程：

p[j] == s[i]:
    dp[i][j] = dp[i-1][j-1]

p[j] == ".":
    dp[i][j] = dp[i-1][j-1]

p[j] =="*":

    p[j-1] != s[i]:
        dp[i][j] = dp[i][j-2]

    p[i-1] == s[i] or p[j-1] == ".":

        dp[i][j] = dp[i-1][j] // 多个字符匹配的情况

        or dp[i][j] = dp[i][j-1] // 单个字符匹配的情况

        or dp[i][j] = dp[i][j-2] // 没有匹配的情况
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # if not s or not p:
        # return False
        s_len = len(s)
        p_len = len(p)
        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
        # print(dp)
        dp[0][0] = True
        for i in range(p_len):
            if p[i] == "*" and dp[0][i - 1]:
                dp[0][i + 1] = True
        # print(dp)
        for i in range(s_len):
            for j in range(p_len):
                if p[j] == s[i] or p[j] == ".":
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == "*":
                    # 匹配0次，前挪两格
                    if p[j - 1] != s[i]:
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    # 匹配1次
                    if p[j - 1] == s[i] or p[j - 1] == ".":
                        dp[i + 1][j + 1] = (dp[i][j + 1] or dp[i + 1][j] or dp[i + 1][j - 1])
        # print(dp)
        return dp[-1][-1]


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s) + 1  # 在字符串开头添加“@”，即s=“@”+s,"@"表示一个s和p都不存在的字符
        m = len(p) + 1  # 在模式串开头添加“@”，即p=“@”+p
        tb = [[False for j in range(n)] for i in range(m)]  # 初始化dp数组
        tb[0][0] = True  # 首行初始化，tb[0][1:]都为False。首列初始化可以放入循环中（加个条件）
        for i in range(1, m):
            for j in range(0, n):  # 从0开始就是为了初始化首列
                if p[i - 1] == "*":  # 循环中模式串当前字符为p[i-1], 字符串当前字符s[j-1]，因为开头添加了“@”，所以下标要减1
                    matched = j > 0 and (p[i - 2] == s[j - 1] or p[i - 2] == '.')  # j>0 用来首列初始化， 比较上一个模式串字符p[i-2]
                    tb[i][j] = tb[i - 2][j] or (
                            matched and tb[i][j - 1])  # tb[i-2][j]：使用0个模式字符，(tb[i][j-1] and matched) ：使用1-n个模式字符
                else:
                    matched = j > 0 and (p[i - 1] == s[j - 1] or p[i - 1] == '.')  # 比较当前模式串字符p[i-1]
                    tb[i][j] = matched and tb[i - 1][j - 1]  # 单个字符匹配
        return tb[m - 1][n - 1]


# aac
# .*
# true 
# 因为.*可以表示为...匹配aac
# 初始化dp
'''
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        # 第一行
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j-1] + 1
        # 第一列
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i-1][0] + 1
'''
# 特殊情况
# "" 和 ".*" 匹配，因为*可以匹配前面的字符0次
# "" 和 "." 不匹配


import pandas as pd
data = pd.DataFrame([12,3,3])
data_1 = data.set
