'''
实现一个基本的计算器来计算一个简单的字符串表达式的值。
字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。
示例 1:
输入: "1 + 1"
输出: 2
示例 2:

输入: " 2-1 + 2 "
输出: 3
示例 3:

输入: "(1+(4+5+2)-3)+(6+8)"
输出: 23
说明：
你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。
'''
'''
怎么把一个字符串形式的正整数，转化成 int 型？

string s = "458";

int n = 0;
for (int i = 0; i < s.size(); i++) {
    char c = s[i];
    n = 10 * n + (c - '0');
}
// n 现在就等于 458
这个还是很简单的吧，老套路了。但是即便这么简单，依然有坑：(c - '0')的这个括号不能省略，否则可能造成整型溢出。

因为变量c是一个 ASCII 码，如果不加括号就会先加后减，想象一下n如果接近 INT_MAX，就会溢出。所以用括号保证先减后加才行。
'''
'''
int calculate(string s) {
    stack<int> stk;
    // 记录算式中的数字
    int num = 0;
    // 记录 num 前的符号，初始化为 +
    char sign = '+';
    for (int i = 0; i < s.size(); i++) {
        char c = s[i];
        // 如果是数字，连续读取到 num
        if (isdigit(c)) 
            num = 10 * num + (c - '0');
        // 如果不是数字，就是遇到了下一个符号，
        // 之前的数字和符号就要存进栈中
        if (!isdigit(c) || i == s.size() - 1) {
            switch (sign) {
                case '+':
                    stk.push(num); break;
                case '-':
                    stk.push(-num); break;
            }
            // 更新符号为当前符号，数字清零
            sign = c;
            num = 0;
        }
    }
    // 将栈中所有结果求和就是答案
    int res = 0;
    while (!stk.empty()) {
        res += stk.top();
        stk.pop();
    }
    return res;
}
'''
'''
(A + B)* C 的情况会是什么样呢？ 回想一下， A B + C * 是等价的后缀表达式。
从左到右处 理此中缀表达式，我们先看到 + 。 
在这种情况下，当我们看到 * ， + 已经放置在结果表达 式中，由于括号它的优先级高于 * 。 
我们现在可以开始看看转换算法如何工作。当我们看到 左括号时，我们保存它，表示高优先级的另一个运算符将出现。
该操作符需要等到相应的右 括号出现以表示其位置（回忆完全括号的算法）。 
当右括号出现时，可以从栈中弹出操作 符。
当我们从左到右扫描中缀表达式时，我们将使用栈来保留运算符。
这将提供我们在第一个例 子中注意到的反转。 堆栈的顶部将始终是最近保存的运算符。
每当我们读取一个新的运算符 时，我们需要考虑该运算符如何与已经在栈上的运算符（如果有的话）比较优先级。 
假设中缀表达式是一个由空格分隔的标记字符串。 操作符标记是 *，/，+ 和 - ，以及左右括 号。
操作数是单字符 A，B，C 等。 以下步骤将后缀顺序生成一个字符串。 
1. 创建一个名为 opstack 的空栈以保存运算符。给输出创建一个空列表。 
2. 通过使用字符串方法拆分将输入的中缀字符串转换为标记列表。
3. 从左到右扫描标记列表。 
    如果标记是操作数，将其附加到输出列表的末尾。 
    如果标记是左括号，将其压到 opstack 上。 
    如果标记是右括号，则弹出 opstack，直到删除相应的左括号。
    将每个运算符附加到 输出列表的末尾。 
    如果标记是运算符， *，/，+ 或 - ，将其压入 opstack。
    但是，首先删除已经在 opstack 中具有更高或相等优先级的任何运算符，并将它们加到输出列表中。 
4. 当输入表达式被完全处理时，检查 opstack。仍然在栈上的任何运算符都可以删除并加到 输出列表的末尾。
'''
# 中缀表达式转后缀表达式
from pythonds.basic.stack import Stack
def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        print(opStack.peek())
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("A + B * C"))
# print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
# 后缀表达式求值
'''
7 8 + 3 2 + / 
在这个例子中有两点需要注意
首先，栈 的大小增长收缩，然后再子表达式求值的时候再次增长
第二，除法操作需要自信处理。回想下，后缀表达式的操作符顺序没变，仅仅改变操作符的位置。
当用于除法的操作符从栈中 弹出时，它们被反转。
由于除法不是交换运算符，换句话说 15/5 和 5/15 不同
因此我们必须保证操作数的顺序不会交换。

假设后缀表达式是一个由空格分隔的标记字符串。 运算符为 *，/，+ 和 - ，操作数假定为单 个整数值。 输出将是一个整数结果。
1. 创建一个名为 operandStack 的空栈。
2. 拆分字符串转换为标记列表。
3. 从左到右扫描标记列表。
    如果标记是操作数，将其从字符串转换为整数，并将值压到operandStack。
    如果标记是运算符 *，/，+ 或 - ，它将需要两个操作数。弹出operandStack 两次。 第一个弹出的是第二个操作数，第二个弹出的是第一个操作数。执行算术运算后， 将结果压到操作数栈中。
4. 当输入的表达式被完全处理后，结果就在栈上，弹出 operandStack 并返回值。
'''
from pythonds.basic.stack import Stack
def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
        return operandStack.pop()
