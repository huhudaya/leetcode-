# 021合并两个有序链表.py
'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
'''
# 非递归
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
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

# 递归 穿针引线方法
#include <iostream>
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 if l1 else l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# 自己的版本
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 链表类的题一定注意边界特殊值的判断
        if l1 == None or l2 == None:
            return l1 if l1 != None else l2
        head =l1 if l1.val < l2.val else l2
        cur1 = l1 if head == l1 else l2
        cur2 = l2 if head == l1 else l1
        pre = None
        next = None
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                pre = cur1
                cur1 = cur1.next
            else:
                next = cur2.next
                pre.next = cur2
                cur2.next = cur1
                # pre始终指向cur1的前一个指针
                pre = cur2 
                cur2 = next
        # 若cur1不为空，即cur2为空，则pre指向cur1
        pre.next = cur1 if cur1 else cur2
        return head