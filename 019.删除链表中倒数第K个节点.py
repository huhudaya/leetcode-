'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None and n < 1:
            return False
        cur = head
        while cur:
            n -= 1
            cur = cur.next
        if n == 0:
            head = head.next
        # 需要找到前一个
        if n < 0:
            cur = head
            while n + 1 != 0:
                n += 1
                cur = cur.next
            cur.next = cur.next.next
        return head

# 一次遍历法
'''
public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    ListNode first = dummy;
    ListNode second = dummy;
    // Advances first pointer so that the gap between first and second is n nodes apart
    for (int i = 1; i <= n + 1; i++) {
        first = first.next;
    }
    // Move first to the end, maintaining the gap
    while (first != null) {
        first = first.next;
        second = second.next;
    }
    second.next = second.next.next;
    return dummy.next;
}
'''


# 重点是找见K-N的节点，然后删除K-N+1的节点，这里用dummy节点会方便很多
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 假设总共有K个节点
        # 核心思想是找到第K-N个节点，然后删除下一个节点，即K-N+1的节点
        # 这里使用dummy节点的话会很方便,因为最后还有None节点，所以其实总共需要遍历K+1次
        # 为了找到K-N个节点，即遍历K-N次，需要先找到N+1个几点，然后遍历K+1-(N-1)次
        dummy = ListNode(-1)
        fast = dummy
        slow = dummy
        dummy.next = head
        for i in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next