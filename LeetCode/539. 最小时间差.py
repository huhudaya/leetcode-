'''
给定一个 24 小时制（小时:分钟）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。

示例 1：
输入: ["23:59","00:00"]
输出: 1

备注:
列表中时间数在 2~20000 之间。
每个时间取值在 00:00~23:59 之间。
'''
from typing import List

# 转化成分钟数，最小的分钟+1440（第二天的第一个时间）再加入到排序数组末尾，最后比较差值
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        d = set()
        for c in timePoints:
            k = int(c[: 2]) * 60 + int(c[3:])
            if k in d:  # 可能快在了判重这里
                return 0
            d.add(k)
        d = sorted(d)
        d.append(d[0] + 1440)
        return min(d[i] - d[i - 1] for i in range(1, len(d)))
