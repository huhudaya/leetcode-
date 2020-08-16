'''
给你个整数数组 arr，其中每个元素都 不相同。

请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。

 

示例 1：

输入：arr = [4,2,1,3]
输出：[[1,2],[2,3],[3,4]]
示例 2：

输入：arr = [1,3,6,10,15]
输出：[[1,3]]
示例 3：

输入：arr = [3,8,-10,23,19,-4,-14,27]
输出：[[-14,-10],[19,23],[23,27]]
 

提示：

2 <= arr.length <= 10^5
-10^6 <= arr[i] <= 10^6
'''
from typing import List
import sys


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # 使用hash
        n = len(arr)
        arr.sort()
        hash = {}
        min_diff = sys.maxsize
        for i in range(n - 1):
            diff = abs(arr[i] - arr[i + 1])
            if diff not in hash:
                hash[diff] = []
            hash[diff].append([arr[i], arr[i + 1]])
            min_diff = min(min_diff, diff)
        return hash[min_diff]


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mindiff = arr[1] - arr[0]
        res = [[arr[0], arr[1]]]
        for i in range(2, len(arr)):
            curdiff = arr[i] - arr[i - 1]
            if curdiff < mindiff:
                res = [[arr[i - 1], arr[i]]]
                mindiff = curdiff
            elif curdiff == mindiff:
                res.append([arr[i - 1], arr[i]])
        return res


from collections import defaultdict


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_map = defaultdict(list)
        arry_min_val = float("inf")
        for i in range(len(arr) - 1):
            min_val = abs(arr[i + 1] - arr[i])
            arry_min_val = min(min_val, arry_min_val)
            min_map[min_val].append([arr[i], arr[i + 1]])

        return min_map[arry_min_val]
