# 61. 旋转链表.py
'''
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

链接：https://leetcode-cn.com/problems/rotate-list
'''


# 快慢指针

class Solution(object):
    """docstring for Solution"""

    def __init__(self, arg):
        super(Solution, self).__init__()
        self.arg = arg

    def rotateRight(self, head, k):
        if head == None or head.next == None or k == 0:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        n = 0
        while cur:
            n += 1
            cur = cur.next
        # 注意，这里需要求余数得到真正需要平移的次数
        k = k % n
        if k == 0:
            return head
        fast = slow = head
        for i in range(k):
            assert (fast != None)
            fast = fast.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next
        newNode = slow.next
        slow.next = None
        fast.next = head
        return newNode


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 穿针引线
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 特判
        if head is None or head.next is None or k <= 0:
            return head

        # 先看链表有多少元素
        node = head
        # 先数这个链表的长度
        counter = 1
        while node.next:
            node = node.next
            counter += 1

        k = k % counter
        if k == 0:
            return head
        # 很重要，先将尾部节点指向头结点，形成一个环！！！
        node.next = head
        node = head
        # 可以取一些极端的例子找到规律
        # counter - k - 1
        for _ in range(counter - k - 1):
            node = node.next
        new_head = node.next
        node.next = None
        return new_head
