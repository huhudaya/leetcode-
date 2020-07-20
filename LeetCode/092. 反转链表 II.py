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


# 递归，记录使用后继节点
class Solution:
    # 递归版本
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 全局变量
        self.successor = None

        # 反转前N个节点函数
        def reverseN(head, n):
            if n == 1:
                # 注意一定要注意保存这个后继节点
                self.successor = head.next
                return head
            last = reverseN(head.next, n - 1)
            head.next.next = head
            head.next = self.successor
            return last

        if m == 1:
            return reverseN(head, n)
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 非递归
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        # 此时pre指针指向第m - 1个节点
        for i in range(m - 1):
            pre = pre.next
        cur = pre.next
        tail = pre.next
        # 保存这个pre
        node = pre
        pre = None
        # 反转m-n 需要转n-m+1次
        for i in range(n - m + 1):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        node.next.next = cur
        node.next = pre
        return dummy.next


'''
思路二:
用三个指针,进行插入操作
例如:
1->2->3->4->5->NULL, m = 2, n = 4
将节点3插入节点1和节点2之间
变成: 1->3->2->4->5->NULL
再将节点4插入节点1和节点3之间
变成:1->4->3->2->5->NULL
实现翻转的效果!
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        # 找到翻转链表部分的前一个节点, 1->2->3->4->5->NULL, m = 2, n = 4 指的是 节点值为1
        for _ in range(m - 1):
            pre = pre.next
        # 用 pre, start, tail三指针实现插入操作
        # tail 是插入pre,与pre.next的节点
        start = pre.next
        tail = start.next
        for _ in range(n - m):
            start.next = tail.next
            tail.next = pre.next
            pre.next = tail
            tail = start.next
        return dummy.next
