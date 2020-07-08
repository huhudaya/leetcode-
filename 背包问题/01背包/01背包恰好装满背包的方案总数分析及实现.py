# 原文链接：https://blog.csdn.net/wumuzi520/article/details/7021210
'''
  网上各大公司经常出题目：假设现在有1元、2元、5元的纸币很多张，现在需要20块钱，你能给多少种找钱方案，这就可以认为是完全背包问题，即背包容量为20，物品体积分别为1、2、5。
        还有公司出题目：给定一个数m，将m拆成不同的自然数的和的形式有多少种方案，这就是典型的01背包问题，背包容量为m，物品件数为k，这里面的k是隐含条件，可以求出来，因为m最多由1+2+…+k得到，由此可以根据m求得物品件数的上限。
       现在切入正题，我们先谈“01背包”将背包刚好装满的方案总数。“完全背包”和“01背包”极为相似，只有极少量代码变动。

       01背包装满的问题抽象化：
       设背包容量为V，一共N件物品，每件物品体积为C[i]，每件物品的价值为W[i]，求将背包装满的方案总数。
       1） 子问题定义：F[i][j]表示前i件物品中选取若干件物品放入剩余空间为j的背包中刚好把背包装满的方案总数。
       2） 根据第i件物品体积和所剩背包容量大小进行决策

       注意初始化条件为F[0][0]=1，即没有物品放入容量为0的背包刚好放满的方案数为1。

# 这里只需要当空间压缩的时候，倒序遍历即可

# 未优化
	F[0][0] ← 1
  	for i ← 1 to N
      		do for j ← 0 to V
          	     if (j < C[i])
                         then F[i][j] ← F[i-1][j]
          	     else
             		 F[i][j] ← F[i-1][j]+F[i-1][j-C[i]]
  	return F[N][V]

# 优化
	F[0] ← 1
  	for i ← 1 to N
              # 注意，这里需要倒序! 01背包的特点就是当空间压缩的时候需要倒序
      		do for j ← V to C[i]
          	   if (j >= C[i])
              		then F[j] ← F[j]+F[j-C[i]]
  	return F[V]
'''