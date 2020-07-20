# 原文链接：https://blog.csdn.net/wumuzi520/article/details/7014830
'''
 完全背包是在N种物品中选取若干件（同一种物品可多次选取）放在空间为V的背包里，每种物品的体积为C1，C2，…，Cn，与之相对应的价值为W1,W2，…，Wn.求解怎么装物品可使背包里物品总价值最大。

动态规划（DP）：
        1） 子问题定义：F[i][j]表示前i种物品中选取若干件物品放入剩余空间为j的背包中所能得到的最大价值。
        2） 根据第i种物品放多少件进行决策
        其中F[i-1][j-K*C[i]]+K*W[i]表示前i-1种物品中选取若干件物品放入剩余空间为j-K*C[i]的背包中所能得到的最大价值加上k件第i种物品；
       设物品种数为N，背包容量为V，第i种物品体积为C[i]，第i种物品价值为W[i]。
       与01背包相同，完全背包也需要求出NV个状态F[i][j]。但是完全背包求F[i][j]时需要对k分别取0,…，j/C[i]求最大F[i][j]值,耗时为j/C[i]。
那么总的时间复杂度为O(NV∑(j/C[i]))

# 未优化
     F[0][] ← {0}
     F[][0] ← {0}
     for i←1 to N
         do for j←1 to V
             do for k←0 to j/C[i]
                if(j >= k*C[i])
                     then F[i][k] ← max(F[i][k],F[i-1][j-k*C[i]]+k*W[i])
     return F[N][V]

空间优化
     F[] = {0}
     for i←1 to N
         do for k←C[i] to V
             F[k] ← max(F[k],F[k-C[i]]+W[i])
     return F[V]
# '''
# 完全背包问题
#
# 描述：
#
# 有N件物品和一个容量为V的背包，每件物品都有无限个！。
#
# 第i件物品的体积是vi，价值是wi。
#
# 求解将哪些物品装入背包，可使这些物品的总体积不超过背包流量，且总价值最大。
#
#
# 一维动态规划
# 完全背包问题跟01背包问题最大的区别就是每一个物品可以选无数次
# 因此当我们考虑到第i个物品时，我们应该考虑的情况是：不选这个物品、选一次这个物品、选两次这个物品......，直到不能再选（选的次数k，k*v[i] > j，j为当前背包容量）
# 然后再从这些情况中选最大的。代码如下：

n, v = map(int, input().split())
goods = []
for i in range(n):
    goods.append([int(i) for i in input().split()])
dp = [0 for i in range(v + 1)]
for i in range(n):
    for j in range(v, -1, -1):  # 从后往前
        k = j // goods[i][0]  # 能选多少次
        # 从这些次里面取最大
        dp[j] = max([dp[j - x * goods[i][0]] + x * goods[i][1] for x in range(k + 1)])

print(dp[-1])
