# 使用dummy节点
'''
1、使用dummy的技巧
dummy = ListNode(-1)
dummy.next = head
pre = dummy
cur = head
while cur:
    xxxx
    cur = cur.next

# 遍历到第n个节点，则需要对head节点遍历 n-1 次
while n > 1:
    n -= 1
    cur = cur.next
或则
for i in range(n):
    pre = pre.next



链表中
使用了dummy,然后dummy.next = head
这样取中间节点的时候
下边界
fast,slow = head,head
while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
上边界
fast,slow = dummy
while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
'''

