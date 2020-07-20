# 004.寻找两个有序数组的中位数.py
'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
'''
# 二分法！ O(log(m+n))
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        left = (n + m + 1) // 2
        right = (n + m + 2) // 2
        return (self.getKth(nums1, 0, n - 1, nums2, 0, m - 1, left) + self.getKth(nums1, 0, n - 1, nums2, 0, m - 1, right)) / 2
    def getKth(self, nums1: List[int], start1: int, end1: int, nums2: List[int], start2: int, end2: int, k: int) -> int:
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        #让 len1 的长度小于 len2，这样就能保证如果有数组空了，一定是 len1 
        if len1 > len2:
            return self.getKth(nums2, start2, end2, nums1, start1, end1, k)
        #这里判断nums1数组是否为空，为空时直接取nums2数组即可
        if len1 == 0:
            return nums2[start2 + k - 1]
        if k == 1:
            return min(nums1[start1], nums2[start2])
        #为什么要减一？是因为在数组中索引是以0开始的
        i = start1 + min(len1, k // 2) - 1
        j = start2 + min(len2, k // 2) - 1
        #谁小抛弃谁的那一部分
        if nums1[i] > nums2[j]:
            #这个时候统一都降一个维度，求两个数组的第（k-抛弃的那部分的长度）
            return self.getKth(nums1, start1, end1, nums2, j + 1, end2, k - (j - start2 + 1))
        else:
            return self.getKth(nums1, i + 1, end1, nums2, start2, end2, k - (i - start1 + 1))

# 双指针
# 简单粗暴，先将两个数组合并，两个有序数组的合并也是归并排序中的一部分。然后根据奇数，还是偶数，返回中位数。
# 时间复杂度：遍历全部数组 (m+n)(m+n)
# 空间复杂度：开辟了一个数组，保存合并后的两个数组 O(m+n)O(m+n)
'''
解法二
其实，我们不需要将两个数组真的合并，我们只需要找到中位数在哪里就可以了。

开始的思路是写一个循环，然后里边判断是否到了中位数的位置，到了就返回结果，但这里对偶数和奇数的分类会很麻烦。当其中一个数组遍历完后，出了 for 循环对边界的判断也会分几种情况。总体来说，虽然复杂度不影响，但代码会看起来很乱。

首先是怎么将奇数和偶数的情况合并一下。

用 len 表示合并后数组的长度，如果是奇数，我们需要知道第 （len+1）/2 个数就可以了，如果遍历的话需要遍历 int(len/2 ) + 1 次。如果是偶数，我们需要知道第 len/2和 len/2+1 个数，也是需要遍历 len/2+1 次。所以遍历的话，奇数和偶数都是 len/2+1 次。

返回中位数的话，奇数需要最后一次遍历的结果就可以了，偶数需要最后一次和上一次遍历的结果。所以我们用两个变量 left 和 right，right 保存当前循环的结果，在每次循环前将 right 的值赋给 left。这样在最后一次循环的时候，left 将得到 right 的值，也就是上一次循环的结果，接下来 right 更新为最后一次的结果。

循环中该怎么写，什么时候 A 数组后移，什么时候 B 数组后移。用 aStart 和 bStart 分别表示当前指向 A 数组和 B 数组的位置。如果 aStart 还没有到最后并且此时 A 位置的数字小于 B 位置的数组，那么就可以后移了。也就是aStart＜m&&A[aStart]< B[bStart]。

但如果 B 数组此刻已经没有数字了，继续取数字 B[ bStart ]，则会越界，所以判断下 bStart 是否大于数组长度了，这样 || 后边的就不会执行了，也就不会导致错误了，所以增加为 aStart＜m&&(bStart) >= n||A[aStart]<B[bStart]) 。

代码
Java
public double findMedianSortedArrays(int[] A, int[] B) {
    int m = A.length;
    int n = B.length;
    int len = m + n;
    int left = -1, right = -1;
    int aStart = 0, bStart = 0;
    for (int i = 0; i <= len / 2; i++) {
        left = right;
        if (aStart < m && (bStart >= n || A[aStart] < B[bStart])) {
            right = A[aStart++];
        } else {
            right = B[bStart++];
        }
    }
    if ((len & 1) == 0)
        return (left + right) / 2.0;
    else
        return right;
}
时间复杂度：遍历 len/2+1 次，len=m+n，所以时间复杂度依旧是 O(m+n)O(m+n)。