def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
print(postfixEval('7 8 + 3 2 + /'))


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
            # 当c不是数字或者遍历到了尽头，就执行入栈的操作
            if (not c.isdigit() and c != ' ') or len(s) == 0:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    # python 除法向 0 取整的写法
                    stack[-1] = int(stack[-1] / float(num))
                num = 0
                sign = c

        return sum(stack)
    # 需要把字符串转成列表方便操作
    return helper(list(s))

# 自己的版本
from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        sDeque = deque(s)
        def helper(sDeque) -> int:
            num = 0
            sign = "+"
            stack = []
            while len(sDeque) > 0:
                # 注意 这里需要从头部开始pop
                char = sDeque.popleft()
                if char.isdigit():
                    # 如果遇见345 + 23，这个时候需要进行((0*10+5)*10+4)*10+3
                    num = num * 10 + int(char)
                if char == '(':
                    num = helper(sDeque)
                if (not char.isdigit() and char != " ") or len(sDeque) == 0:
                    if sign == "+":
                        stack.append(num)
                    elif sign == "-":
                        stack.append(-num)
                    # 重置num和sign
                    num = 0
                    sign = char
                if char == ")":
                    break
            return sum(stack)
        return helper(sDeque)

# 官方题解 好办法啊！！！！
class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        operand = 0
        res = 0 # For the on-going result
        sign = 1 # 1 means positive, -1 means negative

        for ch in s:
            if ch.isdigit():

                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':

                # Evaluate the expression to the left,
                # with result, sign, operand
                res += sign * operand

                # Save the recently encountered '+' sign
                sign = 1

                # Reset operand
                operand = 0

            elif ch == '-':

                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':

                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)

                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0

            elif ch == ')':

                # Evaluate the expression to the left
                # with result, sign and operand
                res += sign * operand

                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop() # stack pop 1, sign

                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                res += stack.pop() # stack pop 2, operand

                # Reset the operand
                operand = 0

        return res + sign * operand

'''
class Solution {
    public int calculate(String s) {

        Stack<Integer> stack = new Stack<Integer>();
        int operand = 0;
        int result = 0; // For the on-going result
        int sign = 1;  // 1 means positive, -1 means negative

        for (int i = 0; i < s.length(); i++) {

            char ch = s.charAt(i);
            if (Character.isDigit(ch)) {

                // Forming operand, since it could be more than one digit
                operand = 10 * operand + (int) (ch - '0');

            } else if (ch == '+') {

                // Evaluate the expression to the left,
                // with result, sign, operand
                result += sign * operand;

                // Save the recently encountered '+' sign
                sign = 1;

                // Reset operand
                operand = 0;

            } else if (ch == '-') {

                result += sign * operand;
                sign = -1;
                operand = 0;

            } else if (ch == '(') {

                // Push the result and sign on to the stack, for later
                // We push the result first, then sign
                stack.push(result);
                stack.push(sign);

                // Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1;
                result = 0;

            } else if (ch == ')') {

                // Evaluate the expression to the left
                // with result, sign and operand
                result += sign * operand;

                // ')' marks end of expression within a set of parenthesis
                // Its result is multiplied with sign on top of stack
                // as stack.pop() is the sign before the parenthesis
                result *= stack.pop();

                // Then add to the next operand on the top.
                // as stack.pop() is the result calculated before this parenthesis
                // (operand on stack) + (sign on stack * (result from parenthesis))
                result += stack.pop();

                // Reset the operand
                operand = 0;
            }
        }
        return result + (sign * operand);
    }
}
作者：LeetCode
链接：https://leetcode-cn.com/problems/basic-calculator/solution/ji-ben-ji-suan-qi-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
