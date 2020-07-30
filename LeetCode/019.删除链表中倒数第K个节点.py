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

'''
上述算法可以优化为只使用一次遍历。
我们可以使用两个指针而不是一个指针。
第一个指针从列表的开头向前移动 n+1 步，而第二个指针将从列表的开头出发。
现在，这两个指针被 n 个结点分开。
我们通过同时移动两个指针向前来保持这个恒定的间隔，直到第一个指针到达最后一个结点。
此时第二个指针将指向从最后一个结点数起的第 n 个结点。此时慢指针是倒数第N+1个节点
(因为快指针和慢指针永远相差N，所以当快指针走到最后一个节点，这个时候慢指针离最后一个节点的距离仍然是N!)
我们重新链接第二个指针所引用的结点的 next 指针指向该结点的下下个结点。
'''


# 重点是找见K-N的节点，然后删除K-N+1的节点，这里用dummy节点会方便很多
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 这种方法不是很好理解，建议用第二种
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 核心思路就是利用双指针，先进行一次循环，将fast和slow两个指针的间隔设置为n,然后同时移动两个指针
        # 这样相当于两个指针的间隔一直不变，一直是n,然后进行删除操作就可以了
        dummy = ListNode(-1)
        fast = dummy
        slow = dummy
        dummy.next = head
        # 这里fast指针先走n + 1步，相当于fast现在指向第n+1个节点，现在fast和slow这两个指针的间隔为n+1
        for i in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        # 核心思路就是利用双指针，先进行一次循环，将fast和slow两个指针的间隔设置为n,然后同时移动两个指针
        # 这样相当于两个指针的间隔一直不变，一直是n,然后进行删除操作就可以了
        dummy = ListNode(-1)
        fast = dummy
        slow = dummy
        dummy.next = head
        # 这里fast指针先走n步，相当于fast现在指向第n个节点
        for i in range(n):
            fast = fast.next
        # 注意这里需要判断一下.next指针是否为null
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        fast = dummy
        slow = dummy
        dummy.next = head
        for i in range(n):
            fast = fast.next
        # 这里的条件为fast.next,则最后fast会落在倒数第1个节点上
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next