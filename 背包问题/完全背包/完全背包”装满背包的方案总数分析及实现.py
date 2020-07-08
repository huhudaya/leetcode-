'''
F[i-1][j]表示背包中不含第i种物品时把背包装满的方案
F[i][j-C[i]]表示至少包含一件第i种物品把背包装满的方案总数。
所以，当j<C[i]时F[i][j] = F[i-1][j]；当j >= C[i]时， F[i][j] = F[i][j-C[i]] + F[i-1][j]
为什么是两者的和，因为F[i][j-C[i]]和F[i-1][j]都是[i][j]状态时把背包装满的方案，且两者互斥。

# 未优化
	F[0][0] ← 1
  	for i ← 1 to N
              # 注意这里是从0开始遍历，这样就相当于我们不用初始化dp的base case了
      	    do for j ← 0 to V
          	if (j < C[i])
                         then F[i][j] ← F[i-1][j]
          	else
              	      F[i][j] ← F[i-1][j]+F[i][j-C[i]]
  	return F[N][V]

# 优化
	F[0] ← 1
	for i ← 1 to N
      	    do for j ← C[i] to V
          	if (j >= C[i])
              	    then F[j] ← F[j]+F[j-C[i]]
  	return F[V]
'''