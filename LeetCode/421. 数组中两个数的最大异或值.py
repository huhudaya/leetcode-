'''
给定一个非空数组，数组中元素为 a0, a1, a2, … , an-1，其中 0 ≤ ai < 231 。
找到 ai 和aj 最大的异或 (XOR) 运算结果，其中0 ≤ i,  j < n 。

你能在O(n)的时间解决这个问题吗？

示例:
输入: [3, 10, 5, 25, 2, 8]
输出: 28
解释: 最大的结果是 5 ^ 25 = 28.
'''
from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        mask = 0
        for i in range(30, -1, -1):
            # 每一轮都会前进一次！
            mask |= (1 << i)  # 这里表示最高位是1，其余为0
            # 当前得到的所有前缀都放在这个哈希表中
            s = set()
            for num in nums:
                s.add(mask & num)  # 这里表示最高位是num本身的二进制

            # 先“贪心地”假设这个数位上是 “1” ，如果全部前缀都看完，都不符合条件，这个数位上就是 “0”
            temp = res | (1 << i)  # 或 有1即为1

            # 遍历每一个元素的最高位
            for prefix in s:
                # 如果找到一个
                if temp ^ prefix in s:  # 这里基于一个事实 0 于任何数异或还是它本身
                    res = temp
                    break
        return res
Solution().findMaximumXOR([3, 10, 5, 25, 2, 8])
