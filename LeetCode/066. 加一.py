# 066. 加一.py
'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

链接：https://leetcode-cn.com/problems/plus-one
'''
'''
根据题意加一，没错就是加一这很重要，因为它是只加一的所以有可能的情况就只有两种：

除 99 之外的数字加一；
数字 99。
加一得十进一位个位数为 00 加法运算如不出现进位就运算结束了且进位只会是一。

所以只需要判断有没有进位并模拟出它的进位方式，如十位数加 11 个位数置为 00，如此循环直到判断没有再进位就退出循环返回结果。

然后还有一些特殊情况就是当出现 9999、999999 之类的数字时，循环到最后也需要进位，出现这种情况时需要手动将它进一位。

'''
# java
'''
class Solution {
    public int[] plusOne(int[] digits) {
        for (int i = digits.length - 1; i >= 0; i--) {
            digits[i]++;
            digits[i] = digits[i] % 10;
            if (digits[i] != 0) return digits;
        }
        digits = new int[digits.length + 1];
        digits[0] = 1;
        return digits;
    }
}
'''
'''
标签：数组遍历
这道题需要整理出来有哪几种情况，在进行处理会更舒服
末位无进位，则末位加一即可，因为末位无进位，前面也不可能产生进位，比如 45 => 46
末位有进位，在中间位置进位停止，则需要找到进位的典型标志，即为当前位 %10后为 0，则前一位加 1，直到不为 0 为止，比如 499 => 500
末位有进位，并且一直进位到最前方导致结果多出一位，对于这种情况，需要在第 2 种情况遍历结束的基础上，进行单独处理，比如 999 => 1000
在下方的 Java 和 JavaScript 代码中，对于第三种情况，对其他位进行了赋值 0 处理，Java 比较 tricky 直接 new 数组即可，JavaScript 则使用了 ES6 语法进行赋值
时间复杂度：O(n)
'''
class Solution:
    def plusOne(self, digits):
        return [int(x) for x in str(int(''.join([str(i) for i in digits])) + 1)]

from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 好题
        # 分两种情况，末位无进位，末位有进位
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            # 当末位是10的时候，这个时候%10为0
            digits[i] = digits[i] % 10 
            if digits[i] != 0:
                return digits
        if digits[0] == 0:
            digits.insert(0, 1)
            return digits



            