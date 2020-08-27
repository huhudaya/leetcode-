# lines = input().strip().split(",")
# arrs = lines[0]
# m = lines[1]
# print(arrs)
# print(m)
arrs = [4, 3, 5, 10, 12]
m = 2
import functools
import sys


class Solution:
    def get_res(self, nums, m):
        @functools.lru_cache(None)
        def get_res1(i, m):
            n = len(nums)
            if n == 0:
                return 0
            if m == 0:
                return 0
            if m == 1:
                return sum(nums[i:])
            res = sys.maxsize
            for j in range(n):
                res = min(res, max(sum(nums[i:j + 1]), get_res1(j + 1, m - 1)))
            return res

        return get_res1(0, m)


print(Solution().get_res(arrs, m))
