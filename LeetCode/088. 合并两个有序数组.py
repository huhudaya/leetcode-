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


# 时间复杂度 : O(n + m)
# 空间复杂度 : O(m)
# 双指针从前往后
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
        # 本题的核心核心就是复制一个tmp数组！！！1
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


# 双指针 从后往前
'''
分析：
    直觉
    双指针从前往后已经取得了最优的时间复杂度O(n + m)
    但需要使用额外空间。这是由于在从头改变nums1的值时，需要把nums1中的元素存放在其他位置
如果我们从结尾开始改写 nums1 的值又会如何呢？这里没有信息，因此不需要额外空间！！！

这里的指针 p 用于追踪添加元素的位置

时间复杂度 : O(n + m)
空间复杂度 : O(1)
'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # two get pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # set pointer for nums1
        p = m + n - 1
        # while there are still elements to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        # add missing elements from nums2
        nums1[:p2 + 1] = nums2[:p2 + 1]

# Java
'''
class Solution {
  public void merge(int[] nums1, int m, int[] nums2, int n) {
    // Make a copy of nums1.
    int [] nums1_copy = new int[m];
    System.arraycopy(nums1, 0, nums1_copy, 0, m);

    // Two get pointers for nums1_copy and nums2.
    int p1 = 0;
    int p2 = 0;

    // Set pointer for nums1
    int p = 0;

    // Compare elements from nums1_copy and nums2
    // and add the smallest one into nums1.
    while ((p1 < m) && (p2 < n))
      nums1[p++] = (nums1_copy[p1] < nums2[p2]) ? nums1_copy[p1++] : nums2[p2++];

    // if there are still elements to add
    if (p1 < m)
      System.arraycopy(nums1_copy, p1, nums1, p1 + p2, m + n - p1 - p2);
    if (p2 < n)
      System.arraycopy(nums2, p2, nums1, p1 + p2, m + n - p1 - p2);
  }
}
'''
