'''
编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。
如果链表中包含 x，x 只需出现在小于 x 的元素之后(如下所示)。
分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间。

示例:

输入: head = 3->5->8->5->10->2->1, x = 5
输出: 3->1->2->10->5->5->8
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 双指针
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 荷兰国旗双指针的思想
        left = head
        right = head
        while right:
            if right.val < x:
                left.val, right.val = right.val, left.val
                left = left.next
            right = right.next
        return head


# 快排的思想
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None:
            return head
        big = None
        small = None
        equal = None
        cur = head
        while cur:
            t = cur
            cur = cur.next
            if t.val < x:
                t.next = small
                small = t
            elif t.val > x:
                t.next = big
                big = t
            else:
                t.next = equal
                equal = t
        dummy = ListNode(-1)
        cur = dummy
        for node in [small, equal, big]:
            while node:
                cur.next = node
                node = node.next
                cur = cur.next
                cur.next = None
        return dummy.next
