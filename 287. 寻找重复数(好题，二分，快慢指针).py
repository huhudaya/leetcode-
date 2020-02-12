# 287. 寻找重复数.py
'''
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n
可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次

链接：https://leetcode-cn.com/problems/find-the-duplicate-number
'''
# 二分
class Solution:
    #O(nlogn)算法
    def findDuplicate(self, nums) -> int:
        start = 1
        end = len(nums) - 1
        #二分,相当于求解count(mid) > mid的FirstPosition
        while start + 1 < end:
            mid = start + (end-start) // 2
            # 这里计算的是小于mid的个数
            count = sum(num <= mid for num in nums)
            if count <= mid:
                start = mid
            else:
                end = mid
        #如果
        if sum(num <= start for num in nums) > start:
            return start
        else:
            return end
# 排序
class Solution:
    def firstDuplicate(self, nums):
        # 不满足题目的中的约束条件：数组是只读的
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]
# 时间复杂度 O(NlogN)

# 集合
class Solution:
    def firstDuplicate(self, nums):
        # 不满足题目要求:空间复杂度为O(N)
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

# 快慢指针
'''
题目设定的问题是N+1个元素都在[1,n]这个范围内。
这样我们可以用那个类似于 ‘缺失的第一个正数’ 这种解法来
但是题意限制了我们不能修改原数组，我们只能另寻他法。
也就是本编题解讲的方法，将这个题目给的特殊的数组当作一个链表来看

数组的下标就是指向元素的指针，把数组的元素也看作指针
如0是指针，指向nums[0]，而nums[0]也是指针，指向nums[nums[0]]

使用数组中的值作为索引下标进行遍历，遍历的结果肯定是一个环（有一个重复元素）
检测重复元素问题转换成检测环的入口
为了找到环的入口，可以进行如下步骤：

1. 设置两个快慢指针， fast每次走两步，slow每次走一步，最终走了slow走了n步与fast相遇，fast走了2*n，fast可能比slow多饶了环的i圈，得到环的周长为n/i
2. slow指针继续走, 且另设第三个指针每次走一步，两个指针必定在入口处相遇
    假设环的入口和起点的距离时m
    当第三个指针走了m步到环的入口时
    slow刚好走了n + m步，换句话说时饶了环i圈（环的周长为n/i）加m步（起点到入口的距离）
    得到相遇的是环的入口，入口元素即为重复元素

'''
# 相当于求环的入口 快慢指针  将索引数组看成链表
class Solution:
    def findDuplicate(self, nums) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        # 因为题意表示一定有环 注意题意是1-n,本题不能出现首位是0，不然会死循环
        while slow != fast:
            # print(slow, fast)
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
a = [1, 2, 3, 4, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0,15]
print(Solution().findDuplicate(a))