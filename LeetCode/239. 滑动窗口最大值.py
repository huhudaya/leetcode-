# 239. 滑动窗口最大值.py
'''
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

 

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：

你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

 

进阶：

你能在线性时间复杂度内解决此题吗？

链接：https://leetcode-cn.com/problems/sliding-window-maximum
'''

from collections import deque
class Solution:
    #暴力解法O(N*M)
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     if k <= 0 or len(nums) < k or nums is None or nums == []:
    #         return []
    #     tmp = []
    #     最多只需要匹配n-m+1次
    #     for i in range(len(nums) - k + 1):
    #         tmp.append(max(nums[i:i+k]))
    #     return tmp
    # 单调队列的方法
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     #双端队列的方法
    #     if k <= 0 or len(nums) < k or nums is None or nums == []:
    #          return []
    #     qmax = deque()
    #     res = []
    #     length = len(nums)
    #     for i in range(length):
    #         #维护一个qmax从大到小双端队列，注意双端队列中维护的是数组下标
    #         while qmax and nums[qmax[-1]] < nums[i]:
    #             qmax.pop()
    #         #注意需要添加的是对应的下标
    #         qmax.append(i)
    #         #判断队列头是否过期
    #         if qmax[0] == i - k:
    #             qmax.popleft()
    #         # i 大于窗口则打印
    #         if i >= k - 1:
    #             #打印队列中的队首元素
    #             res.append(nums[qmax[0]])
    #     return res
    '''
    思路：
    	维护窗口，向右移动时左侧超出窗口的值弹出，
    	因为需要的是窗口内的最大值，所以只要保证窗口内的值是递减的即可
    	小于新加入的值全部弹出。
    	最左端即为窗口最大值 python解法：
    '''
    def maxSlidingWindow(self, nums, k):
        win, ret = [], []
        for i, v in enumerate(nums):
            if i >= k and win[0] <= i - k: win.pop(0)
            while win and nums[win[-1]] <= v: win.pop()
            win.append(i)
            if i >= k - 1: ret.append(nums[win[0]])
        return ret