空间复杂度：我们申请了常数个变量，也就是 m，n，len，left，right，aStart，bStart 以及 i

总共 8 个变量，所以空间复杂度是 O(1)

'''




'''
这道题如果时间复杂度没有限定在 O(log(m+n))O(log(m+n))，我们可以用 O(m+n) 的算法解决，用两个指针分别指向两个数组，比较指针下的元素大小，一共移动次数为 (m+n + 1)/2，便是中位数。

首先，我们理解什么中位数：指的是该数左右个数相等。

比如：odd : [1,| 2 |,3]，2 就是这个数组的中位数，左右两边都只要 1 位；

even: [1,| 2, 3 |,4]，2,3 就是这个数组的中位数，左右两边 1 位；

那么，现在我们有两个数组：

num1: [a1,a2,a3,...an]

nums2: [b1,b2,b3,...bn]

[nums1[:left1],nums2[:left2] | nums1[left1:], nums2[left2:]]

只要保证左右两边 个数 相同，中位数就在 | 这个边界旁边产生。

如何找边界值，我们可以用二分法，我们先确定 num1 取 m1 个数的左半边，那么 num2 取 m2 = (m+n+1)/2 - m1 的左半边，找到合适的 m1，就用二分法找。

当 [ [a1],[b1,b2,b3] | [a2,..an],[b4,...bn] ]

我们只需要比较 b3 和 a2 的关系的大小，就可以知道这种分法是不是准确的！

例如：我们令：

nums1 = [-1,1,3,5,7,9]

nums2 =[2,4,6,8,10,12,14,16]

当 m1 = 4,m2 = 3 ,它的中位数就是median = (num1[m1] + num2[m2])/2

时间复杂度：O(log(min(m,n)))

对于代码中边界情况，大家需要自己琢磨。

代码：
PythonC++Java
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2,nums1)
        k = (n1 + n2 + 1)//2
        left = 0
        right = n1
        while left < right :
            m1 = left +(right - left)//2
            m2 = k - m1
            if nums1[m1] < nums2[m2-1]:
                left = m1 + 1
            else:
                right = m1
        m1 = left
        m2 = k - m1 
        c1 = max(nums1[m1-1] if m1 > 0 else float("-inf"), nums2[m2-1] if m2 > 0 else float("-inf") )
        if (n1 + n2) % 2 == 1:
            return c1
        c2 = min(nums1[m1] if m1 < n1 else float("inf"), nums2[m2] if m2 <n2 else float("inf"))
        return (c1 + c2) / 2
'''

# 双指针
'''
解法二
其实，我们不需要将两个数组真的合并，我们只需要找到中位数在哪里就可以了。

开始的思路是写一个循环，然后里边判断是否到了中位数的位置，到了就返回结果，但这里对偶数和奇数的分类会很麻烦。当其中一个数组遍历完后，出了 for 循环对边界的判断也会分几种情况。总体来说，虽然复杂度不影响，但代码会看起来很乱。

首先是怎么将奇数和偶数的情况合并一下。

用 len 表示合并后数组的长度，如果是奇数，我们需要知道第 （len+1）/2 个数就可以了，如果遍历的话需要遍历 int(len/2 ) + 1 次。如果是偶数，我们需要知道第 len/2和 len/2+1 个数，也是需要遍历 len/2+1 次。所以遍历的话，奇数和偶数都是 len/2+1 次。

返回中位数的话，奇数需要最后一次遍历的结果就可以了，偶数需要最后一次和上一次遍历的结果。所以我们用两个变量 left 和 right，right 保存当前循环的结果，在每次循环前将 right 的值赋给 left。这样在最后一次循环的时候，left 将得到 right 的值，也就是上一次循环的结果，接下来 right 更新为最后一次的结果。

循环中该怎么写，什么时候 A 数组后移，什么时候 B 数组后移。用 aStart 和 bStart 分别表示当前指向 A 数组和 B 数组的位置。如果 aStart 还没有到最后并且此时 A 位置的数字小于 B 位置的数组，那么就可以后移了。也就是aStart＜m&&A[aStart]< B[bStart]。

但如果 B 数组此刻已经没有数字了，继续取数字 B[ bStart ]，则会越界，所以判断下 bStart 是否大于数组长度了，这样 || 后边的就不会执行了，也就不会导致错误了，所以增加为 aStart＜m&&(bStart) >= n||A[aStart]<B[bStart]) 。
'''
