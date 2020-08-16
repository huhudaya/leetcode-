'''
假设你有两个数组，一个长一个短，短的元素均不相同。
找到长数组中包含短数组所有的元素的最短子数组，其出现顺序无关紧要。

返回最短子数组的左端点和右端点，如有多个满足条件的子数组，返回左端点最小的一个。若不存在，返回空数组。

示例 1:

输入:
big = [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]
small = [1,5,9]
输出: [7,10]
示例 2:

输入:
big = [1,2,3]
small = [4]
输出: []
'''
import sys
from typing import List
from collections import defaultdict


class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        # 滑动窗口
        hash = defaultdict(int)
        for i in small:
            hash[i] += 1
        left = 0
        m = len(big)
        n = len(small)
        if n > m:
            return []
        cnt = 0
        max_len = sys.maxsize
        res = []
        for i in range(m):
            hash[big[i]] -= 1
            if hash[big[i]] >= 0:
                cnt += 1
            # 移动左指针,指向第一个有意义的值的索引位置
            while left < i and hash[big[left]] < 0:
                hash[big[left]] += 1
                left += 1
            if cnt == n and max_len > i - left + 1:
                max_len = i - left + 1
                if res == [] or (res and left > res[0]):
                    res = [left, i]
        return res
