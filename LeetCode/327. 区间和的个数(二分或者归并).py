# 327. 区间和的个数.py
'''
给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。

说明:
最直观的算法复杂度是 O(n2) ，请在此基础上优化你的算法。

示例:

输入: nums = [-2,5,-1], lower = -2, upper = 2,
输出: 3
解释: 3个区间分别是: [0,0], [2,2], [0,2]，它们表示的和分别为: -2, -1, 2。

链接：https://leetcode-cn.com/problems/count-of-range-sum
'''

'''
回到根本，这道题是让我们求解任意S[i] - S[j]满足：

lower <= S[i] - S[j] <= upper，j <= i

如果存在下面这个序列，左边蓝色部分是有序的，右边黄色部分是有序的，求有多少个答案满足：

注意 此时的S是指当前区域的和
lower <= S[i] - S[j] <= upper，j <= i (S[i]属于黄色右边区域，S[j]属于蓝色为左边区域)

'''
from typing import List
# 自己的版本
import bisect

'''
回到根本，这道题是让我们求解任意S[i] - S[j]S[i]−S[j]满足：

lower <= S[i] - S[j] <= upper，j <= i

如果存在下面这个序列，左边蓝色部分是有序的，右边黄色部分是有序的，求有多少个答案满足：

lower <= S[i] - S[j] <= upper，j <= i (S[i]属于黄色右边区域，S[j]属于蓝色为左边区域)

'''


