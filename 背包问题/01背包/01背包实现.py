'''
# 初始化都为0
# 如果是恰好装满，则除了00点，其他初始化为max.size
# 空间未优化
     F[0][] ← {0}
     F[][0] ← {0}
     for i←1 to N
         do for k←1 to V
             F[i][k] ← F[i-1][k]
             if(k >= C[i])
                 then F[i][k] ← max(F[i-1][k],F[i-1][k-C[i]]+W[i])
     return F[N][V]




# 空间优化
     F[] ← {0}
     for i ← 1 to N
         do for k ← V to C[i]
             F[k] ← max(F[k],F[k-C[i]]+W[i])
     return F[V]
# 路径信息
     F[] ← {0}
     Path[][]←0
     for i←1 to N
         do for k←V to C[i]
            if(F[k] < F[k-C[i]]+W[i])
                 then F[k] ← F[k-C[i]]+W[i]
                      Path[i][k] ← 1
     return F[V] and Path[][]
'''

# https://www.acwing.com/problem/content/description/2/

m, target = list(map(int, input().split()))
values = []
nums = []
for i in range(m):
    temp = list(map(int, input().split()))
    nums.append(temp[0])
    values.append(temp[1])


def get_max_value(nums, values, target):
    # 定义dp[i]为背包容量为i时可以装的最大价值
    dp = [0 for i in range(target + 1)]
    res = 0
    # nums在外面，因为是01背包，所以需要倒序
    for i in range(m):
        for j in range(target, nums[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - nums[i]] + values[i])
    return dp[target]


print(get_max_value(nums, values, target))
