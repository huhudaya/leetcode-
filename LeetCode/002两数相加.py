# 002两数相加.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


'''
给出两个 非空 的链表用来表示两个非负的整数。
其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''
from typing import List


class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val


# 使用dummyNode
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur = dummy
        ca = 0
        while l1 or l2 or ca:
            if l1:
                ca += l1.val
                l1 = l1.next
            if l2:
                ca += l2.val
                l2 = l2.next
            k = ca % 10
            cur.next = ListNode(k)
            ca = ca // 10
            # 进位
            cur = cur.next
        return dummy.next


# go

'''
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
//go
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    // 准备一个dummy节点
	list := &ListNode{0, nil,}
    //这里用一个result，只是为了后面返回节点方便，并无他用
	result := list
	tmp := 0
	for l1 != nil || l2 != nil || tmp != 0 {
		if l1 != nil {
			tmp += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			tmp += l2.Val
			l2 = l2.Next
		}
		list.Next = &ListNode{tmp % 10, nil}
		tmp = tmp / 10
		list = list.Next
	}
	return result.Next
}
'''

'''
// type ListNode struct {
//     Val int
//     Next *ListNode
//  }
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    dummy := new(ListNode)
    curr := dummy
    carry := 0
    
    for (l1 != nil || l2 != nil || carry > 0) {
        curr.Next = new(ListNode)
        curr = curr.Next
        if l1 != nil {
            carry += l1.Val
            l1 = l1.Next
        }
        if l2 != nil {
            carry += l2.Val
            l2 = l2.Next
        }
        curr.Val = carry % 10 
        carry /= 10
    }
    return dummy.Next
}
'''