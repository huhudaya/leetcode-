# 002两数相加.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


'''
给出两个 非空 的链表用来表示两个非负的整数。
其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''
from typing import List
class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val
from queue import Queue
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = Queue()
        s2 = Queue()
        while l1:
            s1.put(l1.val)
            l1 = l1.next
        while l2:
            s2.put(l2.val)
            l2 = l2.next
        node = None
        pre = None
        head = None
        ca = 0
        n1 = 0
        n2 = 0
        #注意这里必须使用 not queue.empty()来判断队列是否为空
        while not s1.empty() or not s2.empty():
            n1 = s1.get() if not s1.empty() else 0
            n2 = s2.get() if not s2.empty() else 0
            n = n1 + n2 + ca
            # n % 10 即最低位
            node = ListNode(n % 10)
            # n // 10 即进位数
            ca = n//10
            if pre is None:
                node.next = pre
                pre = node
                head = node
            else:
                pre.next = node
                node.next = None
                pre = node 
        # 若s1 和 s2均为空
        if ca == 1:#进位为1
            node = ListNode(1)
            pre.next = node
            node.next = None
        return head






# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 优化
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ca = 0
        n1 = 0
        n2 = 0
        node = None
        pre = None
        c1 = l1
        c2 = l2
        while c1 or c2:
            n1 = c1.val if c1 else 0
            n2 = c2.val if c2 else 0
            # 对应位置的数字相加
            n = n1 + n2 + ca
            #n % 10 为余数 表示最低位
            node = ListNode(n % 10)
            if pre is None:
                node.next = pre
                pre = node
                head = node
            else:
                pre.next = node
                node.next = None
                pre = node
            ca = n//10
            c1 = c1.next if c1 else None
            c2 = c2.next if c2 else None
        if ca == 1:
            node = ListNode(1)
            pre.next = node
            node.next = None
        return head

# 使用dummyNode
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur = dummy
        ca = 0
        while l1 or l2 or ca:
            if l1:
                ca += l1.val
                l1 = l1.next
            if l2:
                ca += l2.val
                l2 = l2.next
            k = ca % 10
            cur.next = ListNode(k)
            ca = ca // 10
            # 进位
            cur = cur.next
        return dummy.next