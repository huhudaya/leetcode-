'''
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]
其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。
不能使用除法。

示例:
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]

提示：
所有元素乘积之和不会溢出 32 位整数
a.length <= 100000
通过次数16,363提交次数28,019
'''
from typing import List
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        # 使用前缀和后缀数组
        n = len(a)
        prefix = [1] * n
        suffix = [1] * n
        res = [0] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * a[i - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * a[i + 1]
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        return res
