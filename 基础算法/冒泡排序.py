class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 冒泡排序
        n = len(nums)
        for i in range(n - 1, -1, -1):
            for j in range(i):
                if nums[j] > nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
        return nums