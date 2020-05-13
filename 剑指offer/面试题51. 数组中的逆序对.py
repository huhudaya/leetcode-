'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数。
示例 1:
输入: [7,5,6,4]
输出: 5

限制：
0 <= 数组长度 <= 50000
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 分治递归 归并的思想
from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeHelper(nums):
            if len(nums) <= 1:
                return 0
            left = 0
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]
            res1 = mergeHelper(left)
            res2 = mergeHelper(right)
            res = 0
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = right[j]
                    j += 1
                else:
                    res += (len(right) - j)
                    nums[k] = left[i]
                    i += 1
                k += 1
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1
            return res + res1 + res2
        ans = mergeHelper(nums)
        return ans
Solution().reversePairs([1,3,2,3,1])