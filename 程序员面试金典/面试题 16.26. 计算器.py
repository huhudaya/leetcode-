'''
给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。

表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:

输入: "3+2*2"
输出: 7
示例 2:

输入: " 3/2 "
输出: 1
示例 3:

输入: " 3+5 / 2 "
输出: 5
说明：
你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。
'''
from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        s = deque(s)
        n = len(s)
        num = 0
        sign = "+"
        stack = []
        for i in range(n):
            char = s.popleft()
            if char.isdigit():
                num = num * 10 + int(char)
            if char == "(":
                num = self.calculate(s)
            if (char != " " and char != "(" and not char.isdigit()) or len(s) == 0:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = char
            if char == ")":
                break
        return sum(stack)