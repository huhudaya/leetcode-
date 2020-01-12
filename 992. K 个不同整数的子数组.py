# 992. K 个不同整数的子数组.py
'''
给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定独立的子数组为好子数组。

（例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。）

返回 A 中好子数组的数目。

 

示例 1：

输出：A = [1,2,1,2,3], K = 2
输入：7
解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
示例 2：

输入：A = [1,2,1,3,4], K = 3
输出：3
解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].
 

提示：

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length

链接：https://leetcode-cn.com/problems/subarrays-with-k-different-integers
'''
'''
public int subarraysWithKDistinct(int[] A, int K) {
    if (A == null || A.length < K) {
        return 0;
    }

    int[] hash = new int[A.length + 1];

    int l = 0, results = 0, count = 0, result = 1;
    for (int r = 0; r < A.length; ++r) {
        hash[A[r]]++;

        if (hash[A[r]] == 1) {
            count++;
        }

        while (hash[A[l]] > 1 || count > K) {
            if (count > K) {
                result = 1;
                count--;
            } else {
                result++;
            }
            hash[A[l]]--;
            l++;
        }

        if (count == K) {
            results += result;
        }
    }

    return results;
}
'''
from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        # 滑动窗口
        # base case 
        if A is None or len(A) < K:
            return 0
        hash = defaultdict(int)
        n = len(A)
        left = 0
        res = 0
        cnt = 0
        tmp = 1
        for i in range(n):
            hash[A[i]] += 1
            if hash[A[i]] == 1:
                cnt += 1
            # 移动左指针的条件，直到满足条件，这里需要注意的是左指针移动一次，算新来一个数!这个时候才tmp++,否则 tmp=1
            while hash[A[left]] > 1 or cnt > K:
                if cnt > K:
                    tmp = 1
                    cnt -= 1
                else:
                    tmp += 1
                hash[A[left]] -= 1
                left += 1
            if cnt == K:
                res += tmp
        return res





print(Solution().subarraysWithKDistinct([2,2,1,2,2,2,1,1],2))




