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
'''