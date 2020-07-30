from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 插入排序
        n = len(nums)
        for i in range(n):
            j = i - 1
            current = nums[i]
            while j >= 0 and current <= nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = current
        return nums