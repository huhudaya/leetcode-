'''
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

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
  [15, 13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''


# 简单的思路 转置+反转
# 方法 1 ：转置加翻转
# 转置是行变列
# 最直接的想法是先转置矩阵，然后翻转每一行。这个简单的方法已经能达到最优的时间复杂度O(N^2)
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        # transpose matrix  这里的i表示第几行
        for i in range(n):
            for j in range(i, n):  # 这里的j表示第几列开始
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

                # reverse each row
        for i in range(n):
            matrix[i].reverse()


# 思路二
'''
思路二: 翻转

直接举例子:

翻转整个数组,再按正对角线交换两边的数

[                    [                  [
  [1,2,3],             [7,8,9],            [7,4,1],
  [4,5,6],    ---->    [4,5,6], ----->     [8,5,2],
  [7,8,9]              [1,2,3]             [9,6,3] 
]                    ]                  ]
这道题是顺时针的,那么逆时针呢?也是一样的
'''
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix[:] = matrix[::-1]
        # print(matrix)
        for i in range(0, n):
            for j in range(i + 1, n):
                # print(i, j)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
