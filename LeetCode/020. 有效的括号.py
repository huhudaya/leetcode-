# 20. 有效的括号.py
'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

链接：https://leetcode-cn.com/problems/valid-parentheses
'''


class Solution:
    def isValid(self, s: str) -> bool:
        # 用栈
        stack = []
        tmp = "[{("
        # n = len(s)
        for char in s:
            if char in tmp:
                stack.append(char)
            else:
                if stack and self.helper(stack[-1], char):
                    stack.pop()
                else:
                    return False
        return not stack

    def helper(self, ch1, ch2):
        opens = "([{"
        closers = ")]}"
        return opens.index(ch1) == closers.index(ch2)


class Solution:
    def isValid(self, s: str) -> bool:
        def check(s1, s2):
            op1 = "([{"
            op2 = ")]}"
            return op1.index(s1) == op2.index(s2)

        op1 = set()
        op1.add("{")
        op1.add("(")
        op1.add("[")
        stack = []
        for i in s:
            if i in op1:
                stack.append(i)
            elif stack:
                if not check(stack.pop(), i):
                    return False
            else:
                return False
        return stack == []
