'''
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。
将这两数相加会返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
 

示例：
输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        dummy = ListNode(-1)

        #
        def push_stack(p, stack):
            while p:
                stack.append(p.val)
                p = p.next

        push_stack(l1, stack1)
        push_stack(l2, stack2)
        # 记录进位
        carry = 0
        while stack1 or stack2 or carry:
            tmp1, tmp2 = 0, 0
            if stack1:
                tmp1 = stack1.pop()
            if stack2:
                tmp2 = stack2.pop()
            carry, mod = divmod(tmp1 + tmp2 + carry, 10)
            # 头插法
            new_node = ListNode(mod)
            new_node.next = dummy.next
            dummy.next = new_node
        return dummy.next
