'''
给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

示例 1:
输入: "aacecaaa"
输出: "aaacecaaa"

示例 2:
输入: "abcd"
输出: "dcbabcd"
'''
# 暴力法
# 先逆序，然后截取逆序后的前i个字符拼接到原串上，取满足回文条件最小的i
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 0:
            return ""
        rs = s[::-1]
        i = 0
        while True:
            if rs[i:] == s[:length - i]:
                break
            i += 1
        return rs[:i] + s

# java
'''
public String shortestPalindrome(String s) {
    String r = new StringBuilder(s).reverse().toString();
    int n = s.length();
    int i = 0;
    for (; i < n; i++) {
        if (s.substring(0, n - i).equals(r.substring(i))) {
            break;
        }
    }
    return new StringBuilder(s.substring(n - i)).reverse() + s;
}
'''