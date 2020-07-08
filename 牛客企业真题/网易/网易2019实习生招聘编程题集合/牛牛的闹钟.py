'''
链接：https://www.nowcoder.com/questionTerminal/9173e83d1774462f81255a26feafd7c6?answerType=1&f=discussion
来源：牛客网

牛牛总是睡过头，所以他定了很多闹钟，只有在闹钟响的时候他才会醒过来并且决定起不起床。从他起床算起他需要X分钟到达教室，上课时间为当天的A时B分，请问他最晚可以什么时间起床

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含一个正整数，表示闹钟的数量N(N<=100)。
接下来的N行每行包含两个整数，表示这个闹钟响起的时间为Hi(0<=A<24)时Mi(0<=B<60)分。
接下来的一行包含一个整数，表示从起床算起他需要X(0<=X<=100)分钟到达教室。
接下来的一行包含两个整数，表示上课时间为A(0<=A<24)时B(0<=B<60)分。
数据保证至少有一个闹钟可以让牛牛及时到达教室。


输出描述:
输出两个整数表示牛牛最晚起床时间。
示例1
输入
3
5 0
6 0
7 0
59
6 59
输出
6 0
'''


'''
列表前面加星号作用是将列表解开成两个独立的参数，传入函数，

字典前面加两个星号，是将字典解开成独立的元素作为形参。

def add(a, b):
    return a+b
 
data = [4,3]
print add(*data)
#equals to print add(4, 3)
data = {'a' : 4, 'b' : 3}
print add(**data)pr



print(*formats(clocks[index - 1]))
这样
>>> print(*(1,2))
>>> 1 2         # 输出
'''
import bisect

tomins = lambda h, m: h * 60 + m
formats = lambda time: (time // 60, time % 60)

n = int(input())
clocks = [tomins(*list(map(int, input().split()))) for i in range(n)]

clocks.sort()
dist = int(input())
schedule = tomins(*list(map(int, input().split())))
idx = bisect.bisect(clocks, schedule - dist)
print(*formats(clocks[idx - 1]))