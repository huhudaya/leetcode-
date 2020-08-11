'''
编写一个函数，检查输入的链表是否是回文的。

示例 1：
输入： 1->2
输出： false

示例 2：
输入： 1->2->2->1
输出： true

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 快慢指针
        slow = head
        fast = head
        if not (head and head.next):
            return True
        # 上边界
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        cur = slow.next
        pre = None
        slow.next = None
        # 反转后半部分
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        # 比较两部分链表
        right = pre
        left = head
        while right:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        return True
