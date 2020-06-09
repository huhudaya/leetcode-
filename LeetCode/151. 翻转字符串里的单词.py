'''
给定一个字符串，逐个翻转字符串中的每个单词。

 

示例 1：

输入: "the sky is blue"
输出: "blue is sky the"
示例 2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
说明：
无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

进阶：
请选用 C 语言的用户尝试使用 O(1) 额外空间复杂度的原地解法。
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        res = " ".join(list(reversed(s.split())))
        return res


class Solution:
    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        # 去掉字符串开头的空白字符
        while left <= right and s[left] == ' ':
            left += 1

        # 去掉字符串末尾的空白字符
        while left <= right and s[right] == ' ':
            right -= 1

        # 将字符串间多余的空白字符去除
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1

        return output

    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0

        while start < n:
            # 循环至单词的末尾
            while end < n and l[end] != ' ':
                end += 1
            # 翻转单词
            self.reverse(l, start, end - 1)
            # 更新start，去找下一个单词
            start = end + 1
            end += 1

    def reverseWords(self, s: str) -> str:
        l = self.trim_spaces(s)

        # 翻转字符串
        self.reverse(l, 0, len(l) - 1)

        # 翻转每个单词
        self.reverse_each_word(l)

        return ''.join(l)



# class Solution:
#     def reverseWords(self, s: str) -> str:
#         s = s.strip()
#         res = " ".join(list(reversed(s.split())))
#         return res
class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        s = s.strip()
        n = len(s)
        # 去掉中间多余的空格
        for i in range(n):
            if s[i] != " ":
                res += s[i]
            elif res[-1] != " ":
                res += s[i]
        def splitFun(str,char):
            output = []
            slow = 0
            fast = 0
            str += char
            for i in str:
                if i == char:
                    output.append(res[slow:fast])
                    slow = fast + 1
                fast += 1
            return output
        res = splitFun(res, " ")
        res = " ".join(reversed(res))
        return res