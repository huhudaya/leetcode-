'''
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:

输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:

输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
 

说明：

题目保证链表中节点的值互不相同
若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点
链接：https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
                return dummy.next
            p = p.next
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # 哨兵
        tempnode = ListNode(0)
        tempnode.next = head
        # pre表示之前的节点，cur表示当前的头结点
        pre, cur = tempnode, head
        while cur:
            # 如果当前遍历节点的值等于目标节点值，则将pre.next=cur.next
            # 如果当前遍历的节点不等于目标值，则将pre指向当前节点；最后cur.next
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return tempnode.next