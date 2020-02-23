# 234. 回文链表.py
'''
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

链接：https://leetcode-cn.com/problems/palindrome-linked-list
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 仅用有限几个变量
        if head is None or head.next is None:
            return True
        slow = head
        fast = head
        # 快慢指针遍历
        while fast.next and fast.next.next:
            slow = slow.next        #中间节点
            fast = fast.next.next   #结尾节点
        cur = slow.next #右部分第一个节点
        # 中间节点指向None
        slow.next = None 
        pre = slow
        # 反转右半区
        while cur:
            next = cur.next
            cur.next = pre 
            pre = cur
            cur = next
        tail = pre # 保留最后一个节点
        right = pre
        left = head
        res = True
        # 检查是否是回文
        while left and right:
            if left.val != right.val:
                res = False
                break
            left = left.next
            right = right.next
        # 恢复原来的链表
        pre = tail
        cur = tail.next
        tail.next = None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return res

'''
    public boolean isPalindrome(ListNode head) {
        if(head == null || head.next == null) {
            return true;
        }
        ListNode slow = head, fast = head;
        ListNode pre = head, prepre = null;
        while(fast != null && fast.next != null) {
            pre = slow;
            slow = slow.next;
            fast = fast.next.next;
            pre.next = prepre;
            prepre = pre;
        }
        if(fast != null) {
            slow = slow.next;
        }
        while(pre != null && slow != null) {
            if(pre.val != slow.val) {
                return false;
            }
            pre = pre.next;
            slow = slow.next;
        }
        return true;
    }
'''



class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 边界条件不用忘记了
        if not (head and head.next):
            return True
        # p = dummy
        p = ListNode(-1)
        p.next = head
        low = p
        fast = p
        # 快慢指针不断迭代，找到中间节点
        while fast and fast.next:
            low,fast = low.next, fast.next.next
        cur = low.next
        pre = None
        low.next = None
        #将链表一分为二之后，反转链表后半部分
        while cur:
            cur.next,pre,cur = pre,cur,cur.next
        a,b = p.next,pre
        # 将链表前半部分和 反转的后半部分对比
        while b:
            if a.val!=b.val:
                return False
            a,b = a.next,b.next
        return True