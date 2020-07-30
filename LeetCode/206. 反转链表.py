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


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 非递归
        pre = None
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return head


# 官方题解
class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next

        return hair.next


# 之间的版本
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# k个一组反转链表
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 递归反转
        # 递归三问：
        '''
        1.这个递归函数是干什么的，输入输出是什么
        2.递归函数的出口是什么
        3.递推关系是什么
        '''
        def reverse(head, k):
            if head is None:
                return None
            cnt = 0
            cur = head
            while cur and cnt != k:
                cur = cur.next
                cnt += 1
            # 此时cur指向下一组的第一个节点
            if cnt == k:
                pre = reverse(cur, k)
                # 反转前面的节点
                while cnt:
                    tmp = head.next
                    head.next = pre
                    pre = head
                    head = tmp
                    cnt -= 1
                head = pre
            return head
        return reverse(head, k)
