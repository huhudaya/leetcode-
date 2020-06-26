# 326. 3的幂.py
'''
给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:

输入: 27
输出: true
示例 2:

输入: 0
输出: false
示例 3:

输入: 9
输出: true
示例 4:

输入: 45
输出: false

链接：https://leetcode-cn.com/problems/power-of-three
'''
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0
# 思路一：循环
# class Solution:
    # def isPowerOfThree(self, n: int) -> bool:
    #     if n > 1:
    #         while n % 3 == 0:
    #             n //= 3
    #     return n == 1

# 思路二：递归
# class Solution:
    # def isPowerOfThree(self, n: int) -> bool:
    #     return n > 0 and (n == 1 or (n % 3 == 0 and self.isPowerOfThree(n // 3)))

# 思路三：数字
# int能放下的最大3的幂
# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         return n > 0 and (1162261467 % n == 0);

'''
若n是3的幂，那么log3(n)一定是个整数，由换底公式可以的得到log3(n) = log10(n) / log10(3)
只需要判断log3(n)是不是整数即可
同理该公式可以推广到n的幂
'''
'''
class Solution {
public:
    bool isPowerOfThree(int n) {
        double res = log10(n) / log10(3);
        return res - (int)res == 0?true:false;
    }
};
'''