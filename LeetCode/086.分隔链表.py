'''

给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
'''

# 双指针法
'''
本题要求我们改变链表结构，使得值小于 x的元素，位于值大于等于x元素的前面
这实质上意味着在改变后的链表中有某个点，在该点之前的元素全部小于x ，该点之后的元素全部 大于等于x
我们将这个点记为JOINT
对该问题的逆向工程告诉我们，如果我们在JOINT将改后链表拆分，我们会得到两个更小的链表
其中一个包括全部值小于x的元素，另一个包括全部值大于x的元素
在解法中，我们的主要目的是创建这两个链表，并将它们连接

直觉
我们可以用两个指针before 和 after 来追踪上述的两个链表
两个指针可以用于分别创建两个链表，然后将这两个链表连接即可获得所需的链表

1.初始化两个指针 before 和 after
  在实现中，我们将两个指针初始化为哑 ListNode
  这有助于减少条件判断。（不信的话，你可以试着写一个不带哑结点的方法自己看看！）

2.利用head指针遍历原链表
3.若head 指针指向的元素值 小于 x，该节点应当是 before 链表的一部分。因此我们将其移到 before 中
4.否则，该节点应当是after 链表的一部分。因此我们将其移到 after 中
5.遍历完原有链表的全部元素之后，我们得到了两个链表 before 和 after。原有链表的元素或者在before 中或者在 after 中，这取决于它们的值
6.现在，可以将 before 和 after 连接，组成所求的链表

'''
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

# 官方
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        # before and after are the two pointers used to create two list
        # before_head and after_head are used to save the heads of the two lists.
        # All of these are initialized with the dummy nodes created.
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            # If the original list node is lesser than the given x,
            # assign it to the before list.
            if head.val < x:
                before.next = head
                before = before.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the after list.
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        # Last node of "after" list would also be ending node of the reformed list
        after.next = None
        # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        before.next = after_head.next

        return before_head.next

class Solution(object):
    def partition(self, head, x):
        # 准备两个哑结点
        before_dummy = ListNode(-1)
        after_dummy = ListNode(-1)
        # 定义两组节点
        before = before_dummy
        after = after_dummy
        # 遍历当前链表
        while head:
            # 如果当前值小于x,则放入前半部分节点中
            if head.val < x:
                before.next = head
                before = before.next
            # 否则加入到后半部分的节点中
            else:
                after.next = head
                after = after.next
            head = head.next
        # 将后半部分的尾部节点置None
        after.next = None
        # 将前半部分的尾部节点置为后半部分节点的头结点
        before.next = after_dummy.next
        return before_dummy.next
'''
复杂度分析

时间复杂度: O(N)，其中N是原链表的长度，我们对该链表进行了遍历。
空间复杂度: O(1)，我们没有申请任何新空间。值得注意的是，我们只移动了原有的结点，因此没有使用任何额外空间。
'''
