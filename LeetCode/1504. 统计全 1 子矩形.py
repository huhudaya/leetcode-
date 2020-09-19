'''
给你一个只包含 0 和 1 的 rows * columns 矩阵 mat ，请你返回有多少个 子矩形 的元素全部都是 1 。

 

示例 1：

输入：mat = [[1,0,1],
            [1,1,0],
            [1,1,0]]
输出：13
解释：
有 6 个 1x1 的矩形。
有 2 个 1x2 的矩形。
有 3 个 2x1 的矩形。
有 1 个 2x2 的矩形。
有 1 个 3x1 的矩形。
矩形数目总共 = 6 + 2 + 3 + 1 + 1 = 13 。
示例 2：

输入：mat = [[0,1,1,0],
            [0,1,1,1],
            [1,1,1,0]]
输出：24
解释：
有 8 个 1x1 的子矩形。
有 5 个 1x2 的子矩形。
有 2 个 1x3 的子矩形。
有 4 个 2x1 的子矩形。
有 2 个 2x2 的子矩形。
有 2 个 3x1 的子矩形。
有 1 个 3x2 的子矩形。
矩形数目总共 = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24 。
示例 3：

输入：mat = [[1,1,1,1,1,1]]
输出：21
示例 4：

输入：mat = [[1,0,1],[0,1,0],[1,0,1]]
输出：5
 

提示：

1 <= rows <= 150
1 <= columns <= 150
0 <= mat[i][j] <= 1
'''
from typing import List

'''
定义二维dp[i][j], 表示第i行从(i,j)向左连续1的个数。
对于每个(i,j)，把元素(i,j)作为能组成矩阵的右下角元素，从当前行往前遍历计算结果。
具体参见代码，时间复杂度O(n*n*m)。
'''


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0

        rows, cols = len(mat), len(mat[0])
        dp = [[0] * cols for _ in range(rows)]  # DP 初始化

        ans = 0
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]:
                    dp[i][j] = ((dp[i][j - 1] + 1) if j > 0 else 1)
                    mmin = float('inf')
                    for k in range(i, -1, -1):  # 从i开始遍历,到0结束, 计算能组成的矩阵个数
                        mmin = min(mmin, dp[k][j])
                        ans += mmin

                        # 提前结束循环
                        if mmin == 0:
                            break
        return ans
