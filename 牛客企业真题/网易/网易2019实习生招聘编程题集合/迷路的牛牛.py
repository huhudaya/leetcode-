'''
链接：https://www.nowcoder.com/questionTerminal/fc72d3493d7e4be883e931d507352a4a?answerType=1&f=discussion
来源：牛客网

牛牛去犇犇老师家补课，出门的时候面向北方，但是现在他迷路了。
虽然他手里有一张地图，但是他需要知道自己面向哪个方向，请你帮帮他。

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含一个正整数，表示转方向的次数N(N<=1000)。
接下来的一行包含一个长度为N的字符串，由L和R组成，L表示向左转，R表示向右转。


输出描述:
输出牛牛最后面向的方向，N表示北，S表示南，E表示东，W表示西。
示例1
输入
3
LRR
输出
E
'''

'''
链接：https://www.nowcoder.com/questionTerminal/fc72d3493d7e4be883e931d507352a4a?answerType=1&f=discussion
来源：牛客网

方法：模拟

分析：
按照题意模拟即可，判断向左走了多少步，向右走了多少步，然后得出向左向右走的步数的差值
然后对4进行取模，为什么对4取模呢？是因为一共有NSWE四个方向，所以需要对4取模
如果取模之后得到的结果ans是负数，那么ans=ans+4，因为向右走了1步等价于向左走了三步
然后根据相差的步数来判断到底是哪个方向，为了方便记录向左ans++，向右ans--：
算法实现：
(0). 遍历字符串s，然后如果当前字符为'L'，那么ans++，否则ans--。
(1). 将ans对4取模，保证ans最后为区间属于[0,3]。
(2). 判断最后牛牛面向的方向:
如果ans = 0，那么牛牛最后面向的方向为N
如果ans = 1，那么牛牛最后面向的方向为W
如果ans = 2，那么牛牛最后面向的方向为S
如果ans = 3，那么牛牛最后面向的方向为E

复杂度分析：
时间复杂度：O(n)
空间复杂度：O(1)
'''
import sys

n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()
res = 0
for i in s:
    if i == "L":
        res -= 1
    else:
        res += 1
di = ["N", "E", "S", "W"]
print(di[res % 4])
