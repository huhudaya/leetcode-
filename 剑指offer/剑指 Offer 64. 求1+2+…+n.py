'''
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

示例 1：
输入: n = 3
输出: 6

示例 2：
输入: n = 9
输出: 45

限制：
1 <= n <= 10000
'''


# 递归
class Solution:
    def sumNums(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            return self.sumNums(n - 1) + n

class Solution:
    def sumNums(self, n: int) -> int:
        return n and (n + self.sumNums(n-1))
# java
'''
public int sumNums(int n) {
        return IntStream.range(1,n+1).sum();
    }
'''
'''
class Solution {
public:
    int sumNums(int n) {
        n && (n += sumNums(n-1));
        return n;
    }
};
'''