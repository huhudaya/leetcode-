'''
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。
进阶：
你是否可以不用额外空间解决此题？
'''
'''
作者：星__尘
链接：https://www.nowcoder.com/discuss/428158?source_id=profile_create&channel=2002
来源：牛客网

1.若两个单链表一个为有环,一个无环. 那么肯定不能相交.
2.若二者都没有环, 问题就转化为 两个无环单链表是否相交,是否能找到第一个相交的节点，方法就是 快慢指针 。
3.若二者都有环,那么问题变成了两个有环单链表是否相交.
第一,先找到二者是否相交.
第二,若相交则需要遍历一遍找到相交点.
如果无环：问题转化为如何判断两个无环链表是否相交？
要想判断是否相交，肯定要看是否能找到相交的点，如果能让两个指针同时走到相交点，也就可以确定两个链表相交。
因为相交后两个链表到终点的距离相等，那么只要两个指针能够消除两个链表之间的长度差就可以到达终点的距离相等。
假设链表A比B长，pB到达结尾后指向headA，然后继续向前遍历，当pA到达结尾后指向headB，此时两者的长度差就消除了。
继续遍历如果两者指向同一节点，返回节点，如果两者都走到结尾依然没有相交，就返回null。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 返回环的入口
        if head is None or head.next is None:
            return None
        slow = head
        fast = head
        # 确定是否相交
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        # 如果链表走到了头，说明不想交
        if fast.next is None or fast.next.next is None:
            return None
        slow = head
        # 直到两个指针相遇，说明这个节点是相交节点
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow