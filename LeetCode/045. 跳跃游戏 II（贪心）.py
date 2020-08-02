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
'''
在具体的实现中，我们维护当前能够到达的最大下标位置，记为边界。
我们从左到右遍历数组，到达边界时，更新边界并将跳跃次数增加 1。

在遍历数组时，我们不访问最后一个元素
这是因为在访问最后一个元素之前，我们的边界一定大于等于最后一个位置
否则就无法跳到最后一个位置了。如果访问最后一个元素，在边界正好为最后一个位置的情况下
我们会增加一次「不必要的跳跃次数」，因此我们不必访问最后一个元素。

'''
# 核心意思就是最后一步的步长一定会跨过倒数第二个元素
# 或者正好落在倒数第二个元素上，这个时候因为遇见边界，步数会+1，所以还是最优。
# 所以说只需要遍历到n-1即可
class Solution:
    def jump(self, nums) -> int:
        end = 0
        maxPosition = 0
        step = 0
        n = len(nums)
        # 注意，这里只需要遍历到n-1即可
        # 意思就是看到达n - 1之前跳跃了几次
        # # 核心意思就是最后一步的步长一定会跨过倒数第二个元素
        # 或者正好落在倒数第二个元素上，这个时候因为遇见边界，步数会+1，所以还是最优。
        # 所以说只需要遍历到n-1即可
        for i in range(n):
            # 找到能跳的最远的地方
            maxPosition = max(maxPosition, nums[i] + i)
            # 遇见边界就更新边界,遇见边界，就说明跳跃一次
            if i == end:
                end = maxPosition
                step += 1
            if end >= n - 1:
                return step
        return step



# 为什么到n-1就停止了，因为当i=0的时候，实际上step会是1，又因为题目说一定可以到达最后的位置，所以只需要遍历到n-1就可以了
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