'''

平面上有 n 个点，点的位置用整数坐标表示 points[i] = [xi, yi]。
请你计算访问所有这些点需要的最小时间（以秒为单位）。

你可以按照下面的规则在平面上移动：

每一秒沿水平或者竖直方向移动一个单位长度，或者跨过对角线（可以看作在一秒内向水平和竖直方向各移动一个单位长度）。
必须按照数组中出现的顺序来访问这些点。


示例 1：
输入：points = [[1,1],[3,4],[-1,0]]
输出：7
解释：一条最佳的访问路径是： [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]
从 [1,1] 到 [3,4] 需要 3 秒
从 [3,4] 到 [-1,0] 需要 4 秒
一共需要 7 秒
示例 2：

输入：points = [[3,2],[-2,2]]
输出：5

提示：
points.length == n
1 <= n <= 100
points[i].length == 2
-1000 <= points[i][0], points[i][1] <= 1000
'''
# 切比雪夫距离
from typing import List

'''
对于平面上的两个点 x = (x0, x1) 和 y = (y0, y1)
设它们横坐标距离之差为 dx = |x0 - y0|，纵坐标距离之差为 dy = |x1 - y1|
对于以下三种情况，我们可以分别计算出从 x 移动到 y 的最少次数：
    dx < dy：沿对角线移动 dx 次，再竖直移动 dy - dx 次，总计 dx + (dy - dx) = dy 次；
    dx == dy：沿对角线移动 dx 次；
    dx > dy：沿对角线移动 dy 次，再水平移动 dx - dy 次，总计 dy + (dx - dy) = dx 次。
其实是一个，数学问题，因为走斜线和走横竖一个值，所以直接取x or y值的最大
因为走对角线等于走一格x和一格y，所以走对角线是最优先的，并且这里的对角线就是 x or y 的最大值
'''


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x0, x1 = points[0]
        ans = 0
        for i in range(1, len(points)):
            y0, y1 = points[i]
            ans += max(abs(x0 - y0), abs(x1 - y1))
            x0, x1 = points[i]
        return ans
