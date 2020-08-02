'''

编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例 1:

输入: 6
输出: true
解释: 6 = 2 × 3
示例 2:

输入: 8
输出: true
解释: 8 = 2 × 2 × 2
示例 3:

输入: 14
输出: false
解释: 14 不是丑数，因为它包含了另外一个质因数 7。
说明：

1 是丑数。
输入不会超过 32 位有符号整数的范围: [−231,  231 − 1]。
通过次数37,727提交次数76,492
'''
'''
根据定义， 任何一个丑叔都可以写成 n = 2^i * 3^j * 5^k 
（i,j,k都是幂，输入法不太方便写成指数，三个数都为0的时候，为丑数1的情况）
于是我们按照2,3,5 的顺序依次循环除，
当除到不是当前因数的倍数时，进行下一个因素的整数
这样，最后剩下的数为1则为丑数

'''


# 递归
class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        if num == 1:
            return True
        if num % 2 == 0:
            return self.isUgly(num // 2)
        if num % 3 == 0:
            return self.isUgly(num // 3)
        if num % 5 == 0:
            return self.isUgly(num // 5)
        return False


# 迭代
class Solution:
    def isUgly(self, num: int) -> bool:
        for p in 2, 3, 5:
            while num % p == 0 < num:
                num //= p
        return num == 1
