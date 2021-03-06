'''
给你一个整数数组 nums，请你将该数组升序排列。

 

示例 1：

输入：nums = [5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
'''

# 快排
from typing import List
import random


class Solution:
    def randomized_partition(self, nums, l, r):
        # 找一个随机数
        pivot = random.randint(l, r)
        # 和最后一个元素进行交换
        nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l - 1
        # 从小到大进行排序，将值小于nums[r]的值放在左边
        for j in range(l, r):
            if nums[j] < nums[r]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def randomized_quicksort(self, nums, l, r):
        if r - l <= 0:
            return
        mid = self.randomized_partition(nums, l, r)
        self.randomized_quicksort(nums, l, mid - 1)
        self.randomized_quicksort(nums, mid + 1, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums


# 堆排序
class Solution:
    def max_heapify(self, heap, root, heap_len):
        p = root
        while p * 2 + 1 < heap_len:
            l, r = p * 2 + 1, p * 2 + 2
            if heap_len <= r or heap[r] < heap[l]:
                nex = l
            else:
                nex = r
            if heap[p] < heap[nex]:
                heap[p], heap[nex] = heap[nex], heap[p]
                p = nex
            else:
                break

    def build_heap(self, heap):
        for i in range(len(heap) - 1, -1, -1):
            self.max_heapify(heap, i, len(heap))

    def heap_sort(self, nums):
        self.build_heap(nums)
        for i in range(len(nums) - 1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.max_heapify(nums, 0, i)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.heap_sort(nums)
        return nums


# 归并排序
class Solution:
    def merge_sort(self, nums, l, r):
        if l == r:
            return
        mid = (l + r) // 2
        self.merge_sort(nums, l, mid)
        self.merge_sort(nums, mid + 1, r)
        # 归并
        tmp = []
        i, j = l, mid + 1
        while i <= mid or j <= r:
            if i > mid or (j <= r and nums[j] < nums[i]):
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        nums[l: r + 1] = tmp

    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums


# 归并
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.sortHelper(nums)
        return nums

    def sortHelper(self, nums):
        if len(nums) <= 1:
            return
        mid = len(nums) // 2
        # 此时为一个新的列表
        left_nums = nums[:mid]
        right_nums = nums[mid:]
        self.sortHelper(left_nums)
        self.sortHelper(right_nums)
        i = j = k = 0
        # 归并
        while i < len(left_nums) and j < len(right_nums):
            if left_nums[i] < right_nums[j]:
                # 注意，此时直接对nums进行修改
                nums[k] = left_nums[i]
                i += 1
            else:
                nums[k] = right_nums[j]
                j += 1
            k += 1
        # 总有一个要越界
        while i < len(left_nums):
            nums[k] = left_nums[i]
            i += 1
            k += 1
        while j < len(right_nums):
            nums[k] = right_nums[j]
            j += 1
            k += 1


# 快排
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 快速排序
        def partition(left, right):
            left_old = left
            temp = nums[left]
            # 指针交换法
            while left < right:
                while left < right and nums[right] >= temp:
                    right -= 1
                while left < right and nums[left] <= temp:
                    left += 1
                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]
            nums[left], nums[left_old] = nums[left_old], nums[left]
            return left

        # 挖坑法
        def partition2(left, right):
            rand_int = random.randint(left, right)
            nums[left], nums[rand_int] = nums[rand_int], nums[left]
            left_old = left
            temp = nums[left_old]
            while left < right:
                while left < right and nums[right] >= temp:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] <= temp:
                    left += 1
                nums[right] = nums[left]
            nums[left] = temp
            return left

        def quick_sort(nums, left, right):
            if left < right:
                index = partition2(left, right)
                quick_sort(nums, left, index - 1)
                quick_sort(nums, index + 1, right)

        n = len(nums)
        quick_sort(nums, 0, n - 1)
        return nums
