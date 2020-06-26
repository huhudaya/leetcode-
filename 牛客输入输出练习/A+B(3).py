'''
链接：https://ac.nowcoder.com/acm/contest/320/C
来源：牛客网

计算a+b

输入描述:
输入包括两个正整数a,b(1 <= a, b <= 10^9),输入数据有多组, 如果输入为0 0则结束输入
输出描述:
输出a+b的结果

输入
1 5
10 20
0 0

输出
6
30
'''

import sys

for line in sys.stdin:
    a, b = list(map(int, line.split()))
    a, b = [int(i) for i in line.split()]
    if a == 0 and b == 0:
        break
    else:
        print(a + b)
