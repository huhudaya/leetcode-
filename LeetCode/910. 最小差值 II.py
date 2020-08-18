'''
给定一个整数数组 A，对于每个整数 A[i]，我们可以选择 x = -K 或是 x = K，并将 x 加到 A[i] 中。

在此过程之后，我们得到一些数组 B。

返回 B 的最大值和 B 的最小值之间可能存在的最小差值。

 

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
输出：3
解释：B = [4,6,3]
'''

'''
首先对数组排序，然后最重要的一个思想是，排序后的数组中
一定有一个位置 i，i 本身及左测全部加 K,i 右侧全部减 K
即A[0]..A[i]全部加上K，A[i+1]..A[n-1]全部减去 K
此时整个数组的最大值是 A[n-1]-K 或 A[i]+K，最小值是 A[0]+K 或 A[i+1]-K
有了这个前提后，就可以线性扫描 
i从0到 n-2(i 等于 n-1相当于全部加 K，也就是原始的最大值-最小值)，求出最小的可能值。
'''

from typing import List
import sys
class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        n = len(A)
        k = K
        res = A[n-1] - A[0]
        for i in range(n - 1):
            low = min(A[0] + K, A[i + 1] - K)
            high = max(A[n - 1] - K, A[i] + K)
            res = min(res, high - low)
        return res

# java
'''
class Solution {
    public int smallestRangeII(int[] A, int K) {
        int N = A.length;
        Arrays.sort(A);
        int ans = A[N-1] - A[0];

        for (int i = 0; i < A.length - 1; ++i) {
            int a = A[i], b = A[i+1];
            int high = Math.max(A[N-1] - K, a + K);
            int low = Math.min(A[0] + K, b - K);
            ans = Math.min(ans, high - low);
        }
        return ans;
    }
}
'''