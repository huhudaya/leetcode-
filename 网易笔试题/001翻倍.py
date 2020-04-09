'''
小易给定你数字A,B（A<B）和系数p,q。每次操作你可以将变成A+p或者将变成p*q。问至少几次操作使得B<=A。
1 <= A
p,B <= 10^9
2 <= q <= 10
1 <= T <= 5
'''
import sys
import sys
class Solution:
    def doubleCnt(self, a, b, p, q):
        res = b - a
        cnt = 0
        while p < res:
            p *= q
            cnt += 1
        return cnt + 1
size = int(sys.stdin.readline().strip())
for i in range(size):
    a, b, p, q = list(map(int, sys.stdin.readline().strip().split()))
    print(Solution().doubleCnt(a, b, p, q))
