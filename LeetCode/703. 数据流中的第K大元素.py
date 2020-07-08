# 703. 数据流中的第K大元素.py
'''
设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。

你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器
它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。

示例:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
说明:
你可以假设 nums 的长度≥ k-1 且k ≥ 1。

链接：https://leetcode-cn.com/problems/kth-largest-element-in-a-stream
'''

'''
    heap = [] 定义一个空堆
    1,heapq.heappush(heap,x):向heap堆中添加元素
    2,heapq.heappop(heap)：弹出堆中最小的元素，并且维持剩余元素的堆结构
    3,heapq.heapify(heap)：将列表转换为堆
    4,heapq.heapreplace(heap, x)：弹出堆中最小的元素，然后将新元素插入。
    5,heapq.nlargest(n, iter)、nsmallest(n, iter)   注意，里面可以有key参数，作为一个函数
    用来寻找任何可迭代对象iter中的前n个最大的或前n个最小的元素。
'''
import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
