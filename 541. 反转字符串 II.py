# 541. 反转字符串 II.py
'''
给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。
如果剩余少于 k 个字符，则将剩余的所有全部反转,如果有小于 2k 但大于或等于 k 个字符.
则反转前 k 个字符，并将剩余的字符保持原样

示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"
要求:

该字符串只包含小写的英文字母。
给定字符串的长度和 k 在[1, 10000]范围内。
链接：https://leetcode-cn.com/problems/reverse-string-ii
'''
# 其实就是每隔k个反转
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # python利用切片
        # 本题题意其实相当于每隔k个元素然后以k个元素进行反转
        a = list(s)
        for i in range(0, len(a), 2*k):
            # 切片的时候不怕越界
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)



# java
'''
class Solution {
    public String reverseStr(String s, int k) {
        char[] a = s.toCharArray();
        for (int start = 0; start < a.length; start += 2 * k) {
            int i = start, j = Math.min(start + k - 1, a.length - 1);
            while (i < j) {
                char tmp = a[i];
                a[i++] = a[j];
                a[j--] = tmp;
            }
        }
        return new String(a);
    }
}
'''

for i in range(0,7,4):
	print(i)