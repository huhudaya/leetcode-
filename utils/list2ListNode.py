# list转链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def list2ListNode(list) -> ListNode:
    dummy = ListNode(-1)
    pre = dummy
    for i in list:
        pre.next = ListNode(i)
        pre = pre.next
    return dummy.next
