# 560. 和为K的子数组.py
'''
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
'''


# hash优化版本
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和思想
        n = len(nums)
        preSum = dict()
        # base case
        preSum[0] = 1
        sum_i = 0
        res = 0
        for i in range(n):
            sum_i += nums[i]
            sum_j = sum_i - k
            if sum_j in preSum:
                res += preSum.get(sum_j)
            preSum[sum_i] = preSum.get(sum_i, 0) + 1
        return res


# 前缀和
# 太牛逼的思路了！
'''
	给定一个整数数组和一个整数k，你需要找到该数组中的和为K的连续子数组的个数
	示例:
		输入:nums = [1,1,1] K=2
		输出:2,[1,1]和[1,1]视为两种情况
	说明:
		数组的长度为[1,20,000]
		数组中元素的范围是[-1000,1000],整数的范围是[-1e7,1e7]
		思路很简单，我把所有子数组都穷举出来，算它们的和，看看谁的和等于 k 不就行了。

关键是，如何快速得到某个子数组的和呢，比如说给你一个数组nums
让你实现一个接口sum(i, j)，这个接口要返回nums[i..j]的和，而且会被多次调用，你怎么实现这个接口呢？

因为接口要被多次调用，显然不能每次都去遍历nums[i..j]
有没有一种快速的方法在 O(1) 时间内算出nums[i..j]呢？这就需要前缀和技巧了。
'''
# 前缀和的思路是这样的，对于一个给定的数组nums，我们额外开辟一个前缀和数组进行预处理：
'''
	int n = nums.length;
// 前缀和数组
int[] preSum = new int[n + 1];
preSum[0] = 0;
for (int i = 0; i < n; i++)
    preSum[i + 1] = preSum[i] + nums[i];
这个前缀和数组preSum的含义也很好理解，preSum[i]就是nums[0..i-1]的和。
那么如果我们想求nums[i..j]的和，只需要一步操作preSum[j+1]-preSum[i]即可，而不需要重新去遍历数组了。

回到这个子数组问题，我们想求有多少个子数组的和为 k，借助前缀和技巧很容易

'''


# 我这里的preSum中就不借助第一个元素为基准元素了
# 需要多准备一格
# 因为这里需要连续的子数组序列，所以不能像其他常规的构造前缀和一样的方法
# hash优化版本
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和思想
        n = len(nums)
        preSum = dict()
        # base case
        preSum[0] = 1
        sum_i = 0
        res = 0
        for i in range(n):
            sum_i += nums[i]
            sum_j = sum_i - k
            if sum_j in preSum:
                res += preSum.get(sum_j)
            preSum[sum_i] = preSum.get(sum_i, 0) + 1
        return res


# 这个解法的时间复杂度O(N2)空间复杂度O(N)，并不是最优的解法。
# 不过通过这个解法理解了前缀和数组的工作原理之后，可以使用一些巧妙的办法把时间复杂度进一步降低

'''
第二层 for 循环在干嘛呢？翻译一下就是，在计算，有几个j能够使得sum[i]和sum[j]的差为 k。
毎找到一个这样的j，就把结果加一。

我们可以把 if 语句里的条件判断移项，这样写：

if (sum[j] == sum[i] - k)
    ans++;
优化的思路是：我直接记录下有几个sum[j]和sum[i]-k相等，直接更新结果，就避免了内层的 for 循环。
我们可以用哈希表，在记录前缀和的同时记录该前缀和出现的次数。
'''


# 优化版本。利用hash
def subarraySum2(nums, k):
    length = len(nums)
    preSum = dict()
    ans = 0
    sum_i = 0
    for i in range(length):
        # 构造前缀和数组
        sum_i += nums[i]
        # 判断条件变形一下
        sum_j = sum_i - k
        if sum_j in preSum:
            # 有几个sum_j
            ans += preSum.get(sum_j)
        # preSum.setdefault(sum_i,preSum.get(sum_i,0)+1)
        # 先取出来，在进行hash的set操作
        preSum[sum_i] = preSum.get(sum_i, 0) + 1
    return ans


a = dict()
print(a.get(1))

'''
前缀和不难，却很有用，主要用于处理数组区间的问题。

比如说，让你统计班上同学考试成绩在不同分数段的百分比，也可以利用前缀和技巧：

'''

# 下面这个是常规的构造前缀和的算法
'''
int[] scores; // 存储着所有同学的分数
// 试卷满分 150 分
int[] count = new int[150 + 1]
// 记录每个分数有几个同学
for (int score : scores)
    count[score]++
// 构造前缀和
for (int i = 1; i < count.length; i++)
    count[i] = count[i] + count[i-1];
'''
'''
这样，给你任何一个分数段，你都能通过前缀和相减快速计算出这个分数段的人数，百分比也就很容易计算了。

但是，稍微复杂一些的算法问题，不止考察简单的前缀和技巧。比如本文探讨的这道题目，就需要借助前缀和的思路做进一步的优化，借助哈希表记录额外的信息。可见对题目的理解和细节的分析能力对于算法的优化是至关重要的。
'''
