# 54. 螺旋矩阵.py
'''
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

链接：https://leetcode-cn.com/problems/spiral-matrix
'''

from typing import List


# 模拟螺旋矩阵的形式
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_len = len(matrix)
        column_len = len(matrix[0])
        # 模拟顺时针
        row_index = [0, 1, 0, -1]
        column_index = [1, 0, -1, 0]
        # seen 矩阵很重要 用来缩圈,触壁就拐弯，同时也可以在当单行单列的时候，用seen防止重复添加元素
        seen = [[False] * column_len for i in range(row_len)]
        res = []
        row = 0
        column = 0
        # direction = 0
        di = 0
        for i in range(row_len * column_len):
            res.append(matrix[row][column])
            seen[row][column] = True
            # 判断下一个前进的方向
            rr = row + row_index[di]
            cc = column + column_index[di]
            # 在范围且没有被访问过,注意必须是 0 <= rr
            if 0 <= rr < row_len and 0 <= cc < column_len and not seen[rr][cc]:
                row = rr
                column = cc
            else:
                di = (di + 1) % 4
                row = row + row_index[di]
                column = column + column_index[di]
        return res


# 精简版本
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(map(list, zip(*matrix)))[::-1]
        return res


# java
# 根据左上角和右下角
'''
class Solution {
    public List < Integer > spiralOrder(int[][] matrix) {
        List ans = new ArrayList();
        if (matrix.length == 0)
            return ans;
        int r1 = 0, r2 = matrix.length - 1;
        int c1 = 0, c2 = matrix[0].length - 1;
        while (r1 <= r2 && c1 <= c2) {
            for (int c = c1; c <= c2; c++) ans.add(matrix[r1][c]);
            for (int r = r1 + 1; r <= r2; r++) ans.add(matrix[r][c2]);
            //这里不判断的话，单行或者单列的时候会多添加数字。为了往左走，往上走
            if (r1 < r2 && c1 < c2) {
                for (int c = c2 - 1; c > c1; c--) ans.add(matrix[r2][c]);
                for (int r = r2; r > r1; r--) ans.add(matrix[r][c1]);
            }
            r1++;
            r2--;
            c1++;
            c2--;
        }
        return ans;
    }
}
'''


# 按圈遍历
class Solution(object):
    def spiralOrder(self, matrix):
        def spiral_coords(r1, c1, r2, c2):
            for c in range(c1, c2 + 1):
                yield r1, c
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1

        if not matrix:
            return []
        ans = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coords(r1, c1, r2, c2):
                ans.append(matrix[r][c])
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
        return ans


# java 计算圈数
'''
public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> list = new ArrayList<Integer>();
        if(matrix == null || matrix.length == 0)
    		return list;
        int m = matrix.length;
        int n = matrix[0].length;
        int i = 0; 

        //统计矩阵从外向内的层数，如果矩阵非空，那么它的层数至少为1层
        int count = (Math.min(m, n)+1)/2;
        //从外部向内部遍历，逐层打印数据
        while(i < count) {
        	for (int j = i; j < n-i; j++) {
				list.add(matrix[i][j]);
			}
        	for (int j = i+1; j < m-i; j++) {
				list.add(matrix[j][(n-1)-i]);
			}
        	
        	for (int j = (n-1)-(i+1); j >= i && (m-1-i != i); j--) {
				list.add(matrix[(m-1)-i][j]);
			}
        	for (int j = (m-1)-(i+1); j >= i+1 && (n-1-i) != i; j--) {
				list.add(matrix[j][i]);
			}
        	i++;
        }    
        return list;
    }
'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        m = len(matrix)
        n = len(matrix[0])
        layer_num = (min(m, n) + 1) // 2  # 总共有多少层
        res_list = []  # 保存结果
        for lr in range(layer_num):
            start = lr  # 该层左上角的位置(start, start)
            last_col = n - lr - 1  # 该层最后一列的索引
            last_row = m - lr - 1  # 该层最后一行的索引

            for c in range(start, last_col + 1):  # from left to right
                res_list.append(matrix[start][c])
            for r in range(start + 1, last_row + 1):  # from top to bottom
                res_list.append(matrix[r][last_col])

            if last_row != start and last_col != start:
                for c1 in range(last_col - 1, start - 1, -1):  # from right to bottom
                    res_list.append(matrix[last_row][c1])
                for r1 in range(last_row - 1, start, -1):  # from bottom to top
                    res_list.append(matrix[r1][start])
        return res_list


class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])  # 行，列

        # 1. 横向遍历m，纵向遍历n-1；
        # 2. 横向遍历m-1，纵向遍历n-2；
        # 3. 横向遍历m-2，纵向遍历n-3；
        # 4. 直到有一方向遍历长度为0时终止。

        ans = []
        judge = 1  # 1为顺序遍历，-1为逆序遍历
        i, j = 0, -1  # 初始位置，列为-1，因为代表[0,0]前一个位置
        while m > 0 and n > 0:

            # 横向遍历
            for x in range(n):
                j += judge * 1
                ans.append(matrix[i][j])

            # 纵向遍历
            for y in range(m - 1):
                i += judge * 1
                ans.append(matrix[i][j])

            # 每遍历一次，m 和 n 都要减少一次，
            m = m - 1
            n = n - 1
            # 每一轮横向和纵向遍历完之后，需要拐点，即col方向减少，row方向减少
            judge *= -1

        return ans


# 好方法
# 将已经走过的地方置0，然后拐弯的时候判断一下是不是已经走过了，如果走过了就计算一下新的方向：
def solution(matrix):
    r, i, j, di, dj = [], 0, 0, 0, 1
    if matrix != []:
        m = len(matrix)
        n = len(matrix[0])
        for _ in range(m * n):
            r.append(matrix[i][j])
            # 走过了就置为0
            matrix[i][j] = 0
            # di的初始值是1
            if matrix[(i + di) % m][(j + dj) % n] == 0:
                di, dj = dj, -di
            i += di
            j += dj
    return r


# solution([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])


# 回溯
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 这里多加一个上的方向
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, 0]]
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        marked = [[False] * n for i in range(m)]
        res = []

        def flag(x, y):
            return 0 <= x < m and 0 <= y < n and not marked[x][y]

        def dfs(matrix, i, j, m, n, marked):
            marked[i][j] = True
            res.append(matrix[i][j])
            start = 1
            # 向左 和 向下 都不能使用的话，说明是最左边的那一列，优先搜索 上 即可
            if not flag(i, j - 1) and not flag(i + 1, j):
                start = 0
            for di in range(start, 5):
                x = i + directions[di][0]
                y = j + directions[di][1]
                if 0 <= x < m and 0 <= y < n and not marked[x][y]:
                    dfs(matrix, x, y, m, n, marked)

        dfs(matrix, 0, 0, m, n, marked)
        return res


# Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])


# 按圈遍历
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order



class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        res = []
        m = len(matrix)
        n = len(matrix[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        seen = [[False] * n for _ in range(m)]
        row = 0
        col = 0
        di = 0
        # 注意这里需要为m * n + 1
        for i in range(m * n + 1):
            res.append(matrix[row][col])
            # 记录是否已经遍历过
            seen[row][col] == True
            rr = row + directions[di][0]
            cc = col + directions[di][1]
            if rr < 0 or rr >= m or cc < 0 or cc >= n or seen[rr][cc]:
                di = (di + 1) % 4
            row += directions[di][0]
            col += directions[di][1]
        return res
Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])