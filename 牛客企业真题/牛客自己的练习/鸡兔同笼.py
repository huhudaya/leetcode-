'''
链接：https://www.nowcoder.com/questionTerminal/fda725b4d9a14010bb145272cababef1
来源：牛客网

一个笼子里面关了鸡和兔子（鸡有2只脚，兔子有4只脚，没有例外）。已经知道了笼子里面脚的总数a，问笼子里面至少有多少只动物，至多有多少只动物。

输入描述:
每组测试数据占1行，每行一个正整数a (a < 32768)


输出描述:
输出包含n行，每行对应一个输入,包含两个正整数，第一个是最少的动物数，第二个是最多的动物数，两个正整数用一个空格分开
如果没有满足要求的答案，则输出两个0。
示例1
输入
2
3
20
输出
0 0
5 10
'''


def get_res(a):
    if a & 1:
        return [0, 0]
    max_val = a // 2
    min_val = a // 4 + a % 4 // 2
    return [min_val, max_val]


n = int(input())
for i in range(n):
    a = int(input())
    print(*get_res(a))
