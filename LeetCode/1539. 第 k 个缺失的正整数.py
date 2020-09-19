'''

给你一个 严格升序排列 的正整数数组 arr 和一个整数 k 。

请你找到这个数组里第 k 个缺失的正整数。



示例 1：

输入：arr = [2,3,4,7,11], k = 5
输出：9
解释：缺失的正整数包括 [1,5,6,8,9,10,12,13,...] 。第 5 个缺失的正整数为 9 。
示例 2：

输入：arr = [1,2,3,4], k = 2
输出：6
解释：缺失的正整数包括 [5,6,7,...] 。第 2 个缺失的正整数为 6 。


提示：

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
对于所有 1 <= i < j <= arr.length 的 i 和 j 满足 arr[i] < arr[j]

'''
# 用count来为缺失数计数
# 当arr遍历完count仍然没有达到k时
# 即第k个缺数数在arr之外时的情况
# 直接返回arr[-1]+k-count
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        last = arr[-1]
        for i in range(1, last + 1):
            if i not in arr:
                count += 1
            if count == k:
                return i
        return last + k - count
