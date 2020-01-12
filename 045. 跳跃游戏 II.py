# 045. 跳跃游戏 II.py
'''
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:
假设你总是可以到达数组的最后一个位置。
'''
'''
从数组的第 0 个位置开始跳，跳的距离小于等于数组上对应的数。
求出跳到最后个位置需要的最短步数。比如上图中的第 0 个位置是 2
那么可以跳 1 个距离，或者 2 个距离，我们选择跳 1 个距离，就跳到了第 1 个位置,也就是 3 上。
然后我们可以跳 1，2，3 个距离，我们选择跳 3 个距离，就直接到最后了。所以总共需要 2 步。
'''
'''
//遇见边界的时候步数才加一
public int jump(int[] nums) {
    int end = 0;
    int maxPosition = 0; 
    int steps = 0;
    for(int i = 0; i < nums.length - 1; i++){
        //找能跳的最远的
        maxPosition = Math.max(maxPosition, nums[i] + i); 
        if( i == end){ //遇到边界，就更新边界，并且步数加一
            end = maxPosition;
            steps++;
        }
    }
    return steps;
}

'''


class Solution:
    def jump(self, nums) -> int:
        if nums.count(1) == len(nums):
            return len(nums) - 1

        def fun(n):
            if not n: return 0
            for k, v in enumerate(n):
                if v >= len(n) - k:
                    return fun(n[:k]) + 1

        return fun(nums[:-1])


# 需要debug
# class Solution:
#     def jump(self, nums) -> int:
#         end = 0
#         step = 0
#         n = len(nums) - 1
#         bound = 0
#         if nums.count(1) == n:
#             return n - 1
#         # 贪心 局部最优,全局最优
#         for i, num in enumerate(nums[:-1]):
#             # end >= i表示在范围之内，然后看i+num是否超出范围
#             if end >= i and end < i + num:
#                 end = i + num
#                 # 遇见边界，更新边界
#                 if i == bound:
#                     step += 1
#                     bound = end
#                 # if end >= n:
#                 #     break
#         return step

class Solution:
    def jump(self, nums) -> int:
        end = 0
        maxPosition = 0
        step = 0
        n = len(nums)
        for i in range(n - 1):
            # 找到能跳的最远的地方
            maxPosition = max(maxPosition, nums[i] + i)
            # 遇见边界就更新边界
            if i == end:
                end = maxPosition
                step += 1
        return step


print(Solution().jump([2, 3, 1, 1, 4]))
