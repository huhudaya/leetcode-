# 315. 计算右侧小于当前元素的个数hard.py
'''
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例:

输入: [5,2,6,1]
输出: [2,1,1,0] 
解释:
5 的右侧有 2 个更小的元素 (2 和 1).
2 的右侧仅有 1 个更小的元素 (1).
6 的右侧有 1 个更小的元素 (1).
1 的右侧有 0 个更小的元素.
链接：https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self
'''
# 技巧 使用索引数组 索引数组index记录数组中第i位置的索引，根据原数组nums可以调整索引数组的位置
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # 使用索引数组
        n = len(nums)
        index = [i for i in range(n)]
        res = [0 for i in range(n)]
        # 归并
        self.__merge(nums, index, res)
        return res
    def __merge(self, nums, index, res):
        if len(index) <= 1:
            return
        mid = len(index) // 2
        # 两个新的空间
        left = index[:mid]
        right = index[mid:]
        self.__merge(nums, left, res)
        self.__merge(nums, right, res)
        i = 0
        j = 0
        k = 0
        # 归并逻辑处理
        while i < mid:
            while j < len(right) and nums[left[i]] > nums[right[j]]:
                j += 1
            res[left[i]] += j
            i += 1
        # 归并排序过程
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if nums[left[i]] < nums[right[j]]:
                index[k] = left[i]
                k += 1
                i += 1
            else:
                index[k] = right[j]
                k += 1
                j += 1
            # 总有一个越界
        while i < len(left):
            index[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            index[k] = right[j]
            k += 1
            j += 1