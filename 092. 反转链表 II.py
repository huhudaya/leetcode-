# 92. 反转链表 II.py
'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 递归版本
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 全局变量
        self.successor = None
        # 反转前N个节点函数
        def reverseN(head, n):
            if n == 1:
                self.successor = head.next
                return head
            last = reverseN(head.next, n-1)
            head.next.next = head
            head.next = self.successor
            return last
        if m == 1:
            return reverseN(head,n)
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head
class Solution:
    # 非递归版本
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 重点是找到m前一个pre
        cur = head
        pre = None
        tail = None
        cnt = 0
        while cur:
            cnt += 1
            pre = cur if cnt == m - 1 else pre
            tail = cur if cnt == n + 1 else tail
            cur = cur.next
        if m > n or m < 1 or n > cnt:
            return head
        start = head if pre is None else pre.next
        cur = start.next
        start.next = tail
        # 反转逻辑
        while cur != tail:
            next = cur.next
            cur.next = start
            start = cur
            cur = next
        if pre:
            # fuck 我这里写成了"=="。。。。黑人问号脸
            pre.next = start
            return head
        return start


# 简约解法
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    	# 定义虚拟头结点
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy     
        for _ in range(m-1):
            pre = pre.next
     
        node = pre
        cur = pre.next
     
        for _ in range(n-m+1):
            cur.next, cur, pre = pre, cur.next, cur
        
        node.next.next = cur
        node.next = pre
        return dummy.next