class Solution:
    # def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
    #     # 前缀和数组初始化
    #     preSum = [0]
    #     # 构造前缀和数组
    #     for i in nums:
    #         preSum += [preSum[-1] + i]
    #     ans = 0
    #     queue = []
    #     # 逆序遍历前缀和数组
    #     for pi in preSum[::-1]:
    #         # 当前前缀和的两个边界
    #         i, j = pi + lower, pi + upper
    #         left = bisect.bisect_left(queue, i)
    #         right = bisect.bisect_right(queue, j)
    #         ans += right - left
    #         bisect.insort(queue, pi)
    #     return ans
    #  归并排序
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # 构造前缀和数组
        n = len(nums)
        preSum = [0 for _ in range(n + 1)]
        if nums is None or len(nums) == 0:
            return 0
        for i in range(n):
            preSum[i + 1] = preSum[i] + nums[i]
        # 前缀和数组中必须有一个前缀0作为辅助位置
        return self.merge(preSum, lower, upper)

    '''
    归并的思想，归并思路大家应该都懂，但是需要注意的是为什么将前缀和数组preSum中的第一个辅助位置初始值0的数不去掉？
    这是因为有单个值就满足条件的情况
    比如 [0,0] 0~0
    这个时候有3个满足条件的区间，前缀数组和是[0,0,0]
    这样单个值也会和初始值0进行比较
    '''

    def merge(self, nums: List[int], lower, upper):
        if len(nums) <= 1:
            return 0
        cnt = 0
        n = len(nums)
        mid = n // 2
        left = nums[:mid]
        right = nums[mid:]
        cnt += self.merge(left, lower, upper)
        cnt += self.merge(right, lower, upper)
        i = 0
        j = 0
        low = 0
        up = 0
        # 归并过程
        while i < mid:  # 这一层循环是为了遍历右边区域中的每一个元素，每一次i都加1
            # 高能，我这里原来吧len(right)写成了len(left)，上班时间单点调试了半天。。。一定要小心哦，fuck!
            while low < len(right) and right[low] - left[i] < lower:
                low += 1
            while up < len(right) and right[up] - left[i] <= upper:
                up += 1
            cnt += up - low
            i += 1
        # 归并排序过程
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            # 谁小移动谁
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        # 总有一个要出界
        while i < len(left):
            nums[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            nums[k] = right[j]
            k += 1
            j += 1
        return cnt


# 二分
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        p = [0]  # 前缀和初始化，前缀和p[x]，就是区间数组[0, x)的和
        for i in nums:
            p += [p[-1] + i]  # 前缀和计算
        # p = [0 for _ in range(len(nums) + 1)]
        # for i in range(1,len(nums)):
        #     p[i] += p[i-1] + nums[i]
        ans = 0
        q = []  # 有序的前缀和队列
        for pi in p[:: -1]:  # 逆序遍历前缀和
            i, j = pi + lower, pi + upper  # 给出当前前缀和两个对应边界
            l = bisect.bisect_left(q, i)  # 二分查找
            r = bisect.bisect_right(q, j)  # 找到对应边界的在前缀和数组里的插入位置
            ans += r - l  # 序号大于自己的前缀和里有多少个前缀和在边界里面，就是以当前区间为起点，符合区间和条件的个数
            bisect.insort(q, pi)  # 二分插入更新队列
        return ans

print(Solution().countRangeSum([-2,5,-1],-2,2))

import bisect
from itertools import accumulate


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix_sorted_sums = [0]

        ans = 0
        for sums in accumulate(nums):
            left = bisect.bisect_left(prefix_sorted_sums, sums - upper)
            right = bisect.bisect_right(prefix_sorted_sums, sums - lower)
            ans += right - left
            bisect.insort(prefix_sorted_sums, sums)
        return ans


# java
'''
前缀和数组为sum[];
满足条件的区间和为：
lower <= sum[i] - sum[j] <= upper;
将上述式子变形得到：
sum[i] - upper <= sum[j] <= sum[i] - lower;
也就是说在前缀和数组sum[0...i]中，满足上述条件的sum[j]都对应着一个满足条件的区间;

TreeMap底层实现为红黑树，是一种有序映射，查找时间复杂度为O(logN),并且可方便的进行区间查找
由于每次查找都是在sum[0...i]的范围内，所以可以边计算前缀和边插入TreeMap，同时统计满足条件的区间个数

class Solution {
    public int countRangeSum(int[] nums, int lower, int upper) {
        if(nums ==  null || nums.length == 0){
            return 0;
        }
        //键值为区间和和这个区间和出现的次数
        TreeMap<Long, Integer> tree = new TreeMap<>();
        tree.put(0L, 1);       
        int count = 0;
        long sum = 0L;
        for(int num : nums){
            sum += num;
            //subMap()返回一个值在sum - upper 和sum - lower 之间的子集合，values()方法获得这个映射的值得视图
            for(int cnt : tree.subMap(sum - upper, true, sum - lower, true).values()){
                count += cnt; //统计满足条件的区间和个数
            }
            tree.put(sum, tree.getOrDefault(sum, 0) + 1);
        }
        return count;
    }
}
'''


# 分治法
def cntSum(self, nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: int
    """
    sums = [0]
    for i in nums:
        sums.append(sums[-1] + i)

    def sort(lo, hi):
        if hi - lo <= 1:  # 如果数组只有一个数，那么下面的算法将不能比较出来，还会将数组长度退化成1，在下面的 sort 会栈溢出
            return 0

        mid = (lo + hi) // 2
        count = sort(lo, mid) + sort(mid, hi)
        i = j = mid  # 放在for 循环的外面，已经计算过的就不再重复，减少计算量
        for left in sums[lo:mid]:  # 对于 lo:mid 和 mid:hi 的所有情况已经在递归中全部计算过了，现在只有右边减去左边的可能没有出现过
            while i < hi and sums[i] - left < lower:
                i += 1
            while j < hi and sums[j] - left <= upper:
                j += 1
            count += j - i
        sums[lo:hi] = sorted(sums[lo:hi])  # 如果不排序，就会出现前面较大的数sums[h] (h >=mid)
        # 在索引低位的数 left计算失败后，left后移，而后面较小的数 sums[h+1] 计算不到 left 的情况的情况
        return count

    return sort(0, len(sums))
