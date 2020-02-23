# 442. 数组中重复的数据.py
'''
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。

找到所有出现两次的元素。

你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？

示例：

输入:
[4,3,2,7,8,2,3,1]

输出:
[2,3]

链接：https://leetcode-cn.com/problems/find-all-duplicates-in-an-array
'''


class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        returnlist = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                returnlist.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1
        return returnlist


# 如果是求任意一个重复出现的数字呢？
# 中心思想是将当前元素换到
def find(arr):
    if arr is None:
        return False
    for i in range(len(arr)):
        # 如果不在自己的位置，就去交换，直到arr[i]在自己的位置，因为题目要求一定会满足这个条件的
        while arr[i] != i:
            # 找到重复的数字
            if arr[arr[i]] == arr[i]:
                return arr[arr[i]]
            # 换到本来的位置
            else:
                arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
    return False
