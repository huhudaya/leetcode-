'''
给你一个整数数组 arr 和一个目标值 target ，请你返回一个整数 value 
使得将数组中所有大于 value 的值变成 value 后，数组的和最接近  target （最接近表示两者之差的绝对值最小）。

如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。
请注意，答案不一定是 arr 中的数字。

示例 1：

输入：arr = [4,9,3], target = 10
输出：3
解释：当选择 value 为 3 时，数组会变成 [3, 3, 3]，和为 9 ，这是最接近 target 的方案。
示例 2：

输入：arr = [2,3,5], target = 10
输出：5
示例 3：

输入：arr = [60864,25176,27249,21296,20204], target = 56803
输出：11361
'''

from typing import List
import bisect


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)

        r, ans, diff = max(arr), 0, target
        for i in range(1, r + 1):
            it = bisect.bisect_left(arr, i)
            cur = prefix[it] + (n - it) * i
            if abs(cur - target) < diff:
                ans, diff = i, abs(cur - target)
        return ans

# 自己的版本
'''
那么 value 值的上下界是多少呢？我们需要进行一些分析：
value 的下界为 0。这是因为当 value = 0 时，数组的和为 0。由于 target 是正整数，因此当 value 继续减小时，数组的和也会随之减小，且变为负数（这个和等于 value * n，其中 n 是数组 arr 的长度），并不会比 value = 0 时更接近 target。
value 的上界为数组 arr 中的最大值。这是因为当 value >= arr 时，数组中所有的元素都不变，因为它们均不大于 value。由于我们需要找到最接近 target 的最小 value 值，因此我们只需将数组 arr 中的最大值作为上界即可。
'''
# 关键是找上界和下界
import sys
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        # 前缀和数组和后缀数组
        prefix_arr = [0] * n
        for i in range(1, n):
            prefix_arr[i] = prefix_arr[i - 1] + arr[i - 1]
        # 二分遍历
        left = 0
        right = arr[-1]
        res = 0
        diff = sys.maxsize
        for i in range(right + 1):
            index = bisect.bisect_left(arr, i)
            tmp = prefix_arr[index] + (n - index) * i
            if abs(tmp - target) < diff:
                res = i
                diff = abs(tmp - target)
        return res
Solution().findBestValue([4,9,3],10)
