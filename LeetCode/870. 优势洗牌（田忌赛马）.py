'''
给定两个大小相等的数组 A 和 B，A 相对于 B 的优势可以用满足 A[i] > B[i] 的索引 i 的数目来描述。

返回 A 的任意排列，使其相对于 B 的优势最大化。

 

示例 1：

输入：A = [2,7,11,15], B = [1,10,4,11]
输出：[2,11,7,15]
示例 2：

输入：A = [12,24,8,32], B = [13,25,32,11]
输出：[24,32,8,12]
 

提示：

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9
通过次数7,650提交次数19,876
'''
from typing import List


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        new_B = [(i, B[i]) for i in range(n)]
        new_B.sort(key=lambda x: x[1])
        res = [-1 for _ in range(n)]
        A.sort()
        # 核心思路，A当前的最小值比B当前的最小值大，则两者进行配对
        # 否则A当前的最小值要和B当前的最大值进行一个配对
        # 让A的每一个元素都发挥一个最大的作用
        left = 0
        right = n - 1
        print(A, new_B)
        for i in range(n):
            if A[i] > new_B[left][1]:
                res[new_B[left][0]] = A[i]
                left += 1
            else:
                res[new_B[right][0]] = A[i]
                right -= 1
        return res


A = [12, 24, 8, 32]
B = [13, 25, 32, 11]
print(Solution().advantageCount(A, B))
