'''
为了提高自己的代码能力，小张制定了 LeetCode 刷题计划，他选中了 LeetCode 题库中的 n 道题，编号从 0 到 n-1，并计划在 m 天内按照题目编号顺序刷完所有的题目（注意，小张不能用多天完成同一题）。

在小张刷题计划中，小张需要用 time[i] 的时间完成编号 i 的题目。此外，小张还可以使用场外求助功能，通过询问他的好朋友小杨题目的解法，可以省去该题的做题时间。为了防止“小张刷题计划”变成“小杨刷题计划”，小张每天最多使用一次求助。

我们定义 m 天中做题时间最多的一天耗时为 T（小杨完成的题目不计入做题总时间）。请你帮小张求出最小的 T是多少。

示例 1：

输入：time = [1,2,3,3], m = 2

输出：3

解释：第一天小张完成前三题，其中第三题找小杨帮忙；第二天完成第四题，并且找小杨帮忙。这样做题时间最多的一天花费了 3 的时间，并且这个值是最小的。

示例 2：

输入：time = [999,999,999], m = 4

输出：0

解释：在前三天中，小张每天求助小杨一次，这样他可以在三天内完成所有的题目并不花任何时间。
限制：
1 <= time.length <= 10^5
1 <= time[i] <= 10000
1 <= m <= 1000
'''
# 给定一个数组，将其划分成 M 份，使得每份元素之和最大值最小，每份可以任意减去其中一个元素。
from typing import List


class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        # 给定一个limit 求对应的时间.这里需要减去每天最大的那个元素，可以使用滑动窗口的思想
        def get_num(limit, n):
            l = 0
            r = 0
            cnt = 0
            while r < n:
                tmp = 0
                max_value = 0
                while r < n:
                    tmp += time[r]
                    if max_value < time[r]:
                        max_value = time[r]
                    if tmp - max_value > limit:
                        break
                    r += 1
                cnt += 1
                l = r
            return cnt

        nums = time
        n = len(nums)
        # 注意，left这里需要初始化为0，不是max(nums)
        left = 0
        right = sum(nums)
        while left + 1 < right:
            mid = left + (right - left) // 2
            # 相当于找小于等于m的lastposition
            if get_num(mid, n) <= m:
                right = mid
            else:
                left = mid
        if get_num(left, n) <= m:
            return left
        if get_num(right, n) <= m:
            return right
        return -1


Solution().minTime([1, 2, 3, 3], 2)
