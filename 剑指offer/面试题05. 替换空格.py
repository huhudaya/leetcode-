'''
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

 

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."
 

限制：

0 <= s 的长度 <= 10000

链接：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof
'''


class Solution:
    def replaceSpace(self, s: str) -> str:
        s1 = []                         # 设列表
        for cha in s:                   # 遍历字符串
            if cha == ' ':              # 如果是空格，就在列表后面添加%20
                s1.append('%20')
            else:                       # 如果不是空格，就在列表后面原样添加
                s1.append(cha)
        return ''.join(s1)              # 把列表转为str

class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')
