'''

对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。

返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。



示例 1：

输入：str1 = "ABCABC", str2 = "ABC"
输出："ABC"
示例 2：

输入：str1 = "ABABAB", str2 = "ABAB"
输出："AB"
示例 3：

输入：str1 = "LEET", str2 = "CODE"
输出：""


提示：

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] 和 str2[i] 为大写英文字母
'''


# 枚举法
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(min(len(str1), len(str2)), 0, -1):
            if (len(str1) % i) == 0 and (len(str2) % i) == 0:
                if str1[: i] * (len(str1) // i) == str1 and str1[: i] * (len(str2) // i) == str2:
                    return str1[: i]
        return ''


# 枚举优化
'''
方法二：枚举优化
思路

注意到一个性质：如果存在一个符合要求的字符串 X
那么也一定存在一个符合要求的字符串 X'，它的长度为 str1 和 str2 长度的最大公约数
最大公约数为gcd(x1, x2)



解法2证明：
证：如果存在最大公约串，则其的长度必然等于两母串长度的最大公约数
证明：
  反证：如果存在最大公约串sub的长度不等于两串长度的最大公约数gcd ①成立则上述规律不成立
  那么gcd必然大于sub长度,否则sub的长度就是gcd，即sub长度小于gcd
  如果sub长度小于gcd，而且sub又是公约串
  那么sub必然是长度为gcd的串gsub的公约串
  那么gsub是比sub更长的公约串
  那么gsub才是最大公约串，与①不符
  反证不成立，得证
'''
import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # gcd算法需要O（logN）
        candidate_len = math.gcd(len(str1), len(str2))
        candidate = str1[: candidate_len]
        if candidate * (len(str1) // candidate_len) == str1 and candidate * (len(str2) // candidate_len) == str2:
            return candidate
        return ''