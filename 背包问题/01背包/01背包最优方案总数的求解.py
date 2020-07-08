# 01背包最优方案总数的求解
# https://blog.csdn.net/mengt2012/article/details/43491859?utm_source=blogkpcl3
'''
回忆一下01背包的动态规划状态及状态方程：
 设背包容量为M，一共有N件物品，每件物品质量为weight[i]，每件物品的价值为value[i]。
1） 子问题定义：dp[i][j]表示前i件物品中选取若干件物品放入剩余容量为j的背包中所能得到的最大价值。
2） 根据第i件物品放或不放进行决策。

详细细节就不再多说了，我们直接进入正题。

在这里的话，最优方案总数就是物品总价值最大的方案数，那要怎么求呢？
我们设kry[i][j]为dp[i][j]的方案数，那么最优方案总数就是kry[N][M]，我们分析下怎么求kry[i][j]
对于01背包来说：
经过max函数取最大值后，如果dp[i][j]==dp[i-1][j] 或者 dp[i][j]==dp[i-1][j-weight[i]]+value[i] 
那么kry[i][j] = kry[i-1][j] 或者 kry[i][j] = kry[i-1][j-weight[i]]。
也就是说，对于dp[i][j]==dp[i-1][j] 时，表明第i件不放入时价值更大
那么到状态[i][j]的方案数就应该等于到状态[i-1][j]的方案数。
同理，如果dp[i][j]==dp[i-1][j-weight[i]]+value[i]
说明第i件放入时价值更大，此时到状态[i][j]的方案数就应该等于到状态[i-1][j-weight[i]]的方案数。
而若dp[i-1][j] ==dp[i-1][j-weight[i]]+value[i]，]
则说明即可以通过状态[i-1][j]在不加入第i件物品情况下到达状态[i][j]
又可以通过状态[i-1][j-C[i]]在加入第i件物品的情况下到达状态[i][j]
并且这两种情况都使得价值最大且这两种情况是互斥的
那么此时kry[i][j] = kry[i-1][j] + kry[i-1][j-weight[i]]
（你可以这样理解：两种到目前的状态[i][j]的方案都是最优解，那最优解的方案总数就是两个最优解的方案数相加）。
还有一点需要注意的，就是kry[][]必须全部初始化为1
因为无论dp[i][j]中i, j的值是多少，dp[i][j]总是存在的，既然存在，那就说明至少有一种方案，因此初始化为1。
这里可能有些难以理解，没事，先记着，慢慢就会懂了。
'''
'''
for(int j=0; j<maxm; j++ )
    kry[j] = 1;
memset(dp, 0, sizeof(dp));
for( int i=1; i<=n; i++ )
{
    for( int j=1; j<=m; j++ )
    {
    	dp[i][j] = dp[i-1][j];
    	kry[i][j] = kry[i-1][j];
    	if( j>=w[i] )
	{
	    if( dp[i][j]<dp[i-1][j-w[i]]+1 )
	    {
	    	dp[i][j] = dp[i-1][j-w[i]] + 1;
	        kry[i][j] = kry[i-1][j-w[i]];
	    }
	    	else if( dp[i][j]==dp[i-1][j-w[i]]+1 )
	             kry[i][j] = kry[i-1][j] + kry[i-1][j-w[i]];
	}
    }
}
'''
# https://blog.csdn.net/wumuzi520/article/details/7019131
'''
  最优方案总数这里指物品总价值最大的方案数。

         我们设G[i][j]代表F[i][j]的方案总数，那么最总结果应该是G[N][V]。我们初始化G[][]为1，因为对每个F[i][j]至少应该有一种方案，即前i件物品中选取若干件物品放入剩余空间为j的背包使其价值最大的方案数至少为1，因为F[i][j]一定存在。

         下面开始分析怎么求G[i][j]。对于01背包来说：

        如果F[i][j]=F[i-1][j]且F[i][j]!=F[i-1][j-C[i]]+W[i]说明在状态[i][j]时只有前i-1件物品的放入才会使价值最大，所以第i件物品不放入，那么到状态[i][j]的方案数应该等于[i-1][j]状态的方案数即G[i][j]=G[i-1][j]；

        如果F[i][j]=F[i-1][j-C[i]]+W[i] 且F[i][j]!=F[i-1][j]说明在状态[i][j]时只有第i件物品的加入才会使总价值最大，那么方案数应该等于[i-1][j-C[i]]的方案数，即G[i][j]=G[i-1][j-C[i]]；

        如果F[i][j]=F[i-1][j-C[i]]+W[i] 且F[i][j]=F[i-1][j]则说明即可以通过状态[i-1][j]在不加入第i件物品情况下到达状态[i][j]，又可以通过状态[i-1][j-C[i]]在加入第i件物品的情况下到达状态[i][j]，并且这两种情况都使得价值最大且这两种情况是互斥的，所以方案总数为G[i][j]=G[i-1][j-C[i]]+ G[i-1][j]。
# 未优化
  F[0][] ← 0
 
  F[][0] ← 0
 
  G[][ ] ← 1
 
  for i ← 1 to N
 
      do for j ← 1 to V
 
          F[i][j] ← F[i-1][j]
 
          G[i][j] ← G[i-1][j]
 
          if (j >= C[i])
 
              if (F[i][j] < F[i-1][j-C[i]]+W[i])
 
                  then F[i][j] ← F[i-1][j-C[i]]+W[i]
 
                      G[i][j] ← G[i-1][j-C[i]]
 
              else if (F[i][j] == F[i-1][j-C[i]]+W[i])
 
                  then G[i][j] ← G[i-1][j]+G[i-1][j-C[i]]
 
  return F[N][V] and G[N][V]

# 优化
  F[] ← 0
  G[] ← 1
  for i ← 1 to N
      do for j ← V to C[i]
          if (F[j] < F[j-C[i]]+W[i])
              then F[j] ← F[j-C[i]]+W[i]
                   G[j] ← G[j-C[i]]
          else if (F[j] = F[j-C[i]]+W[i]) 
              then G[j] ← G[j]+G[j-C[i]]
  return F[V] and G[V]
  
'''


