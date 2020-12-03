'''

给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
示例 1：
输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]

示例 2：
输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]

提示：
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A 已按非递减顺序排序。
'''
from typing import List
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # 双指针
        n = len(A)
        left = 0
        right = n - 1
        res = [0 for i in range(n)]
        i = 0
        while left <= right:
            if abs(A[left]) >= abs(A[right]):
                res[i] = A[left] ** 2
                left += 1
            elif abs(A[left]) < abs(A[right]):
                res[i] = A[right] ** 2
                right -= 1
            i += 1
        return res[::-1]

# go
'''
func sortedSquares(a []int) []int {
    ans := make([]int, len(a))
    for i, v := range a {
        ans[i] = v * v
    }
    sort.Ints(ans)
    return ans
}
'''
# java
'''
class Solution {
    public int[] sortedSquares(int[] A) {
        int n = A.length;
        int[] ans = new int[n];
        for (int i = 0, j = n - 1, pos = n - 1; i <= j;) {
            if (A[i] * A[i] > A[j] * A[j]) {
                ans[pos] = A[i] * A[i];
                ++i;
            } else {
                ans[pos] = A[j] * A[j];
                --j;
            }
            --pos;
        }
        return ans;
    }
}
'''
# go
'''
func sortedSquares(a []int) []int {
    n := len(a)
    ans := make([]int, n)
    i, j := 0, n-1
    for pos := n - 1; pos >= 0; pos-- {
        if v, w := a[i]*a[i], a[j]*a[j]; v > w {
            ans[pos] = v
            i++
        } else {
            ans[pos] = w
            j--
        }
    }
    return ans
}
'''