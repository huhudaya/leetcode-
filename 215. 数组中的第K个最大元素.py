# 215. 数组中的第K个最大元素.py
'''
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
'''
# 堆排序
# 默认是小根堆
# 时间复杂度 : O(Nlogk)。
# 空间复杂度 : O(k)，用于存储堆元素。
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            if len(heap) < k:
                heapq.heappush(heap,i)
            elif heap[0] < i:
                heapq.heapreplace(heap,i)
        return heap[0]


# 堆排序简易版本
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[-1]

# 快排
from random import randint
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return
        index = randint(0,len(nums)-1)
        pivot = nums[index]
        less_part = [i for i in nums[:index]+nums[index+1:] if i < pivot]
        great_part = [i for i in nums[:index]+nums[index+1:] if i >= pivot]
        if len(great_part) == k-1:
            return pivot
        elif len(great_part) > k-1:
            return self.findKthLargest(great_part,k)
        else:
            return self.findKthLargest(less_part,k-len(great_part)-1)

# 快排
# 快速选择算法 的平均时间复杂度为 O(N)。就像快速排序那样，本算法也是 Tony Hoare 发明的，因此也被称为 Hoare选择算法。
'''
复杂度分析

时间复杂度 : 平均情况 O(N)，最坏情况 O(N^2)。
空间复杂度 : O(1)。
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            pivot = nums[left]
            l = left + 1
            r = right
            while l <= r:
                if nums[l] < pivot and nums[r] > pivot:
                    nums[l], nums[r] = nums[r], nums[l]
                if nums[l] >= pivot:
                    l += 1
                if nums[r] <= pivot:
                    r -= 1
            nums[r], nums[left] = nums[left], nums[r]
            return r
        left = 0
        right = len(nums) - 1
        while 1:
            idx = partition(left, right)
            if idx == k - 1:
                return nums[idx]
            if idx < k - 1:
                left = idx + 1
            if idx > k - 1:
                right = idx - 1
# --------------------------------------------------------------
# 使用快排完成topK
# 挖坑法
def partition(arr,low,high):
	# 必须使用一个index 作为一个基准值 默认取数组的第一个位置的元素作为index
	index = arr[low]
	while low < high:
		while arr[high] <= index and low < high:
			high-=1
		arr[low] = arr[high]
		while arr[low] > index and low < high:
			low+=1
		arr[high] = arr[low]
	arr[low] = index
	return low
# 快排
# def quickSort(arr,low,high):
# 	if low < high:
# 		key = partition(arr,low,high)
# 		quickSort(arr,0,key-1)
# 		quickSort(arr,key+1,high)
# arr = [1,3,4,3,2,5,3]
# quickSort(arr,0,len(arr)-1)
# print(arr)

# 指针交换法 
def partition1(arr,l,r):
	index = arr[l]
	low = l
	while l < r :
		while l < r and arr[r] <= index:
			r-=1
		while l < r and arr[l] >= index:
			l+=1
		if l < r:
			arr[l],arr[r] = arr[r],arr[l]
	arr[l],arr[low] = arr[low],arr[l]
	return l

# topK
# 思路 利用快排求topK
def topK(arr,k,low,high):
	pos = partition(arr,low,high)
	# cnt = pos - low + 1
	if pos < k:
		return topK(arr,k,pos+1,high)  #注意写 return 我刚开始没写return 导致出错
# arr = [1,3,4,3,2,5,3]
	elif pos > k:
		return topK(arr,k,0,pos-1)
	return arr[pos]