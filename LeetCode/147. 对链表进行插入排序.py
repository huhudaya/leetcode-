# 147. 对链表进行插入排序.py
'''
对链表进行插入排序。


插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。


链接：https://leetcode-cn.com/problems/insertion-sort-list
'''
'''
从链表头部开始遍历，记录当前要插入排序的节点和其上一个节点，对每个节点执行如下操作：

从头部开始找到当前节点之前第一个不大于它的节点，记录找到的节点以及它前一个节点

如果它前一个节点为空，说明要插入到头节点之前，若不为空，则插入到该节点之后

继续进行下一次插入排序，直到遍历到链表尾部
'''


class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    """docstring for Solution"""

    def insertionSortList(self, head):
        if head == None or head.next == None:
            return head
        dummyNode = ListNode(-1)
        dummyNode.next = head
        cur = head.next
        head.next = None
        # pre 保存待插入元素的前一个位置
        while cur:
            pre = dummyNode
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            # tmp 保存待插入链表中的下一个节点
            tmp = pre.next
            # q 保存原始链表中待插入点的下一个节点
            q = cur.next
            pre.next = cur
            cur.next = tmp
            cur = q
        return dummyNode.next


# 从头开始 这个道题就像排队,先找个排头dummy,然后依次从head节点放入dummy,只需要依次dummy现有节点比较,插入其中!
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 找个排头
        dummy = ListNode(-1)
        # 注意不要将dummy.next = head,此时dummy.next = None
        # 为什么要设置为None呢？因为此时的队尾就是none，要将cur插入到dummy开头的链表中,当前这个链表的终点是none
        pre = dummy
        # 依次拿head节点
        cur = head
        while cur:
            # 把下一次节点保持下来
            tmp = cur.next
            # 找到插入的位置的前一个位置
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            # 进行插入操作
            cur.next = pre.next
            pre.next = cur
            # 插入完成之后继续将pre移动到dummy位置
            pre = dummy
            # cur指针指向下一个节点
            cur = tmp
        return dummy.next


# tail插法
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 找个排头
        dummy = ListNode(float("-inf"))
        pre = dummy
        tail = dummy
        # 依次拿head节点
        cur = head
        while cur:
            if tail.val < cur.val:
                tail.next = cur
                tail = cur
                cur = cur.next
            else:
                # 把下一次节点保持下来
                tmp = cur.next
                tail.next = tmp
                # 找到插入的位置
                while pre.next and pre.next.val < cur.val:
                    pre = pre.next
                # 进行插入操作
                cur.next = pre.next
                pre.next = cur
                pre = dummy
                cur = tmp
        return dummy.next
