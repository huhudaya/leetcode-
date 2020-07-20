'''
给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
通过次数2,896提交次数4,526
在真实的面试中遇到过这道题？
'''
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # 双指针优化版本
        # 只考虑当前的柱子
        if not height:
            return 0
        n = len(height)
        left = 0
        right = n - 1
        l_max = height[0]
        r_max = height[n-1]
        res = 0
        while left < right:
            # 更新左端和右端的最大值
            l_max = max(height[left], l_max)
            r_max = max(height[right], r_max)
            if height[left] < height[right]:
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1
        return res