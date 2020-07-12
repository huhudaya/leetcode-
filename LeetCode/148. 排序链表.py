# 148. 排序链表.py
'''
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5

链接：https://leetcode-cn.com/problems/sort-list
'''

'''
归并排序的思想：
首先将数据分为两部分，对这两部分的数据进行行排序
然后将两部分排序好的数组进行归并（有一种 O(N) 时间复杂度的方法可以实现）
归并排序的思想对于链表这种不支持随机存取的数据结构也是支持的
所以刚好可以符合时间复杂度 O(NlogN) 的要求。
我们可以使用快慢指针的方法找到中间节点
然后分别对链表的左右两边进行归并排序,最后进行 merge 操作
和并两个有序链表，可以用 O(N) 的时间复杂度完成。
'''
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 归并
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        pre, slow, fast = None, head, head
        # 找到中间节点以及中间节点前一个节点，这里的中间节点是后边界
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        #  * 是解包的操作
        return self.mergeTwoLists(*map(self.sortList, (head, slow)))

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2


# 快排
class Solution(object):
    def sortList(self, head):

        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = ListNode(0)
        newHead.next = head
        self.quicksort(newHead, None)
        return newHead.next

    def partition(self, start, end):
        node = start.next.next
        pivotPrev = start.next
        pivotPrev.next = end
        pivotPost = pivotPrev
        while node != end:
            temp = node.next
        if node.val > pivotPrev.val:
            node.next = pivotPost.next
            pivotPost.next = node
        elif node.val < pivotPrev.val:
            node.next = start.next
            start.next = node
        else:
            node.next = pivotPost.next
            pivotPost.next = node
            pivotPost = pivotPost.next
        node = temp
        return [pivotPrev, pivotPost]

    def quicksort(self, start, end):
        if start.next != end:
            prev, post = self.partition(start, end)
        self.quicksort(start, prev)
        self.quicksort(post, end)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 自己的版本
class Solution():
    """docstring for Solution"""

    def sortList(self, head):
        if head is None or head.next is None:
            return head
        # 快慢指针找到中点和中间节点前一个节点
        fast = head
        slow = head
        pre = None
        if fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        list_1 = self.sortList(head)
        list_2 = self.sortList(head2)
        return self.mergeTwoLists(list_1, list_2)

    # # 递归
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     if not l1 or not l2:
    #         return l1 if l1 else l2
    #     if l1.val < l2.val:
    #         l1.next = self.mergeTwoLists(l1.next, l2)
    #         return l1
    #     else:
    #         l2.next = self.mergeTwoLists(l1, l2.next)
    #         return l2
    # 非递归
    def mergeTwoLists(self, list_1, list_2):
        dummy = ListNode(-1)
        p = list_1
        q = list_2
        cur = dummy
        while p != None and q != None:
            if p.val < q.val:
                cur.next = p
                p = p.next
            else:
                cur.next = q
                q = q.next
            cur = cur.next
        if p is None:
            cur.next = q
        if q is None:
            cur.next = p
        return dummy.next


# 堆排序
import heapq


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        ptr = head
        p_queue = []
        heapq.heapify(p_queue)
        while ptr != None:
            heapq.heappush(p_queue, ptr.val)
            ptr = ptr.next
        ptr = head
        while p_queue:
            ptr.val = heapq.heappop(p_queue)
            ptr = ptr.next
        return head

# 快速排序
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        # 分成三个链表，分别是比轴心数小，相等，大的数组成的链表
        big = None
        small = None
        equal = None
        cur = head
        while cur is not None:
            t = cur
            cur = cur.next
            if t.val < head.val:
                t.next = small
                small = t
            elif t.val > head.val:
                t.next = big
                big = t
            else:
                t.next = equal
                equal = t

        # 拆完各自排序即可，equal 无需排序
        big = self.sortList(big)
        small = self.sortList(small)

        ret = ListNode(None)
        cur = ret

        # 将三个链表组合成一起，这一步复杂度是 o(n)
        # 可以同时返回链表的头指针和尾指针加速链表的合并。
        for p in [small, equal, big]:
            while p is not None:
                cur.next = p
                p = p.next
                cur = cur.next
                cur.next = None
        return ret.next
