'''
链接：https://www.nowcoder.com/questionTerminal/5272cb35e20d460d85362c3728d4197a
来源：牛客网
在没有任何数学库函数的情况下，求一个数 m 开 n 次方的结果。
输入描述:
每组输入只有1行，包括有一个正实数m和一个正整数n，其中1 <= n <= 32, 1<=m<=2^n
输出描述:
输出只有一行，打印m开n次方的结果，小数点后面保留12位。
示例1
输入
2 10
输出
1.071773462536
'''

# 方法一
if __name__ == '__main__':
    m, n = list(map(float, input().split()))
    n = int(n)

    left = 0
    right = m
    midpre = 0
    mid = 0
    while left < right:
        mid = (right - left) / 2 + left
        # sum_num = 1
        # for i in range(n):
        #     sum_num *= mid
        sum_num = mid ** n

        if abs(mid - midpre) < 1e-13:
            break
        elif sum_num > m:
            right = mid
        else:
            left = mid
        midpre = mid

    print("%.12f" % mid)


# 方法二
def root3(n, num):
    acc = 10 ** (-14)
    low = 0
    high = num
    while (high - low >= acc):
        mid = (low + high) / 2.0
        # prod=1
        # for j in range(n): # mid multiply n times
        # prod=prod*mid
        prod = mid ** n
        if (abs(prod - num) <= acc):
            break
        if (prod >= num):
            high = mid
        else:
            low = mid

    print("%.12f" % mid)


if __name__ == "__main__":
    num, n = map(float, input().strip().split())
    n = int(n)
    root3(n, num)

# 自己的版本
import sys

m, n = list(map(float, input().strip().split()))
n = int(n)


def check(x, y, eps):
    return abs(x - y) <= eps


def sqrt(m, n):
    left = 0
    right = m
    # 这个eps要取的比精度稍微大一点
    eps = 1e-13
    while abs(right - left) >= eps:
        mid = left + (right - left) / 2
        tmp = mid ** n
        # 下面这句话加不加无所谓
        # if abs(tmp - m) <= eps:
        #     break
        if tmp > m:
            right = mid
        else:
            left = mid
    # return "%.12f" % mid
    return "%.12f" % left


print(sqrt(m, n))

# 浮点数的二分模板
'''
和定点数的二分查找不同的地方有以下几个方面：

1、使用二分查找。

2、三个变量（左边界、右边界、中间值） 必须使用 double 类型。

3、查找循环条件不同。判断浮点数相等的方法和判断定点数相等方法是不一样的，一般我们定义一个精度范围 eps
  两个浮点数之差的绝对值在 eps 之内，我们就认为这两个浮点数是相同的。
'''
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
    while (r-l > 1e-14){
        double mid = (l+r)/2;
        if(pow(mid,n) >= m)
            r = mid;
        else
            l = mid;
    }
    printf("%.12lf\n",l);
    return 0;
}
'''

# 模板
'''
//校验函数
bool check(double x) {
    ...
}
 
//下面是主框架
double left = -1e6;//左边界。可以根据题目具体查找条件修改
double right = 1e6;//右边界。可以根据题目具体查找条件修改
double eps = 1e-9;//精度
double mid;//中值
 
while (fabs(right-left)>eps) {
    mid=(right+left)/2;
    ans = calc(mid);   
    //使用mid计算
    if (check(mid)) {
        right = mid;
    } else {
        left = mid;
    }
}
//left就是最终的结果
'''

# 三分模板
'''
//计算函数
bool calc(double ) {
    ...
}
 
//下面是主框架
double left = -1e6;//左边界。可以根据题目具体查找条件修改
double right = 1e6;//右边界。可以根据题目具体查找条件修改
double eps = 1e-9;//精度
//采用三分
double l_mid;//左中值
double l_ans;
double r_mid;//右中值
double r_ans;
 
while (fabs(right-left)>eps) {
    l_mid=left+(right-left)/3;
    l_ans = calc(l_mid);//使用l_mid计算
 
    r_mid=right-(right-left)/3;
    r_ans = calc(r_mid);//使用r_mid计算
    
    //缩小查找范围
    if (l_ans <= r_ans) {
        right = r_mid;
    } else {
        left = l_mid;
    }
}
//l_ans就是最终的结果
'''

'''
#include <cstdio>
#include <cmath>
 
double check(double x, double n) {
    return x*x*x>=n;
}
 
int main() {
    double n;
    scanf("%lf", &n);
 
    double left = -10000;
    double right = 10000;
    double eps = 1e-8;
    double mid;
    while (fabs(left-right)>eps) {
        mid = (right+left)/2;
        if (true == check(mid, n)) {
            right = mid;
        } else {
            left = mid;
        }
    }
    printf("%.6lf\n", left);
    return 0;
}
'''
