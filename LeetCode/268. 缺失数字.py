# 268. 缺失数字.py
'''
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:

输入: [3,0,1]
输出: 2
示例 2:

输入: [9,6,4,2,3,5,7,0,1]
输出: 8
说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
'''
'''
给一个长度为 n 的数组，其索引应该在[0,n)，但是现在你要装进去 n + 1 个元素[0,n]
那么肯定有一个元素装不下嘛，请你找出这个缺失的元素。

这道题不难的，我们应该很容易想到，把这个数组排个序，然后遍历一遍，不就很容易找到缺失的那个元素了吗？

或者说，借助数据结构的特性，用一个 HashSet 把数组里出现的数字都储存下来，再遍历[0,n]之间的数字
去 HashSet 中查询，也可以很容易查出那个缺失的元素。

排序解法的时间复杂度是 O(NlogN)
HashSet的解法时间复杂度是 O(N)，但是还需要 O(N) 的空间复杂度存储 HashSet。

第三种方法是位运算。

对于异或运算（^）
我们知道它有一个特殊性质：一个数和它本身做异或运算结果为 0，一个数和 0 做异或运算还是它本身。

而且异或运算满足交换律和结合律，也就是说：

2 ^ 3 ^ 2 = 3 ^ (2 ^ 2) = 3 ^ 0 = 3

而这道题索就可以通过这些性质巧妙算出缺失的那个元素。比如说nums = [0,3,1,4]：
int missingNumber(int[] nums) {
    int n = nums.length;
    int res = 0;
    // 先和新补的索引异或一下
    res ^= n;
    // 和其他的元素、索引做异或
    # 注意异或的性质，0和任何数异或为本身，自己和自己异或是0
    for (int i = 0; i < n; i++)
        res ^= i ^ nums[i];
    return res;
}
'''
# 时间复杂度 O(N)，空间复杂度 O(1)
'''
如果这样想，说明我们受算法的毒害太深，随着我们学习的知识越来越多
反而容易陷入思维定式，这个问题其实还有一个特别简单的解法：等差数列求和公式。

题目的意思可以这样理解：现在有个等差数列 0, 1, 2,…, n，其中少了某一个数字，请你把它找出来。
那这个数字不就是sum(0,1,..n) - sum(nums)嘛？  类似于 137题
'''
'''
int missingNumber(int[] nums) {
    int n = nums.length;
    // 公式：(首项 + 末项) * 项数 / 2
    int expect = (0 + n) * (n + 1) / 2;

    int sum = 0;
    for (int x : nums) 
        sum += x;
    return expect - sum;
'''
# 优化

'''
假设缺失元素的位置补了一个 0，我们让每个索引减去其对应的元素，再把相减的结果加起来，不就是那个缺失的元素吗？
int missingNumber(int[] nums) {
    int n = nums.length;
    int res = 0;
    // 新补的索引
    res += n - 0;
    // 剩下索引和元素的差加起来
    for (int i = 0; i < n; i++) 
        res += i - nums[i];
    return res;
}
'''
from typing import List

class Solution:
    # def missingNumber(self, nums) -> int:
    #     n = len(nums)
    #     res = 0
    #     res ^= n
    #     for i in range(n):
    #         res ^= i ^ nums[i]
    #     return res
    def missingNumber(self, nums) -> int:
        n = len(nums)
        # 新补的索引
        res = n
        for i in range(n):
            # 对应的索引数组相减，最后的相减的结果就是缺失的那个数字
            res += i - nums[i]
        return res

