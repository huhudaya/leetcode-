'''
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

 

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。
给定 target = 20，返回 false。
限制：
0 <= n <= 1000
0 <= m <= 1000
注意：本题与主站 240 题相同：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
'''
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if not array: return False
        m, n = len(array), len(array[0])
        row, col = m - 1, 0
        while row >= 0 and col < n:
            if array[row][col] < target:
                col += 1
            elif array[row][col] > target:
                row -= 1
            else:
                return True
        return False


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == None or len(matrix) == 0 or matrix[0] == None or len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        # 初始化为右上角
        i = 0
        j = n - 1
        # 时间复杂度O(M+N) 空间复杂度O(1)
        while i < m and j >= 0:
            if target > matrix[i][j]:
                i += 1
            elif target < matrix[i][j]:
                j -= 1
            else:
                return True
        return False