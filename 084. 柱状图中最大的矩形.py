# 084. 柱状图中最大的矩形.py
'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
示例:

输入: [2,1,5,6,2,3]
输出: 10

链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram
'''
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if heights is None or len(heights) == 0:
            return 0
        # 单调栈 min
        stack = []
        maxArea = 0
        n = len(heights)
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                j = stack.pop()
                k = stack[-1] if stack else -1
                curArea = (i - k - 1) * heights[j]
                maxArea = max(maxArea, curArea)
            stack.append(i)
        while stack:
            j = stack.pop()
            k = stack[-1] if stack else -1
            curArea = (n - k - 1) * heights[j]
            maxArea = max(maxArea, curArea)
        return maxArea