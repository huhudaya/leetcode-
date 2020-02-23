# 674最长连续递增序列.py
'''
给定一个未经排序的整数数组，找到最长且连续的的递增序列。

示例 1:

输入: [1,3,5,4,7]
输出: 3
解释: 最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。 
示例 2:

输入: [2,2,2,2,2]
输出: 1
解释: 最长连续递增序列是 [2], 长度为1。
注意：数组长度不会超过10000。
'''


# 自己的版本
class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        left = 0
        right = 0
        res = 0
        n = len(nums)
        if nums == [] or nums is None:
            return 0
        while right < n - 1:
            if nums[right] >= nums[right + 1]:
                res = max(res, right - left + 1)
                left = right + 1
            right += 1
        return max(res, right - left + 1)

    # 简约版本
    def findLengthOfLCIS(self, nums) -> int:
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[i - 1] >= nums[i]:
                anchor = i
            ans = max(ans, i - anchor + 1)
        return ans


# Java版本 时间击败百分之百
# 计数法
# class Solution {
#     public int findLengthOfLCIS(int[] nums) {
#         int len = nums.length;
#         if (len < 2) {
#             return len;
#         }
#         int count = 1;
#         int t = 1;
#         for (int i = 0; i < len - 1; i++) {
#             if (nums[i] < nums[i + 1]) {
#                 t++;
#                 if (t > count) {
#                     count = t;
#                 }
#             } else {
#                 t = 1;
#             }
#         }
#         return count;
#     }
# }

a = list(set([1, 2, 4, 3, 2, 4]))
a.sort()
a.reverse()
print(a)
