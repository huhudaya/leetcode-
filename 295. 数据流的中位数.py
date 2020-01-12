# 295. 数据流的中位数.py
'''
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
进阶:

如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？

链接：https://leetcode-cn.com/problems/find-median-from-data-stream
'''
# 大根堆+小根堆
import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap1 = [] # 大顶堆
        self.heap2 = [] # 小顶堆

    def addNum(self, num: int) -> None:
        if not self.heap1 and not self.heap2:
            heapq.heappush(self.heap2,num)
            return
        if num >= self.heap2[0]:
            # 加入小顶堆
            if len(self.heap1) == len(self.heap2) or len(self.heap1) == len(self.heap2)+1:
                heapq.heappush(self.heap2,num)
            # 调整+加入小顶堆
            elif len(self.heap1) == len(self.heap2)-1:
                ltop = heapq.heappop(self.heap2)
                heapq.heappush(self.heap1,-ltop)
                heapq.heappush(self.heap2,num)
        else:
            # 加入大顶堆
            if len(self.heap1) == len(self.heap2) or len(self.heap1) == len(self.heap2)-1:
                heapq.heappush(self.heap1,-num)
            # 调整+加入大顶堆(或小顶堆)
            elif len(self.heap1) == len(self.heap2)+1:
                if num <= -self.heap1[0]:
                    stop = heapq.heappop(self.heap1)
                    heapq.heappush(self.heap2,-stop)
                    heapq.heappush(self.heap1,-num)
                else:
                    heapq.heappush(self.heap2,num)

        #print(self.heap1,self.heap2)

    def findMedian(self) -> float:
        if len(self.heap1) == len(self.heap2):
            return (-self.heap1[0]+self.heap2[0])/2
        elif len(self.heap1) == len(self.heap2)+1:
            return -self.heap1[0]
        elif len(self.heap1) == len(self.heap2)-1:
            return self.heap2[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# 二分
import bisect
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.data, num)

    def findMedian(self) -> float:
        n = len(self.data)
        mid = (n - 1) // 2
        if n % 2 == 1:
            return self.data[mid]
        else:
            return (self.data[mid] + self.data[mid + 1]) / 2

# 堆
'''
思路二：堆

我们用两个堆， 一个最小堆，一个最大堆

我们把数据分成两部分，求中位数就是前半部分的最大值，后半部分的最小值。

当数据流为奇数个时候，说明最小堆个数，和最大堆个数要不一样，我们把这个数放在哪个堆里，其实都一样的，这里我放在后半部分（最小堆）

我们每次入堆，都有从另一个堆里挤出一个元素，保证最小堆和最大堆是数据流前后两部分

插入时间复杂度：O(log(n)

查找：O(1)
'''
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        else:
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return self.min_heap[0]

'''
1、  数据是如何在两个堆之间流动的,脑子里要建立如下动态的过程:
	为了找到添加新数据以后,数据流的中位数，我们让这个新数据在大顶堆和小顶堆中都走了一遍。
	而为了让大顶堆的元素多 11 个，我们让从小顶堆中又拿出一个元素“送回”给大顶堆

'''
# 大小根堆
import heapq
class MedianFinder:
    def __init__(self):
        # 当前大顶堆和小顶堆的元素个数之和
        self.count = 0
        self.max_heap = []
        self.min_heap = []
    def addNum(self, num: int) -> None:
        self.count += 1
        # 因为 Python 中的堆默认是小顶堆，所以要传入一个 tuple，用于比较的元素需是相反数，
        # 才能模拟出大顶堆的效果
        heapq.heappush(self.max_heap, (-num, num))
        _, max_heap_top = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, max_heap_top)
        if self.count & 1:
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, (-min_heap_top, min_heap_top))
    def findMedian(self) -> float:
        if self.count & 1:
            # 如果两个堆合起来的元素个数是奇数，数据流的中位数大顶堆的堆顶元素
            return self.max_heap[0][1]
        else:
            # 如果两个堆合起来的元素个数是偶数，数据流的中位数就是各自堆顶元素的平均值
            return (self.min_heap[0] + self.max_heap[0][1]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


'''
import java.util.PriorityQueue;

public class MedianFinder {

    /**
     * 当前大顶堆和小顶堆的元素个数之和
     */
    private int count;
    private PriorityQueue<Integer> maxheap;
    private PriorityQueue<Integer> minheap;

    /**
     * initialize your data structure here.
     */
    public MedianFinder() {
        count = 0;
        maxheap = new PriorityQueue<>((x, y) -> y - x);
        minheap = new PriorityQueue<>();
    }

    public void addNum(int num) {
        count += 1;
        maxheap.offer(num);
        minheap.add(maxheap.poll());
        // 如果两个堆合起来的元素个数是奇数，小顶堆要拿出堆顶元素给大顶堆
        if ((count & 1) != 0) {
            maxheap.add(minheap.poll());
        }
    }

    public double findMedian() {
        if ((count & 1) == 0) {
            // 如果两个堆合起来的元素个数是偶数，数据流的中位数就是各自堆顶元素的平均值
            return (double) (maxheap.peek() + minheap.peek()) / 2;
        } else {
            // 如果两个堆合起来的元素个数是奇数，数据流的中位数大顶堆的堆顶元素
            return (double) maxheap.peek();
        }
    }
}
'''
class MedianFinder:

    def __init__(self):
        # 当前大顶堆和小顶堆的元素个数之和
        self.count = 0
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        self.count += 1
        # 因为 Python 中的堆默认是小顶堆，所以要传入一个 tuple，用于比较的元素需是相反数，
        # 才能模拟出大顶堆的效果
        heapq.heappush(self.max_heap, -num)
        max_heap_top = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, -max_heap_top)
        # 判断奇偶性质
        if self.count & 1:
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_heap_top)

    def findMedian(self) -> float:
        if self.count & 1:
            # 如果两个堆合起来的元素个数是奇数，数据流的中位数大顶堆的堆顶元素
            return -self.max_heap[0]
        else:
            # 如果两个堆合起来的元素个数是偶数，数据流的中位数就是各自堆顶元素的平均值
            return (self.min_heap[0] - self.max_heap[0]) / 2