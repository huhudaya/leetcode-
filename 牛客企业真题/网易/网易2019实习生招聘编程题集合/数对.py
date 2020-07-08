'''
牛牛以前在老师那里得到了一个正整数数对(x, y), 牛牛忘记他们具体是多少了。

但是牛牛记得老师告诉过他x和y均不大于n, 并且x除以y的余数大于等于k。
牛牛希望你能帮他计算一共有多少个可能的数对。

输入描述:
输入包括两个正整数n,k(1 <= n <= 10^5, 0 <= k <= n - 1)。


输出描述:
对于每个测试用例, 输出一个正整数表示可能的数对数量。
示例1
输入
5 2
输出
7
说明
满足条件的数对有(2,3),(2,4),(2,5),(3,4),(3,5),(4,5),(5,3)
'''
# 链接：https://www.nowcoder.com/questionTerminal/bac5a2372e204b2ab04cc437db76dc4f?f=discussion
'''
链接：https://www.nowcoder.com/questionTerminal/bac5a2372e204b2ab04cc437db76dc4f?f=discussion
朴素的做法是枚举n^2个点然后跟k作比较。这显然对n<=100000的规模来说是不允许通过的。
注意到当除数是y时，当x=1~n时，余数是1,2,3,...,y-1,0循环出现，循环节长度显然是y
那么我们可以枚举y=k~n(当y<k时所有余数均小于k，因此不需要考虑)
然后对于x=1~n，总共出现了[n/y]个循环节，然后数出每个循环节里面不小于k的余数。
最后再数出不满一个循环节的不小于k的余数，就是答案了。注意当k=0的时候由于余数0出现在循环的末尾，因此要特别判断。
复杂度为O(n)
'''
temp = list(map(int, input().split()))
n = temp[0]
k = temp[1]
# 这里特判一下是不是k=0,如果是0，要特殊处理一下
if k == 0:
    ans = n * n  # k=0是比较特殊的
else:
    ans = 0
    for y in range(k + 1, n + 1):
        # 从每一列来看，根据每y个一个循环的规律，快速计算余数矩阵余数值
        # cycle = [i for i in range(1, y)] + [0]  # 循环部分
        satisfy_num = y - k  # 一个循环中满足的组合个数
        cycle_num = n // y  # 完整循环个数
        res_num = n % y  # 剩余不完整部分循环中的元素个数
        ans += satisfy_num * cycle_num + max(res_num - k + 1, 0)  # 注意这里最差就是不完整部分满足个数为0，但是不能为负数
print(ans)


# 另外的版本
n, k = list(map(int, input().strip().split()))
ans = 0
# 遍历 y 的取值
for y in range(k + 1, n + 1):
    res = n // y * (y - k)
    ans += res
    if n % y >= k:
        if k:
            res += n % y - k + 1
        else:
            res += n % y