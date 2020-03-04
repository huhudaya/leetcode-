'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Sloution:
    def deleteDuplicates(self, head: ListNode) -> None:
        if head is None:
            return
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
