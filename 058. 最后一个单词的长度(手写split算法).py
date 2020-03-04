'''
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。
如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
如果不存在最后一个单词，请返回 0 。

说明：一个单词是指仅由字母组成、不包含任何空格的 最大子字符串。
示例:
输入: "Hello World"
输出: 5
'''

'''
先去掉字符串的最后空格
将字符串按照空格分组
取分组后的最后一项
计算它的长度
'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(" ")[-1])


'''
直接找最后一个单词

先找最后一个单词最后一个字母

再找最后一个单词第一个字母
'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1
        while end >= 0 and s[end] == " ":
            end -= 1
        if end == -1: return 0
        start = end
        while start >= 0 and s[start] != " ":
            start -= 1
        return end - start


# 自己编写split算法
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 想到最好的方式就是直接split,但是直接用库函数良心过不去
        # 自己编写一个split算法吧。。。
        # 去掉最后面的空格，很简单，就不写了，直接用库吧
        s = s.rstrip()

        def splitFun(str, char):
            res = []
            slow = 0
            fast = 0
            str += char
            # 快慢指针
            for i in str:
                if i == char:
                    res.append(str[slow:fast])
                    slow = fast + 1
                fast += 1
            return res

        res = len(splitFun(s, " ")[-1])
        return res
