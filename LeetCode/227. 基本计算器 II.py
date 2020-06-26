'''

实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:

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
'''
那么，为什么说处理括号没有看起来那么难呢，因为括号具有递归性质。我们拿字符串3*(4-5/2)-6举例：
calculate(3*(4-5/2)-6)
= 3 * calculate(4-5/2) - 6
= 3 * 2 - 6
= 0
可以脑补一下，无论多少层括号嵌套，通过 calculate 函数递归调用自己，都可以将括号中的算式化简成一个数字。换句话说，括号包含的算式，我们直接视为一个数字就行了。
现在的问题是，递归的开始条件和结束条件是什么？遇到(开始递归，遇到)结束递归：
'''
from typing import List
def calculate(s: str) -> int:

    def helper(s: List) -> int:
        stack = []
        sign = '+'
        num = 0

        while len(s) > 0:
            c = s.pop(0)
            if c.isdigit():
                num = 10 * num + int(c)
            # 遇到左括号开始递归计算 num
            if c == '(':
                num = helper(s)
            # 当c不是数字或者遍历到了尽头，就执行入栈的操作
            if (not c.isdigit() and c != ' ') or len(s) == 0:
                if sign == '+': ...
                elif sign == '-': ...
                elif sign == '*': ...
                elif sign == '/': ...
                num = 0
                sign = c
            # 遇到右括号返回递归结果
            if c == ')': break
        return sum(stack)

    return helper(list(s))



# 自己的版本,注意需要使用deque,否则自带的list的效率很低
from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        s = deque(s)
        def helper(s) -> int:
            stack = []
            sign = "+"
            num = 0
            while len(s) > 0:
                # 注意这里是pop(0)!!!!，pop最左边的数据
                c = s.popleft()
                if c.isdigit():
                    num = num * 10 + int(c)
                # 当c不是数字或者遍历到了尽头，就执行入栈的操作
                if (not c.isdigit() and c != ' ') or len(s) == 0:
                    # 判断之前的sign标志位
                    if sign == "+":
                        stack.append(num)
                    elif sign == "-":
                        stack.append(-num)
                    # 如果遇见乘除法，需要弹出栈顶的元素先进行一次运算操作
                    elif sign == "*":
                        stack.append(stack.pop() * num)
                        # stack[-1] = stack[-1] * num
                    elif sign == "/":
                        stack[-1] = int(stack[-1] / float(num))
                    num = 0
                    sign = c
            return sum(stack)
        return helper(s)