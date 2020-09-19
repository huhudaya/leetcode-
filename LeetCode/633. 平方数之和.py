'''
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c

示例1:
输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5

示例2:
输入: 3
输出: False
'''

# java
'''
public class Solution {
    public boolean judgeSquareSum(int c) {
        for (long a = 0; a * a <= c; a++) {
            double b = Math.sqrt(c - a * a);
            if (b == (int) b)
                return true;
        }
        return false;
    }
}
'''


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c ** 0.5)
        while left <= right:
            if c == left ** 2 + right ** 2:
                return True
            elif c < left ** 2 + right ** 2:
                right -= 1
            else:
                left += 1
        return False
