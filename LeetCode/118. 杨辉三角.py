'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。
示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        def dfs(numRows):
            for i in range(numRows):
                path = [0 for i in range(i + 1)]
                path[0] = 1
                path[-1] = 1
                for j in range(1, i):
                    path[j] = res[i - 1][j - 1] + res[i - 1][j]
                res.append(path[:])
            return res

        return dfs(numRows)
