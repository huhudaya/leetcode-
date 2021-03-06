'''
链接：https://ac.nowcoder.com/acm/contest/320/B
来源：牛客网

计算a+b

输入描述:
输入第一行包括一个数据组数t(1 <= t <= 100)
接下来每行包括两个正整数a,b(1 <= a, b <= 10^9)
输出描述:
输出a+b的结果
示例1
输入

2
1 5
10 20

输出
6
30
'''
import sys

cnt = int(input())
for i in range(cnt):
    a, b = list(map(int, input().split()))
    print(a + b)

import sys

n = int(input())
for line in sys.stdin.readlines():
    value = list(map(int, line.strip().split()))
    print(sum(value))

line = list(map(int, sys.stdin.readline().strip().split))
