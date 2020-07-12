'''

给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。

表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

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
# 逆波兰表达式
class Solution:
    def calculate(self, s: str) -> int:
        def postfix_expression(exp: str):
            exp = exp.replace("+", " + ").replace("-", " - ").replace("/", " / ").replace("*", " * ")
            exp = exp.split()
            op = []
            ret = []
            for e in exp:
                if e.isdigit():
                    ret.append(e)
                else:
                    if e in "+-":
                        while op:
                            ret.append(op.pop())
                        op.append(e)
                    elif e in {"*", "/"}:
                        while op and op[-1] in {"*", "/"}:
                            ret.append(op.pop())
                        op.append(e)
            return ret + op[::-1]

        expression = postfix_expression(s)
        res = []
        for i in expression:
            if i.isdigit():
                res.append(int(i))
            else:
                sec = res.pop()
                fir = res.pop()
                if i == "+": res.append(fir + sec)
                if i == "-": res.append(fir - sec)
                if i == "*": res.append(fir * sec)
                if i == "/": res.append(fir // sec)
        return res[0]


import math
class Solution:
    def calculate(self, s: str) -> int:
        s = list(s)
        sign = "+"
        num = 0
        res = []
        while len(s) > 0:
            str = s.pop(0)
            if str.isdigit():
                num = num * 10 + int(str)
            elif str == "(":
                self.calculate(s)
            if (not str.isdigit() and str != " ") or len(s) == 0:
                if sign == "+":
                    res.append(num)
                elif sign == "-":
                    res.append(-num)
                elif sign == "*":
                    res.append(res.pop() * num)
                elif sign == "/":
                    if res[-1] < 0:
                        res.append(math.ceil(res.pop() / num))
                    else:
                        res[-1] = (res[-1] // num)
                sign = str
                num = 0
            elif str == ")":
                return
        return sum(res)

# java
'''
    public int calculate(String s) {

        Stack<Integer> stack = new Stack<>();
        char opt = '+';
        int num = 0;

        for (int i = 0; i < s.length(); i++) {

            char ch = s.charAt(i);

            if (Character.isDigit(ch))
                num = num * 10 + (ch - '0');

            if ((!Character.isDigit(ch) && ch != ' ') || i == s.length() - 1) {

                if (opt == '+')
                    stack.push(num);
                else if (opt == '-')
                    stack.push(-num);
                else if (opt == '*') 
                    stack.push(stack.pop() * num);
                else    
                    stack.push(stack.pop() / num);
                
                num = 0;
                opt = ch;
            }
        }

        int res = 0;
        while (!stack.isEmpty())
            res += stack.pop();
        
        return res;
    }
'''