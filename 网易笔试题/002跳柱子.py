'''
一开始有N根柱子，第i根柱子的高度是hi.
一开始小易站在第一根柱子上。小易能从第i根柱子跳到第j根柱子，当且仅当hj <= hi且1<= j-i <=k。其中k为指定的一个数字。
另外小易拥有一次释放超能力的机会。这个超能力能让小易从柱子i跳到任意满足1<= j-i <=k的柱子j而无视柱子高度的限制。
现在小易想知道，小易是否能到达第n根柱子
'''


class Solution:
    def skip(self, nums, k):
        size = nums
        left = 0
        right = 0
        dp = [-1 for i in range(size)]
        # 0:success 1:fail 2:super
        dp[0] = 0
        for i in range(size):
            for j in range(i, i - k - 1, -1):
                if j < 0:
                    continue
                elif nums[i] < nums[j] and (dp[j] == 2 or dp[j] == 0):
                    dp[i] = 0
                    continue
                else:




def skip(nums, k):
    used = [False for i in range(k)]
    unused = used[:]
    unused[0] = True
    n = len(nums)
    for i in range(k):
        for j in range(i):
            if unused[j] and nums[j] >= nums[i]:
                unused[i] = True
                break
        used[i] = True
    for i in range(k, n):
        for j in range(i-k, i):
            if unused[j]:
                used[i] = True
                if nums[j] >= nums[i]:
                    unused[i] = True
                    break
            if used[j]:
                if nums[j] >= nums[i]:
                    used[i] = True
    if unused[n - 1] or used[n - 1]:
        return "YES"
    else:
        return  "NO"

num = [6,2,4,3,8]
print(skip(num,3))