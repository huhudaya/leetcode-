'''
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例：
输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"

提示：
在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
'''

# 手写split和reverse函数
class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        res = []

        def split(s, char):
            s += char
            fast = 0
            slow = 0
            res = []
            for i in s:
                if i == char:
                    res.append(s[slow:fast])
                    slow = fast + 1
                fast += 1
            return res

        def reverse(s):
            s = list(s)
            n = len(s)
            left = 0
            right = n - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            return "".join(s)

        s = split(s, " ")
        for i in s:
            res.append("".join(reverse(i)))
        return " ".join(res)

# 简洁版
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(i[::-1] for i in s.split())

# c++
'''
class Solution {
public: 
    string reverseWords(string s) {
        int length = s.length();
        int i = 0;
        while (i < length) {
            int start = i;
            while (i < length && s[i] != ' ') {
                i++;
            }

            int left = start, right = i - 1;
            while (left < right) {
                swap(s[left], s[right]);
                left++;
                right--;
            }
            while (i < length && s[i] == ' ') {
                i++;
            }
        }
        return s;
    }
};
'''

# java
'''
class Solution {
    public String reverseWords(String s) {
	String[] strs = s.split(" ");
	StringBuffer buffer = new StringBuffer();
	for (int i = 0; i < strs.length; i++) {
		buffer.append(new StringBuffer(strs[i]).reverse().toString());
		buffer.append(" ");
	}
	return buffer.toString().trim();
    }
}
'''