'''
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false

链接：https://leetcode-cn.com/problems/search-a-2d-matrix
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row * col
        while left < right:
            mid = left + (right - left) // 2
            if matrix[mid // col][mid % col] < target:
                left = mid + 1
            else:
                right = mid
        #print(left,right)
        return left < row * col and matrix[left // col][left % col] == target

# 自己的版本
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 二分
        if matrix is None or len(matrix) == 0 or matrix[0] is None or len(matrix[0]) == 0:
            return False
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row * col - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if matrix[mid // col][mid % col] < target:
                left = mid
            elif matrix[mid // col][mid % col] > target:
                right = mid
            else:
                return True
        if matrix[left // col][left % col] == target:
            return True
        elif matrix[right // col][right % col] == target:
            return True
        else:
            return False