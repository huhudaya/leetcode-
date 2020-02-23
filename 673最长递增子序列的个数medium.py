# 673最长递增子序列的个数medium.py
'''
描述
评论
题解New
历史
给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
'''

from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # 最长递增子序列的变种 so easy~
        n = len(nums)
        if n < 1:
            return 0
        # 初始化dp
        dp = [1 for i in range(n)]
        dc = [1 for i in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        dc[i] = dc[j]  # 组合数不变
                    elif dp[j] + 1 == dp[i]:
                        dc[i] += dc[j]  # 找到新的组合数
            # dp[i] = max(dp[i],dp[j]+1)  
        _max = max(dp)
        res = 0
        for p, z in zip(dp, dc):
            if p == _max:
                res += z
        return res


# scala版本
'''
import scala.util.control.Breaks._

object Solution {
  def findNumberOfLIS(nums: Array[Int]): Int = {
    var res = 0
    var mx = 0
    val len = new Array[Int](nums.length)
    val cnt = new Array[Int](nums.length)
    len.indices.foreach(i => len(i) = 1)
    cnt.indices.foreach(i => cnt(i) = 1)

    nums.indices.foreach(i => {
      (0 until i).foreach(j => {
        breakable {
          if (nums(i) <= nums(j)) break
          if (len(i) == len(j) + 1) cnt(i) += cnt(j)
          else if (len(i) < len(j) + 1) {
            len(i) = len(j) + 1
            cnt(i) = cnt(j)
          }
        }
      })
      mx = math.max(mx, len(i))
    })

    nums.indices.foreach(i => if (mx == len(i)) res += cnt(i))
    res
  }
    
}
'''
