'''
给你一个整数数组 A，请你给数组中的每个元素 A[i]
都加上一个任意数字 x （-K <= x <= K），从而得到一个新数组 B

返回数组 B 的最大值和最小值之间可能存在的最小差值。

 

示例 1：

输入：A = [1], K = 0
输出：0
解释：B = [1]
示例 2：

输入：A = [0,10], K = 2
输出：6
解释：B = [2,8]
示例 3：

输入：A = [1,3,6], K = 3
输出：0
解释：B = [3,3,3] 或 B = [4,4,4]
 

提示：

1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000
'''

'''
假设 A 是原始数组，B 是修改后的数组，我们需要最小化 max(B) - min(B)
也就是分别最小化 max(B) 和最大化 min(B)
最小化max(B) 最小可能为 max(A) - K，因为 max(A) 不可能再变得更小
最大化min(B) 最大可能为 min(A) + K
所以结果 max(B) - min(B) 至少为 ans = (max(A) - K) - (min(A) + K)
'''


class Solution(object):
    def smallestRangeI(self, A, K):
        return max(0, max(A) - min(A) - 2 * K)


# Java
'''
class Solution {
    public int smallestRangeI(int[] A, int K) {
        int min = A[0], max = A[0];
        for (int x: A) {
            min = Math.min(min, x);
            max = Math.max(max, x);
        }
        return Math.max(0, max - min - 2*K);
    }
}
'''
