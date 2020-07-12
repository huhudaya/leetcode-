'''
给定一个自然数N，要求把N拆分成若干个正整数相加的形式，参与加法运算的数可以重复。

注意:

拆分方案不考虑顺序；
至少拆分成2个数的和。
求拆分的方案数 mod 2147483648的结果。

输入格式

一个自然数N。

输出格式

输入一个整数，表示结果。

数据范围

1≤N≤4000

输入样例：

7
输出样例：

14
思路:将一个数差分成若干个数，很显然其中某些数可能会出现多次， 就是说这些数可以用无限多次来构成最初的数，这就是完全背包问题：有n个物品，每个物品可以选无限多次，求选出的若干个物品的价值之和恰好为n的方案个数。

状态表示：用f[i,j]表示选前i个物品且总价值之和恰好为j的方案，维护的属性：count。

状态计算：将f[i,j]按当前i(集合的最后一件物品)选和不选划分为两部分，前一部分：f[i-1,j];

后一部分：因为每件物品可能选多次，所以还要考虑次数,所这一部分方案数为：f[i,j-vi]+f[i,j-2vi]+...

因此，总的方案数为f[i,j]=f[i-1,j]+(f[i,j-vi]+f[i,j-2vi]+...)，但是这样就要再枚举每件物品选的次数，时间复杂度变成o

(n^3)，所以要再进一步优化：

通过对比观察f[i,j]和f[i,j-vi]代入上式的结果发现：f[i,j]=f[i-1,j]+f[i,j-vi]+f[i,j-2vi]+...

                                                                        f[i,j-vi]=f[i-1,j-vi]+f[i,j-2vi]+...

所以，通过等价代换可得：f[i,j]=f[i-1,j]+f[i,j-vi]

所以每次当前状态i与i这一状态有关，所以只要在循环体积时，从小到大枚举，就可以保证每次状态都是新的,恰好达到统计效果。

完整代码：

#include <iostream>

using namespace std;

const int maxn=4e3+5,mod=2147483648;

unsigned f[maxn];

int main()
{
    int n;
    cin>>n;
    f[0]=1;
    for(int i=1;i<=n;i++){//枚举物品（最初的自然数）
        for(int j=i;j<=n;j++){//枚举体积（分解的每个数）
            f[j]+=f[j-i];
        }
    }
    cout<<(f[n]-1)%mod<<endl;//因为至少要拆成两个数，所以1个的不算，要-1
    return 0;
'''

# 用高低两个数组优化
'''
题意：
给你一个数n,在给你一个数K,问你这个n用1-k的数去组合，有多少种组合方式。
思路：
背包重量就是n；
那么可以看出 1-k就是重物，价值是数值，重量是数值。
每个重物可以无限取，问题转化为完全背包。
我们用dp[]代表方案数的话，dp[0]=1;
由于当n=1000，k=1000的时候这个方案数是巨大的。
看了别的大牛博客，这个整数拆分真是好啊；

一个代表高位，一个代表低位；

#include<cstdio>
#include<iostream>
#include<string.h>
#include<algorithm>
using namespace std;

typedef long long LL;
const LL INF=1e18;
const int N=1e3+10;
LL d1[N],d2[N];

int main()
{
    int n,k;
    scanf("%d%d",&n,&k);
    memset(d1,0,sizeof(d1));
    memset(d2,0,sizeof(d2));

    d2[0]=1;
    for(int i=1;i<=k;i++)
    {
        for(int j=i;j<=n;j++)
        {
            d1[j]=d1[j]+d1[j-i]+(d2[j]+d2[j-i])/INF;//高位
            d2[j]=(d2[j]+d2[j-i])%INF;
        }
    }
    if(d1[n])
        printf("%lld",d1[n]);
    printf("%lld\n",d2[n]);
    return 0;
}
'''