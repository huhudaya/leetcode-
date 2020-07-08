'''
矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。
如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。
给出两个矩形，判断它们是否重叠并返回结果。

示例 1：
输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
输出：true

示例 2：
输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1]
输出：false
提示：
两个矩形 rec1 和 rec2 都以含有四个整数的列表的形式给出。
矩形中的所有坐标都处于 -10^9 和 10^9 之间。
x 轴默认指向右，y 轴默认指向上。
你可以仅考虑矩形是正放的情况。
'''

'''
我们尝试分析在什么情况下，矩形 rec1 和 rec2 没有重叠。

想象一下，如果我们在平面中放置一个固定的矩形 rec2，那么矩形 rec1 必须要出现在 rec2 的「四周」
也就是说，矩形 rec1 需要满足以下四种情况中的至少一种：

矩形 rec1 在矩形 rec2 的左侧；

矩形 rec1 在矩形 rec2 的右侧；

矩形 rec1 在矩形 rec2 的上方；

矩形 rec1 在矩形 rec2 的下方。

何为「左侧」？如果矩形 rec1 在矩形 rec2 的左侧
那就表示我们可以找到一条竖直的线（可以与矩形的边重合）
使得矩形 rec1 和 rec2 被分在这条竖线的两侧
对于「右侧」、「上方」以及「下方」，它们的定义与「左侧」是类似的

算法

我们将上述的四种情况翻译成代码。具体地，我们用 (rec[0], rec[1]) 表示矩形的左下角
(rec[2], rec[3]) 表示矩形的右上角，与题目描述一致。对于「左侧」
即矩形 rec1 在 x 轴上的最大值不能大于矩形 rec2 在 x 轴上最小值
对于「右侧」、「上方」以及「下方」同理。因此我们可以翻译成如下的代码：

左侧：rec1[2] <= rec2[0]；

右侧：rec1[0] >= rec2[2]；

上方：rec1[1] >= rec2[3]；

下方：rec1[3] <= rec2[1]。
'''


# 逆向思维
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        return not (rec1[2] <= rec2[0] or  # left 第一个矩形的右上角x小于等于第二个矩形的左下角x
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])  # top


'''
如果两个矩形重叠，那么它们重叠的区域一定也是一个矩形
那么这代表了两个矩形与 x 轴平行的边（水平边）投影到 x 轴上时会有交集
与 y 轴平行的边（竖直边）投影到 y 轴上时也会有交集
因此，我们可以将问题看作一维线段是否有交集的问题


矩形 rec1 和 rec2 的水平边投影到 x 轴上的线段分别为 (rec1[0], rec1[2]) 和 (rec2[0], rec2[2])
根据数学知识我们可以知道，当 min(rec1[2], rec2[2]) > max(rec1[0], rec2[0]) 时这两条线段有交集
对于矩形 rec1 和 rec2 的竖直边投影到 y 轴上的线段
同理可以得到，当 min(rec1[3], rec2[3]) > max(rec1[1], rec2[1]) 时，这两条线段有交集
'''

# 转换为在 X 轴和 Y 轴是否有交集
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)

        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and
                intersect(rec1[1], rec1[3], rec2[1], rec2[3]))



# 自己
from typing import List
class Solution1:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # 逆向思维
        return not (
                rec1[2] <= rec2[0]  # left
                or
                rec1[3] <= rec2[1]  # bottom
                or
                rec1[0] >= rec2[2]  # right
                or
                rec1[1] >= rec2[3]  # top
        )


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # 投影到 X和Y 轴看交集
        def intersect(x1, x2, x3, x4):
            return min(x2, x4) > max(x1, x3)

        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2])  # X轴
                and
                intersect(rec1[1], rec1[3], rec2[1], rec2[3])
                )
