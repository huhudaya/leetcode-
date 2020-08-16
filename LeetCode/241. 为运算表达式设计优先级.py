'''
给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。

示例 1:

输入: "2-1-1"
输出: [0, 2]
解释:
((2-1)-1) = 0
(2-(1-1)) = 2
示例 2:

输入: "2*3-4*5"
输出: [-34, -14, -10, -10, 10]
解释:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
'''

from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        res = []
        ops = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}
        for indx in range(1, len(input) - 1):
            if input[indx] in ops.keys():

                for left in self.diffWaysToCompute(input[:indx]):
                    for right in self.diffWaysToCompute(input[indx + 1:]):
                        res.append(ops[input[indx]](left, right))
        if not res:
            res.append(int(input))

        return res
