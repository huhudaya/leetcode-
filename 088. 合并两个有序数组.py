# 88. 合并两个有序数组.py
'''
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

链接：https://leetcode-cn.com/problems/merge-sorted-array
'''
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 其实就是归并排序的思想吧。。
        # 双指针
        i = 0
        j = 0
        k = 0
        tmp = nums1[:m]
        while i < m and j < n:
            # 谁小移动谁
            if tmp[i] < nums2[j]:
                nums1[k] = tmp[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        # 总有一个要到头
        while i < m:
            nums1[k] = tmp[i]
            i += 1
            k += 1
        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1
