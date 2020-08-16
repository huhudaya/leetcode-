'''
给定一个整数，将其转化为7进制，并以字符串形式输出。

示例 1:

输入: 100
输出: "202"
示例 2:

输入: -7
输出: "-10"
注意: 输入范围是 [-1e7, 1e7] 。
'''


class Solution:
    def convertToBase7(self, num: int) -> str:
        res = ''
        numAbs = abs(num)
        while numAbs >= 7:
            res += str(numAbs % 7)
            numAbs //= 7
        res += str(numAbs)

        return res[::-1] if num >= 0 else '-' + res[::-1]
