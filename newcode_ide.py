# lines = input().strip().split(",")
# arrs = lines[0]
# m = lines[1]
# print(arrs)
# print(m)
arrs = [4, 3, 5, 10, 12]
m = 5
import functools
import sys
class Solution:
    def get_res(self, nums, m):
        def get_res1(nums, m):
            n = len(nums)
            if n == 0:
                return 0
            if m == 0:
                return 0
            if m == 1:
                return sum(nums)
            res = sys.maxsize
            for i in range(n):
                res = min(res, max(sum(nums[:i + 1]), self.get_res(nums[i + 1:], m - 1)))
            return res
        return get_res1(nums, m)

print(Solution().get_res(arrs, m))
