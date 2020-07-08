# 237. 删除链表中的节点.py
'''
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

现有一个链表 -- head = [4,5,1,9]，它可以表示为:
示例 1:

输入: head = [4,5,1,9], node = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:

输入: head = [4,5,1,9], node = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
 

说明:

链表至少包含两个节点。
链表中所有节点的值都是唯一的。
给定的节点为非末尾节点并且一定是链表中的一个有效节点。
不要从你的函数中返回任何结果。

链接：https://leetcode-cn.com/problems/delete-node-in-a-linked-list
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
由于只给出要删除的节点 node
按照常规思路，需要找到删除节点的上一个节点 pre
但是显然这道题目我们是获取不到的
所以，我们需要转变思路
由于本题并没有限制我们修改链表，所以可以采用复制法解决这个问题
把需要删除节点的下一个节点的值赋值给要删除的节点，之后删除节点的下一个节点即可。
明确了思路之后，代码实现非常简单
'''
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 看清楚题目啊！要求删除节点node
        if node.next:
            node.val = node.next.val
            node.next = node.next.next