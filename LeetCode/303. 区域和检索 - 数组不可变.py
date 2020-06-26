'''
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
说明:

你可以假设数组不可变。
会多次调用 sumRange 方法。

'''

from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        # 构造前缀和
        self.dp = [0]
        for num in nums:
            self.dp.append(self.dp[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j + 1] - self.dp[i]

class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.dp =[0 for _ in range(n + 1)]
        for i in range(n):
            self.dp[i + 1] = self.dp[i] + nums[i]
    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j + 1] - self.dp[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)