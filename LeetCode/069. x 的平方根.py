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
        if end**2 <= x:
            return end
        else:
            return start
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

def sqrt(x):
    if x < 2:
        return x
    left, right = 0, x
    result = 1
    while abs(result - x) > 0.000001:  # 不能等于0
        mid = left + (float(right - left)) / 2  # 要加个float，python2.x中/根据除数被除数情况来决定是否精确除法还是取整除法，python3.x中/精确除法，//整除
        result = mid * mid
        if result < x:
            # left=mid
            left = mid
        else:
            # right=x
            right = mid
    return mid
print(sqrt(2))

# 递归
'''
    private double mySqrt(int num, double low, double high, double range) {
        double mid = (low + high) / 2f;
//        System.out.println("mid = " + mid);
        if (num - mid * mid < 0 ) {
            return  mySqrt(num,low,(mid + high)/2f,range);
        }else{
            if (num - mid * mid > range){
                return  mySqrt(num,(low + mid)/2f,high,range);
            }
            String str = String.format("%.6f",mid);
            return Double.valueOf(str);
        }
    }
'''
'''
#include <iostream>
using namespace std;
 
double sqrtCount(double x, double precision) {
	if (x < 0)
		return -1;
	double low = 1, up = x;
	if (x > 0 && x < 1)
		low = x, up = 1;
	while (low <= up) {
		double mid = low + (up - low) / 2.0;
		if (abs(mid*mid - x) <= precision)
			return mid;
		else if (mid*mid > x)
			up = mid;
		else if (mid*mid < x)
			low = mid;
	}
	return -1;
}
 
int main() {
	double x = 11, precision = 0.000001;
	double res = sqrtCount(x, precision);
	cout << res << endl;
	cin.get();
	return 0;
}

'''
# 浮点数的二分模板
'''
链接：https://www.nowcoder.com/questionTerminal/5272cb35e20d460d85362c3728d4197a
来源：牛客网

#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    double m;
    cin>>m>>n;
    //浮点数二分模板
    double l = 0;
    double r = m;
    while (r-l>1e-14){
        double mid = (l+r)/2;
        if(pow(mid,n)>=m)
            r = mid;
        else
            l = mid;
    }
    printf("%.12lf\n",l);
    return 0;
}
'''