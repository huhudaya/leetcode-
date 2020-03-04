'''
给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。

初始化 A 和 B 的元素数量分别为 m 和 n。

示例:

输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
'''
from typing import List
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        # 双指针，从后往前遍历
        p1 = m -1
        p2 = n - 1
        # 定义p指针为写指针，记录当前的位置
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            # 谁大移动谁
            if A[p1] < B[p2]:
                A[p] = B[p2]
                p2 -= 1
            else:
                A[p] = A[p1]
                p1 -= 1
            p -= 1
        A[:p2 + 1] = B[:p2 + 1]