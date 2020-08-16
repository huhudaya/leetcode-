'''
在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。

每个矩形由其左下顶点和右上顶点坐标表示，如图所示。

示例:

输入: -3, 0, 3, 4, 0, -1, 9, 2
输出: 45
说明: 假设矩形面积不会超出 int 的范围。
'''


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        r12 = (C - A) * (D - B) + (G - E) * (H - F)
        if A > G or C < E or D < F or B > H:
            return r12
        else:
            x1 = max(A, E)
            x2 = min(C, G)
            y1 = max(B, F)
            y2 = min(D, H)
            return r12 - (y2 - y1) * (x2 - x1)


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        # 看投影
        # 总面积
        r12 = (C - A) * (D - B) + (G - E) * (H - F)
        res = 0
        rec_x_2 = min(G, C)
        rec_x_1 = max(A, E)
        rec_long = max(rec_x_2 - rec_x_1, 0)
        rec_y_1 = min(D, H)
        rec_y_2 = max(B, F)
        rec_high = max(rec_y_1 - rec_y_2, 0)
        res = rec_high * rec_long
        return r12 - res