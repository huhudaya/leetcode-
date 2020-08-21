'''

给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字）
并返回该子数组所对应的乘积。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
'''
from typing import List
import sys

'''
第 1 步：状态设计（特别重要）
dp[i][j]：以 nums[i] 结尾的连续子数组的最值，计算最大值还是最小值由 j 来表示，j 就两个值；
当 j = 0 的时候，表示计算的是最小值；
当 j = 1 的时候，表示计算的是最大值。
这样一来，状态转移方程就容易写出。

第 2 步：推导状态转移方程（特别重要）
由于状态的设计 nums[i] 必须被选取（请大家体会这一点，这一点恰恰好也是使得子数组、子序列问题更加简单的原因：当情况复杂、分类讨论比较多的时候，需要固定一些量，以简化计算）；

nums[i] 的正负和之前的状态值（正负）就产生了联系，由此关系写出状态转移方程：

当 nums[i] > 0 时，由于是乘积关系：
最大值乘以正数依然是最大值；
最小值乘以同一个正数依然是最小值；
当 nums[i] < 0 时，依然是由于乘积关系：
最大值乘以负数变成了最小值；
最小值乘以同一个负数变成最大值；
当 nums[i] = 0 的时候，由于 nums[i] 必须被选取，最大值和最小值都变成 00 ，合并到上面任意一种情况均成立。
但是，还要注意一点，之前状态值的正负也要考虑：例如，在考虑最大值的时候，当 nums[i] > 0 是，如果 dp[i - 1][1] < 0 （之前的状态最大值） ，此时 nums[i] 可以另起炉灶（这里依然是第 53 题的思想），此时 dp[i][1] = nums[i] ，合起来写就是：


dp[i][1] = max(nums[i], nums[i] * dp[i - 1][1]) if nums[i] >= 0
其它三种情况可以类似写出，状态转移方程如下：


dp[i][0] = min(nums[i], nums[i] * dp[i - 1][0]) if nums[i] >= 0
dp[i][1] = max(nums[i], nums[i] * dp[i - 1][1]) if nums[i] >= 0

dp[i][0] = min(nums[i], nums[i] * dp[i - 1][1]) if nums[i] < 0
dp[i][1] = max(nums[i], nums[i] * dp[i - 1][0]) if nums[i] < 0
第 3 步：考虑初始化
由于 nums[i] 必须被选取，那么 dp[i][0] = nums[0]，dp[i][1] = nums[0]。

第 4 步：考虑输出
题目问连续子数组的乘积最大值，这些值需要遍历 dp[i][1] 获得。
'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 动态规划
        n = len(nums)
        # dp[i]为以 i 结尾的位数的最大乘积
        dp = [[0] * 2 for _ in range(n)]
        res = -sys.maxsize
        # base case
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        for i in range(1, n):
            if nums[i] > 0:
                # 最大值
                dp[i][0] = max(dp[i - 1][0] * nums[i], nums[i])
                # 最小值
                dp[i][1] = min(dp[i - 1][1] * nums[i], nums[i])
            else:
                # 最大值
                dp[i][0] = max(dp[i - 1][1] * nums[i], nums[i])
                # 最小值
                dp[i][1] = min(dp[i - 1][0] * nums[i], nums[i])
        print(dp)
        for i in range(n):
            res = max(res, dp[i][0])
        return res


'''
思路三：根据符号的个数 [^2]
当负数个数为偶数时候，全部相乘一定最大
当负数个数为奇数时候，它的左右两边的负数个数一定为偶数，只需求两边最大值
当有 0 情况，重置就可以了
'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums_reverse = nums[::-1]
        reversed(nums)
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1  # or 1的作用是，当nums[i - 1]==0时，nums[i]乘等自身
            nums_reverse[i] *= nums_reverse[i - 1] or 1
        return max(max(nums), max(nums_reverse))


# 正向遍历和反向遍历
# 正序遍历和反序遍历
# 类似括号匹配这道题 LeetCode：32
'''
思路： 求最大值，可以看成求被0拆分的各个子数组的最大值。

当一个数组中没有0存在，则分为两种情况：

1.负数为偶数个，则整个数组的各个值相乘为最大值；

2.负数为奇数个
  从左边开始，乘到最后一个负数停止有一个“最大值”
  从右边也有一个“最大值”，比较，得出最大值。

class Solution {
    public int maxProduct(int[] nums) {
        int a=1;  
        int max=nums[0];
        
        for(int num:nums){
            a=a*num;
            if(max<a) max=a;
            if(num==0) a=1;

        }
        a=1;
        for(int i=nums.length-1;i>=0;i--){
            a=a*nums[i];
            if(max<a) max=a;
            if(nums[i]==0) a=1;
        }  
        return max;
    }
}
'''


# 动态规划
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 核心思路，记录之前的最大值和最小值
        # dp[i][j]：
        # 以 nums[i] 结尾的连续子数组的最值，计算最大值还是最小值由 j 来表示，j 就两个值 0 和 1
        if not nums:
            return 0
        n = len(nums)
        # dp[i][j]为以i结尾的最值
        dp = [[0] * 2 for _ in range(n)]
        # 注意base case
        dp[0][0] = dp[0][1] = nums[0]
        # 分类讨论，如果nums[i] > 0, 正数乘前面的最大值还是最大值，乘最小值还是最小值
        for i in range(1, n):
            # 如果是正数
            if nums[i] > 0:
                # 最大值
                dp[i][0] = max(nums[i], dp[i - 1][0] * nums[i])
                # 最小值
                dp[i][1] = min(nums[i], dp[i - 1][1] * nums[i])
            # 如果是负数
            else:
                # 最大值 负数的最大值为当前值乘最小值
                dp[i][0] = max(nums[i], dp[i - 1][1] * nums[i])
                # 最小值 负数的最小值为当前值乘最大值
                dp[i][1] = min(nums[i], dp[i - 1][0] * nums[i])
        res = -sys.maxsize
        for i in range(n):
            res = max(res, dp[i][0])
        return res
