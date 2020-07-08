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




# 字典树
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Compute length L of max number in a binary representation
        L = len(bin(max(nums))) - 2
        # zero left-padding to ensure L bits for each number
        nums = [[(x >> i) & 1 for i in range(L)][::-1] for x in nums]

        max_xor = 0
        trie = {}
        for num in nums:
            node = trie
            xor_node = trie
            curr_xor = 0
            for bit in num:
                # insert new number in trie
                if not bit in node:
                    node[bit] = {}
                node = node[bit]

                # to compute max xor of that new number
                # with all previously inserted
                '''
                如果当前比特值存在互补比特值，访问具有互补比特值的孩子节点，并在异或值最右侧附加一个 1
                如果不存在，直接访问具有当前比特值的孩子节点，并在异或值最右侧附加一个 0
                '''
                toggled_bit = 1 - bit
                if toggled_bit in xor_node:
                    curr_xor = (curr_xor << 1) | 1
                    xor_node = xor_node[toggled_bit]
                else:
                    curr_xor = curr_xor << 1
                    xor_node = xor_node[bit]

            max_xor = max(max_xor, curr_xor)

        return max_xor

# 作者：powcai
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # 创建前缀树
        root = {}
        for num in nums:
            cur = root
            for i in range(31, -1, -1):
                cur_bit = (num >> i) & 1
                cur.setdefault(cur_bit, {})
                cur = cur[cur_bit]

        res = float("-inf")
        # 按位找最大值
        for num in nums:
            # 此时的cur为前缀树的根节点
            cur = root
            cur_max = 0
            for i in range(31, -1, -1):
                # 相当于得到将当前num的二进制的第i位
                cur_bit = (num >> i) & 1
                # 因为 a ^ b = max, max ^ a = b,先假设异或的结果是1，看能与之异或的值是否在前缀字典中
                if cur_bit ^ 1 in cur:
                    cur_max += (1 << i)
                    cur = cur[cur_bit ^ 1]
                else:
                    cur = cur[cur_bit]
            res = max(res, cur_max)
        return res

Solution().findMaximumXOR([3, 10, 5, 25, 2, 8])
