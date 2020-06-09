# 029. 两数相除.py
'''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3

示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。

'''
# 转换思路：这道题实际上要求的就是除数能够减多少个被除数
def divide(self, divd: int, dior: int) -> int:
    res = 0
    # 判断
    sign =  1 if divd ^ dior >= 0 else -1
    divd = abs(divd)
    dior = abs(dior)
    while divd >= dior:
        res += 1
        divd -= dior
    res = res*sign 
    return min(max(-2**31, res), 2**31-1)

'''
上面就是我们简单想法，但是有个问题，当被除数为2147483648，除数为 1，必然超时？
那么该怎么办呢？我们接着上面的想法继续往下想！
我们直接举个例子如果被除数 15，除数 3，用我们上面的方法要遍历 5 次。
接下来，我们使用不断 增倍除数
比如：
被除数 除数
15 3
12 6
6 12
发现除数 大于 被除数大，再重现开始
6 3
...
3 3
虽然这个例子遍历次数相等，对于较大的数，可以减少时间复杂度。
'''


# 优化
class Solution:
    def divide(self, divd: int, dior: int) -> int:
        res = 0
        # 负数 ^ 负数 = 正数，负数 ^ 正数 = 负数
        sign =  1 if divd ^ dior >= 0 else -1
        #print(sign)
        divd = abs(divd)
        dior = abs(dior)
        while divd >= dior:
            # tmp, i = dior, 1
            tmp = dior
            i = 1
            while divd >= tmp:
                divd -= tmp
                res += i
                # i *= 2
                i <<= 1
                # tmp *= 2
                tmp <<= 1
        res = res * sign 
        return min(max(-2**31, res), 2**31-1)
# 作弊 1
class Solution:
    def divide(self, divd, dior):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign =  1 if divd ^ dior >= 0 else -1
        res = abs(divd) // abs(dior)
        res *= sign
        return min(max(-2**31, res), 2**31-1)


# 作弊2
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        self.dividend = dividend
        self.divisor = divisor

        a = int(operator.truediv(dividend, divisor))
        if a >= 2**31 or a < -2**31:
                return 2**31 - 1
        else:
                return a


# 二分
'''
除了异或判断符号位，其他没有用到位运算，都是加减运算，性能还是够用的。

题目分类提示了二分查找，那么按二分查找的思路去想就行了
既然要求不能使用乘除模运算，那么就让除数不断自加倍增，与被除数对比
倍增过头了就初始化为原始的除数值再次循环倍增
循环过程中被除数减去除数不断减小
直到小于除数为止
其过程就是把二分查找中的 mid=(left+right)/2 替换成了divisor*2
把 left 和 right 替换成了 divisor_tmp 和 divideng_tmp，这样理解就比较直观了
位运算我现在没什么思路，目前唯一想到的就是除数和被除数都 x&(-x) 取最低位的1，Math.min取小值，然后移位清掉后面的0，然后再进入二分循环，不知道这样会不会快一些。第一次写解答，自己好菜啊，只自学了一个多月的java，菜鸡瑟瑟发抖，欢迎大佬指点批评。╭(￣▽￣)╯

'''
# java
'''
class Solution {
    public int divide(int dividend, int divisor) {
        /** 除数为零就返回-1 按照测试样例的要求写的*/
        if (divisor==0)
            return -1;
        if (dividend==0)
            return 0;
        /** -2147483648, -1 这个测试样例的确没想到，结果翻车了*/
        if (dividend==Integer.MIN_VALUE && divisor==-1)
            return Integer.MAX_VALUE;
        /** 符号位的处理参考了大佬的异或处理方法*/
        boolean negetive= (dividend^ divisor)<0;
        /** div_count 是当前divisor_tmp相对于divisor的倍数 */
        int res=0, div_count=1;
        /** 因为值溢出之后边界问题处理太繁琐了，直接将数值转为long省去麻烦 */
        long dividend_tmp= Math.abs((long)dividend);
        long divisor_tmp= Math.abs((long)divisor);
        
        /** 按标准的二分查找代码模板写的 */
        while (dividend_tmp >= divisor_tmp) {
            dividend_tmp -= divisor_tmp;
            res+= div_count;
            
            if (dividend_tmp < Math.abs(divisor))
                break;

            /** divisor_tmp无法倍增时，就将其初始化为divisor绝对值，重新开始下一轮倍增*/
            if (dividend_tmp - divisor_tmp < divisor_tmp) {
                divisor_tmp = Math.abs(divisor);
                div_count = 1;
                continue;
            } 
            /** 不断倍增divisor_tmp直到和dividend_tmp一样大*/
            divisor_tmp += divisor_tmp;
            div_count += div_count;
        }
        return negetive? 0-res: res;
    }
}
'''




class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 倍增法
        # 负数 ^ 负数 = 正数  主要是看首位字母
        sign = 1 if dividend ^ divisor >= 0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            tmp = divisor
            i = 1
            while dividend >= tmp:
                dividend -= tmp
                res += i
                # 倍增
                # i *= 2
                # tmp *= 2
                i <<= 1
                tmp <<= 1
        res *= sign
        return min(max(-2 ** 31, res),2 ** 31 - 1)


