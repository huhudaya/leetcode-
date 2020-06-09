# 024. 两两交换链表中的节点.py
'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
'''


# 递归
class Solution(object):
    def swapPairs(self, head):
        # 递归的终止条件
        # if head == None or head.next == None:
        #  not AB <====> A + B
        if not (head and head.next):
            return head
        # 假设链表是 1->2->3->4
        # 这句就先保存节点2
        tmp = head.next
        # 继续递归，处理节点3->4
        # 当递归结束返回后，就变成了4->3
        # 于是head节点就指向了4，变成1->4->3
        head.next = self.swapPairs(tmp.next)
        # 将2节点指向1
        tmp.next = head
        return tmp


# 非递归，迭代
class Solution(object):
    def swapPairs(self, head):
        # 增加一个特殊节点方便处理
        p = ListNode(-1)
        # 创建a，b两个指针，这里还需要一个tmp指针
        a, b, p.next, tmp = p, p, head, p
        while b.next and b.next.next:
            # a前进一位，b前进两位
            a, b = a.next, b.next.next
            # 这步很关键，tmp指针用来处理边界条件的
            # 假设链表是1->2->3->4，a指向1，b指向2
            # 改变a和b的指向，于是就变成2->1，但是1指向谁呢？
            # 1是不能指向2的next，1应该指向4，而循环迭代的时候一次处理2个节点
            # 1和2的关系弄清楚了，3和4的关系也能弄清楚，但需要一个指针来处理
            # 2->1，4->3的关系，tmp指针就是干这个用的
            tmp.next, a.next, b.next = b, b.next, a
            # 现在链表就变成2->1->3->4
            # tmp和b都指向1节点，等下次迭代的时候
            # a就变成3，b就变成4，然后tmp就指向b，也就是1指向4
            tmp, b = a, a
        return p.next


#  自己的版本
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 简明的写法 非递归
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 两两交换,迭代
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        while cur and cur.next:
            q = cur.next
            r = q.next
            pre.next = q
            q.next = cur
            cur.next = r
            pre = cur
            cur = r
        return dummy.next
