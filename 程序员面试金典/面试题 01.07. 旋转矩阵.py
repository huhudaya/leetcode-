'''
给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。

不占用额外内存空间能否做到？

 

示例 1:

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

'''
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return
        m = len(matrix)
        n = len(matrix[0])
        nums = matrix
        def reverse(left, right, nums):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        for i in range(m):
            for j in range(i, n):
                nums[i][j], nums[j][i] = nums[j][i], nums[i][j]
        for i in range(m):
            reverse(0, n - 1, matrix[i])