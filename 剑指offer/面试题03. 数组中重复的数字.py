'''
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，
但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个
重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
 

限制：

2 <= n <= 100000
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
'''
class Solution:
    def findRepeatNumber(self, arr) -> int:
        if arr is None or arr == []:
            return False
        n = len(arr)
        for i in range(n):
            while arr[i] != i:
                if arr[arr[i]] == arr[i]:
                    return arr[i]
                else:
                    arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
        return False


'''
将数组看做链表，其中元素的值看做next指针
由于存在相同的元素值，则必然存在两个节点同时指向了一个节点，即存在环。此时，本问题就转换为了求环形链表中环入口位置的问题。

Floyd 的判圈算法被划分成两个不同的阶段：

在第一阶段，用快慢指针找出列表中是否有环。如果没有环，可以直接返回 null 并退出
在第二阶段，用同速指针相遇来找到环的入口

'''


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # Floyd法
        if not nums: return None

        # 阶段0 寻找不指向自己的元素作为head
        head = 0
        while nums[nums[head]] == head:
            head += 1
        fast = slow = head

        # 阶段1 快慢指针
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        # 阶段2 同速指针
        fast = head
        while True:
            fast = nums[fast]
            slow = nums[slow]
            if fast == slow:
                break
        return fast
