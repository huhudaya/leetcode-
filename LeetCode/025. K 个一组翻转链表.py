# 025. K 个一组翻转链表.py
'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
'''
# // # 反转链表K个一组递归.py


# // 相当于1->2->3反转为2->1->null
# 反转a,b之间的节点
# ListNode reverse(ListNode a, ListNode b) {
#     ListNode pre, cur, nxt;
#     pre = null; cur = a; nxt = a;
#     // while 终止的条件改一下就行了
#     while (cur != b) {
#         nxt = cur.next;
#         cur.next = pre;
#         pre = cur;
#         cur = nxt;
#     }
#     // 返回反转后的头结点
#     return pre;
# }


# // 解释一下 for 循环之后的几句代码，注意 reverse 函数是反转区间 [Node a, Node b)
# ListNode reverseKGroup(ListNode head, int k) {
#     if (head == null) return null;
#     // 区间 [a, b) 包含 k 个待反转元素
#     ListNode a, b;
#     a = b = head;
#     for (int i = 0; i < k; i++) {
#         // 不足 k 个，不需要反转，base case
#         if (b == null) return head;
#         b = b.next;
#     }
#     // 反转前 k 个元素
#     ListNode newHead = reverse(a, b);
#     // 递归反转后续链表并连接起来
#     a.next = reverseKGroup(b, k);
#     return newHead;
# }


# 尾插法
'''
pre
tail    head
dummy    1     2     3     4     5
# 我们用tail 移到要翻转的部分最后一个元素
pre     head       tail
dummy    1     2     3     4     5
	       cur
# 我们尾插法的意思就是,依次把cur移到tail后面
pre          tail  head
dummy    2     3    1     4     5
	       cur
# 依次类推
pre     tail      head
dummy    3     2    1     4     5
		cur
'''

# 尾插
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        tail = dummy
        while True:
            count = k
            while count and tail:
                count -= 1
                tail = tail.next
            if not tail:
                break
            head = pre.next
            while pre.next != tail:
                cur = pre.next  # 获取下一个元素
                # pre与cur.next连接起来,此时cur(孤单)掉了出来
                pre.next = cur.next
                cur.next = tail.next  # 和剩余的链表连接起来
                tail.next = cur  # 插在tail后面
            # 改变 pre tail 的值
            pre = head
            tail = head
        return dummy.next


# 递归
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head
        count = 0
        # 每次先遍历前k个节点
        while cur and count != k:
            cur = cur.next
            count += 1
        # 如果这一组的个数等于K,进行反转
        if count == k:
            # cur充当为翻转链表中的pre
            cur = self.reverseKGroup(cur, k)
            while count:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                count -= 1
            head = cur
        return head


# 栈
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        while True:
            count = k
            stack = []
            tmp = head
            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
            # 注意,目前tmp所在k+1位置
            # 说明剩下的链表不够k个,跳出循环
            if count:
                p.next = head
                break
            # 翻转操作
            while stack:
                p.next = stack.pop()
                p = p.next
            # 与剩下链表连接起来
            p.next = tmp
            head = tmp

        return dummy.next


# 迭代，空间复杂度为O(1)
class Solution:
    def reverseKGroup(self, head, k):
        '''
        :param head: ListNode
        :param k: int
        :return: ListNode
        '''
        if head == None or head.next == None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        # 保存上一组反转的最后一个节点
        pre = dummy
        while cur:
            cnt = 0
            # p 保存下一组的首节点
            p = cur
            while cnt < k and p:
                # p用来保存下一组链表的头结点
                p = p.next
                cnt += 1
            if cnt == k:
                # 此时cur为待翻转的一组链表的头节点，start=cur表示start为这一组翻转后的尾节点
                start = cur
                # 对 [cur, p)节点反转
                # q作为待翻转的一组链表的pre
                q = None
                # 翻转这一组节点，q作为这一组的pre
                for i in range(1, k + 1):
                    next = cur.next
                    cur.next = q
                    q = cur
                    cur = next
                # 翻转之后cur为
                start.next = p
                pre.next = q
                pre = start
            else:
                break
        return dummy.next