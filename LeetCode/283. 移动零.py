'''

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
'''
from typing import List


# 两次遍历
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if not nums:
            return 0
        # 方法1：快慢指针，快指针不断往后遍历，找到不为0的数，一旦找到，就把该值赋予给慢指针所在的位置，然后慢指针往后走一格，这样就保证慢指针前面的全是非0，等快指针遍历完了，那么直接把慢指针之后的都赋为0即可。
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1

        for i in range(slow, len(nums)):
            nums[i] = 0



# 一次遍历，借助快排的思想
class Solution:
    class Solution:
        def moveZeroes(self, nums: List[int]) -> None:
            n = len(nums)
            slow = 0
            for i in range(n):
                if nums[i] != 0:
                    nums[slow], nums[i] = nums[i], nums[slow]
                    slow += 1
