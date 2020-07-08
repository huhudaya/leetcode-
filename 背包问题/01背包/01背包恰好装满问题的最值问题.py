# https://blog.csdn.net/Ratina/article/details/87859525?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase
'''
总结：
①求最大值：
fill(dp,dp+maxn,-INF), dp[0]=0;
若 dp[j] < 0，说明容量为 j 的背包无法被装满；


②求最小值：
fill(dp,dp+maxn,INF), dp[0]=0;
若 dp[j] == INF，说明容量为 j 的背包无法被装满；

还有一种问题：要求背包恰好装满的情况。
1.
    在对二维数组初始化时：
1）v[0][0]初始化为0
2）第一行和第一列的其他值都设为-INF(未装满的状态)
原因：
1）占用空间为0的物品刚好可以装满空间为0的背包
2）只有上一层恰好装满时，使用状态方程得到的下一层才能是正好装满，因此初始值设为-INF，即上一层未装满时，下一层加入a[i]结果仍然是-INF即未装满。
2.
    同样的，初始化一维数组时，将v[0]设为0，其他设为-INF

我们看到的求最优解的背包问题题目中，事实上有两种不太相同的问法。
有的题 目要求“恰好装满背包”时的最优解，有的题目则并没有要求必须把背包装满。
一种区别这两种问法的实现方法是在初始化的时候有所不同。
如果是第一种问法，要求恰好装满背包，那么在初始化时除了 f[0]为 0 其它 f[1..W]均设为-∞
这样就可以保证最终得到的 f[N]是一种恰好装满背包的最 优解。
如果并没有要求必须把背包装满，而是只希望价格尽量大，初始化时应该将 f[0..W]全部设为 0。
为什么呢?可以这样理解:
初始化的 f 数组事实上就是在没有任何物品可以放入 背包时的合法状态。
如果要求背包恰好装满，那么此时只有容量为 0 的背包可能 被价值为 0 的 nothing“恰好装满”
其它容量的背包均没有合法的解，属于未 定义的状态，它们的值就都应该是-∞了。
如果背包并非必须被装满，那么任何 容量的背包都有一个合法解“什么都不装”，这个解的价值为 0
所以初始时状 态的值也就全部为 0 了
这个小技巧完全可以推广到其它类型的背包问题，后面也就不再对进行状态转移 之前的初始化进行讲解。
链接：https://www.jianshu.com/p/25f4a183ede5
'''

'''
//01背包--不要求正好装满
#include <iostream>
using namespace std;
#define max(N1,N2) N1>N2?N1:N2
int main()
{
	int N, V;
	while (cin >> V >> N)//这里要求V<1000，N<100,否则后面的数组装不下
	{
		int v[100], w[100];//体积和价值
		int f[1000] = { 0 };//状态转移矩阵，这里将f数组全部初始化为0
		for (int i = 1; i <= N; i++)
		{
			cin >> v[i] >> w[i];//输入原始数据
		}
		for (int i = 1; i <= n; i++)
		{
			for (int j = V; j >= v[i]; j--)
			{
				f[j] = max(f[j], f[j - v[i]] + w[i]);
			}
		}
		cout << f[V] << endl;//输出结果
	}
	return 0;
}

'''