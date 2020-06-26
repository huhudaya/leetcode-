'''
链接：https://ac.nowcoder.com/acm/contest/320/A
来源：牛客网

计算a+b

输入描述:
输入包括两个正整数a,b(1 <= a, b <= 10^9),输入数据包括多组。
输出描述:
输出a+b的结果
示例1
输入
复制
1 5
10 20
输出
复制
6
30
'''
# 方法一
import sys

for nums in sys.stdin:
    i = [int(i) for i in nums.split()]
    print(sum(i))

# 方法二
while True:
    try:
        A = list(map(int, input().split(' ')))
        print(sum(A))
    except:
        break
# 方法三
import sys

for line in sys.stdin:
    a, b = list(map(int, line.split()))
    print(a + b)
