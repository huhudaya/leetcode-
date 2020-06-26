# 206. 反转链表.py
'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

链接：https://leetcode-cn.com/problems/reverse-linked-list
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 非递归方法
    def reverseList1(self, head: ListNode) -> ListNode:
        pre = None
        next = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre
    # 递归方法
    def reverseList2(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        new_head = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return new_head
