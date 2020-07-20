'''
给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。
一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。
返回一对观光景点能取得的最高分。

示例：
输入：[8,1,5,2,6]
输出：11
解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11

提示：
2 <= A.length <= 50000
1 <= A[i] <= 1000
'''

'''
方法一：
思路：
设数组A长度为n，dp[j]表示以第j个元素结尾的数组的能拿到的最高分，那么dp[n-1]就是我们所需的答案。
对于第j个元素有两种选择：

不选为第二个观光结点，则最高分的两个观光结点在前j-1个元素中。dp[j] = dp[j-1]
选为第二个观光结点，则第一个观光结点在前j-1个元素中，遍历前j-1个元素，找到最高分数。dp[j] = max(A[i]+A[j]+i-j, ...), i从0到j-1
这种方法时间复杂度为O(n^2)，超时了。


class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& A) {
        int n = A.size();
        vector<int> dp(n, numeric_limits<int>::min());
        for(int j=1; j<n; ++j){
            dp[j] = dp[j-1];
            for(int i=0; i<j; ++i){
                dp[j] = max(dp[j], A[i]+A[j]+i-j);
            }
        }
        return dp.back();
    }
};
方法二：
思路：
方法一的主要问题是对于每一个d[j]，都要遍历前面所有的j-1个元素才能得到答案，方法二通过将得分划分为两个独立的部分，可以避免这个遍历。注意到得分可划分为两个独立部分： (A[i] + i) + (A[j] - j)，这两部分的得分不会相互影响。

dp1[i]表示以第i个元素结尾的数组，前面元素中A[i]+i的最大值是多少。
dp1[i] = max(dp1[i-1], A[i]+i);
dp2[j]表示以第i个元素结尾的数组，能取得的最高分。
dp2[j] = max(dp2[j-1], dp1[j-1]+A[j]-j);
其中dp2[j-1]表示不选当前元素为第二个观光景点，两个观光景点都在前j-1个元素中
dp1[j-1]+A[j]-j表示选当前元素为第二个观光景点，另一个观光景点在[0, j-1]时的最大得分

class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& A) {
        int n = A.size();
        vector<int> dp1(n, numeric_limits<int>::min());
        dp1[0] = A[0] + 0;
        for(int i=1; i<n; ++i){
            dp1[i] = max(dp1[i-1], A[i]+i);
        }
        vector<int> dp2(n, numeric_limits<int>::min());
        for(int j=1; j<n; ++j){
            dp2[j] = max(dp2[j-1], dp1[j-1]+A[j]-j);
        }
        return dp2.back();
    }
};
方法三：官方题解
方法二中求dp1的过程，可以只用一个变量去存储，这样就变成了官方题解。
注意：更新dp1的时机。是在dp2[j] = max(dp2[j-1], dp1+A[j]-j);前更新，还是在它之后更新。


class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& A) {
        int n = A.size();
        int dp1 = A[0] + 0;
        vector<int> dp2(n, numeric_limits<int>::min());
        for(int j=1; j<n; ++j){
            dp2[j] = max(dp2[j-1], dp1+A[j]-j);
            dp1 = max(dp1, A[j]+j);
        }
        return dp2.back();
    }
};
'''
# 自己的版本
from typing import List
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        # 空间优化
        # A[i] + A[j] + i - j 等价于(A[i] + i) + (A[j] -j)
        n = len(A)
        # dp[i]定义为到索引i为止的景点组合最高分
        dp = [0] * n
        left_max = A[0]
        # base case
        for i in range(1, n):
            # 做选择，不选择当前景点或者选择当前景点
            dp[i] = max(dp[i - 1], left_max + A[i] - i)
            # 更新left_max
            left_max = max(left_max, A[i] + i)
        return dp[n - 1]