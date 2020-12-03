'''
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。

 

示例：

输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
 

提示：

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
'''

nums = [2, 3, 1, 1, 4, 0, 0, 4, 3, 3]
from typing import List
'''
如果原数组可以修改，则可以使用就地算法求解。

为数组的偶数下标部分和奇数下标部分分别维护指针 i, j
随后，在每一步中，如果 A[i] 为奇数，则不断地向前移动 j（每次移动两个单位)直到遇见下一个偶数
此时，可以直接将 A[i]A[i] 与 A[j]A[j] 交换
我们不断进行这样的过程，最终能够将所有的整数放在正确的位置上
'''
'''
func sortArrayByParityII(A []int) []int {
    nums := A
    n := len(A)
    for i, j := 0, 1; i < n; i += 2 {
        // 如果是奇数
        if nums[i] & 1 == 1 {
            for ; nums[j] & 1 == 1; j += 2 {
            }
            nums[i], nums[j] = nums[j], nums[i]
        }
    }
    return nums
}
'''

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        nums = A
        n = len(A)
        i = 0
        j = 1
        while i < n:
            # nums[i]是奇数
            if nums[i] & 1 == 1:
                while nums[j] & 1 == 1:
                    j += 2
                nums[i], nums[j] = nums[j], nums[i]
            i += 2
        return nums