# 143. 重排链表.py
'''
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

链接：https://leetcode-cn.com/problems/reorder-list
'''

'''
首先利用快慢指针得到中间节点
然后将后一半的链表链表进行翻转（对中间过后的链表进行翻转
之后将前面的链表和翻转后的链表进行交叉合并即可
'''
class Solution:
	def reorderList(self, head):
		if head == None or head.next == None or head.next.next == None:
			return
		dummy = ListNode(-1)
		dummy.next = head
		pre = dummy
		fast = dummy
		slow = dummy
		# 找到中间节点  下边界
		while fast != None and fast.next != None:
			slow = slow.next
			fast = fast.next.next
		p = slow.next
		slow.next = None
		# 对中间节点过后的链表进行反转
		pre = None
		cur = p
		while cur:
			next = cur.next
			cur.next = pre
			pre = cur
			cur = next
		# 交叉合并
		cur = pre
		p = head
		# 可以不去理会链表长度是奇偶性这些边界问题
		while cur:
			temp = p.next
			next = cur.next
			p.next = cur
			cur.next = temp
			p = temp
			cur = next
		
			