'''
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

 

示例：

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。
'''
# 方法一：直接排序
# 思路及算法
# 最直接的做法是将这个二维数组另存为为一维数组，并对该一维数组进行排序。最后这个一维数组中的第 k 个数即为答案。
# 时间复杂度：O(n^2logn)
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rec = sorted(sum(matrix, []))
        return rec[k - 1]


# 方法二：归并排序
# 合并n个有序数组，合并k个有序数组
# 使用堆进行 n个有序数组的合并排序 KlogN
# 思路及算法
# 由题目给出的性质可知，这个矩阵的每一行均为一个有序数组。问题即转化为从这 n 个有序数组中找第 k 大的数，可以想到利用归并排序的做法，归并到第 k 个数即可停止。
# 一般归并排序是两个数组归并，而本题是 n 个数组归并，所以需要用小根堆维护，以优化时间复杂度。
# 时间复杂度：O(klogn) 需要进行k次归并，每次维护堆的数据结构都是logN的算法，所以为klogN的时间复杂度
# 但是最坏的情况下，k=n^2, 此时时间复杂度为N^2logN
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)  # 注：题目中这个矩阵是n*n的，所以长宽都是n

        # 需要一同记录一个(idx,idy)作为第几行第几列，其中idx为行索引，idy为列索引
        pq = [(matrix[i][0], i, 0) for i in range(n)]  # 取出第一列候选人
        # matrix[i][0]是具体的值，后面的(i,0)是在记录候选人在矩阵中的位置，方便每次右移添加下一个候选人

        heapq.heapify(pq)  # 变成一个heap
        # Python中为小根堆，只要从堆中取k次即可
        for i in range(k - 1):  # 一共弹k次：这里k-1次，return的时候1次
            num, x, y = heapq.heappop(pq)  # 弹出候选人里最小一个
            if y != n - 1:  # 如果这一行还没被弹完
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))  # 加入这一行的下一个候选人

        return heapq.heappop(pq)[0]


'''
关于二分查找返回的left一定在矩阵中这个问题, 写一点个人的理解.
可以参考34. 在排序数组中查找元素的第一个和最后一个位置.

我们先看check函数.check函数的目的是统计矩阵里小等于mid的元素数目count.
 再判断count和k的关系.因为mid = (l + r) / 2
 这种划分方法是把矩阵划分成了[left , mid] 与[mid + 1, right]两部分. 
 当 count < k 时, 说明mid太小了, 我们应该在[mid + 1, right] 这个范围里查找. 
 否则在[left, mid]范围里查找.
如果存在一个不在矩阵中的数a满足条件, 因为a不在矩阵中,那count统计的元素肯定都是小于a的,
那一定存在一个比a小且在矩阵中的数b满足条件,即从小于a的数变成了小于等于b的数 .
等用题目中的例子,x = 13 和x = 14 都满足小于等于x的元素数目等于8
对14来说统计的都是小于它的数, 而对13来说统计的都是小于等于它的数.
 问题来了, 那为何取到的不是14而是13呢?

因为我们取mid的取法是 mid = (left + right) / 2
当left < right时, mid 永远 取不到right, 想要mid取到right ,只有left == right.
 但循环条件是 while(left < right),当 left == right时循环已经终止. 所以我们得到会是一个左边界. 
 还是用题目中的例子, 假设left = 13, right = 14 则 mid = (13 + 14) / 2 = 13
'''


# 二分查找的次数为log(right-left)
# 每次二分都是O(N)
# 所以事件复杂度为 NlogN
# 值域二分法（好题啊）
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/you-xu-ju-zhen-zhong-di-kxiao-de-yuan-su-by-leetco/
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


# 自己的版本二分
# 这里要注意，求firstposition一定能够得到正确答案，因为如果是虚构的一个值，那么在所有的数中一定可以取到
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 二分
        if not matrix or not matrix[0]:
            return -1
        m = len(matrix)
        n = len(matrix[0])

        # 计算得到小于等于mid的个数
        def get_count(target):
            cnt = 0
            row = m - 1
            col = 0
            # 从左下角开始遍历
            while row >= 0 and col < n:
                if matrix[row][col] <= target:
                    cnt += row + 1
                    col += 1
                elif matrix[row][col] > target:
                    row -= 1
            return cnt

        right = matrix[m - 1][n - 1]  # matrix的最大值
        left = matrix[0][0]
        # 二分找firstposition
        while left + 1 < right:
            mid = left + (right - left) // 2
            # 小于等于 mid 的个数和 k 进行比较
            cnt = get_count(mid)
            # 相当于求f(mid) >= k 的first_position,因为是求first，所以一定可以取到正确答案
            if cnt >= k:
                right = mid
            else:
                left = mid
        if get_count(left) >= k:
            return left
        else:
            return right



