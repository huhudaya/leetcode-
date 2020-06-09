# 069. x 的平方根.py
'''
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    # 二分法
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        start = 0
        end = x
        while start + 1 < end:
            #找 mid^2 <= x的LastPosition
            mid = start + (end-start) // 2
            if mid**2 <= x:
                start = mid
            else:
                end = mid
        if end**2 <= x: return end
        else: return start
    #在题解中看到基本不等式方法
    # '''基本不等式(a+b)/2 >=√ab 推导自 (a-b)^2 >= 0，注意 a>0 且 b>0'''
    # def mySqrt(self, x: int) -> int:
    #     r = x
    #     while r*r > x:
    #         r = (r + x/r) // 2
    #     return int(r)
    # def mySqrt(self, x):
    #     """
    #     :type x: int
    #     :rtype: int
    #     """
    #     if x <= 1:
    #         return x
    #     r = x
    #     while r > x / r:
    #         r = (r + x / r) // 2
    #     return int(r)