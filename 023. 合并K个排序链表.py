# 23. 合并K个排序链表.py
'''
方法一：贪心算法、优先队列
思路分析：

1、由于是 k 个排序链表，那么这 k 个排序的链表头结点中 val 最小的结点就是合并以后的链表中最小的结点；

2、最小结点所在的链表的头结点就要更新了，更新成最小结点的下一个结点（如果有的话），此时还是这 kk 个链表，这 kk 个排序的链表头结点中 val 最小的结点就是合并以后的链表中第 22 小的结点。

写到这里，我想你应该差不多明白了，我们每一次都从这 kk 个排序的链表头结点中拿出 val 最小的结点“穿针引线”成新的链表，这个链表就是题目要求的“合并后的排序链表”。“局部最优，全局就最优”，这不就是贪心算法的思想吗。

这里我们举生活中的例子来理解这个思路。

假设你是一名体育老师，有 33 个班的学生，他们已经按照身高从矮到高排好成了 33 列纵队，现在要把这 33 个班的学生也按照身高从矮到高排列 11 列纵队。我们可以这么做：

1、让 33 个班的学生按列站在你的面前，这时你能看到站在队首的学生的全身；
2、每一次队首的 33 名同学，请最矮的同学出列到“队伍4”（即我们最终认为排好序的队列），出列的这一列的后面的所有同学都向前走一步（其实走不走都行，只要你能比较出站在你面前的 3 位在队首的同学同学的高矮即可）；
3、重复第 2 步，直到 33 个班的同学全部出列完毕。

具体实现的时候，“每一次队首的 33 名同学，请最矮的同学出列”这件事情可以交给优先队列（最小堆、最小索引堆均可）去完成。在连续的两次出队之间完成“穿针引线”的工作。

下面的图解释了上面的思路。

（温馨提示：下面的幻灯片中，有几页上有较多的文字，可能需要您停留一下，可以点击右下角的后退 “|◀” 或者前进 “▶|” 按钮控制幻灯片的播放。）

Python3 代码：Python3 的 heapq 模块传入的 tuple 对象里面不能有引用对象，就只好传一个索引进去了。
Java 代码：保留了一些调试代码。
# Python3 下的代码
from typing import List
import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l = []
        size = len(lists)

        for index in range(size):
            # 针对一些特殊的测试用例，有的链表可能是空链表
            if lists[index]:
                heapq.heappush(l, (lists[index].val, index))

        dummy_node = ListNode(-1)
        cur = dummy_node

        while l:
            _, index = heapq.heappop(l)

            # 定位到此时应该出列的那个链表的头结点
            head = lists[index]
            # 开始“穿针引线”
            cur.next = head
            cur = cur.next
            # 同样不要忘记判断到链表末尾结点的时候
            if head.next:
                # 刚刚出列的那个链表的下一个结点成为新的链表头结点加入优先队列
                heapq.heappush(l, (head.next.val, index))
                # 切断刚刚出列的那个链表的头结点引用
                lists[index] = head.next
                head.next = None
        return dummy_node.next
'''
# 暴力法
'''
遍历所有链表，将所有节点的值放到一个数组中。
将这个数组排序，然后遍历所有元素得到正确顺序的值。
用遍历得到的值，创建一个新的有序链表。
时间复杂度O(NlogN)
空间复杂度O(N)
'''
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        dummy = ListNode(-1)
        pre = dummy
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            pre.next = ListNode(x)
            pre = pre.next
        return dummy.next

# 优先队列----穿针引线
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 使用heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            if lists[i] :
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next

# ----------------------------------------------------------------
# 两两合并链表 递归
'''
时间复杂度O(KN),其中K是链表的数目
空间复杂度O(1)
'''
# 分治
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    # 合并两个有序链表 非递归版本
    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next

# 递归&分治=========>归并的思想
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:return 
        n = len(lists)
        return self.merge(lists, 0, n-1)
    def merge(self,lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)
    # 递归
    def mergeTwoLists(self,l1, l2):
        if not l1:return l2
        if not l2:return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
    # 非递归
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_node = ListNode(-1)
        p1 = l1
        p2 = l2
        # 因为涉及到head节点，所以设置一个dummy节点来避免边界情况
        cur = dummy_node
        while p1 and p2:
            if p1.val < p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next
        if p1 is None:
            cur.next = p2
        if p2 is None:
            cur.next = p1
        return dummy_node.next