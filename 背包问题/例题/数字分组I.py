'''
题目描述
给出一堆魔法石的重量，问如何分成两堆，使得它们质量和之差最小，求出这个最小值。
输入
第一行一个数n (n ≤30)。 接下来n行，每行一个正整数。(每个数≤100000)
'''
'''
将问题转化为求背包容量为所有数总和一半的背包问题
#include <iostream>
#include <cstring>
 
using namespace std;
int f[]={},sum,n;
int a[];
int main()
{
    cin>>n;
    sum=;
    memset(f,,sizeof(f));
    for(int i=;i<n;i++)
    {
        cin>>a[i];
        sum+=a[i];
    }
    for(int i=;i<n;i++)
    {
        for(int j=sum/;j>=a[i];j--)
        {
            f[j]=max(f[j],f[j-a[i]]+a[i]);
        }
    }
    cout<<sum-*f[sum/]<<endl;
    return ;
}
'''

'''
考虑最后分组情况，如果所有数的和为sum, 较小和的那组数一定不超过 [sum / 2]。
我们的目标是使得和较小组的总和尽可能大。

我们的目标是从这n个数中选出一些数，这些数的总和不超过[sum / 2]且总和尽可能大。

那我们重新定义int f(i,j)表示从前i个数中选出的数，总和不超过j的时候能得到的最大的和。

则如果不选择ai    f(i-1,j) = f(i,j)
如果选择ai,则f(i,j) = f(i, j - ai)    j >=  ai
'''
# 正整数分组
# 思路 P + N = sum(nums)=S，P > N
# P + N + P - N = S + P - N = S - 2P, P > N
# P - N = S - 2P
# 求P - N的最小值，相当于求 S - 2P的最小值，又因为P > N,所以S - 2P >= 0,所以P <= S/2, 等价于求P不大于S/2的最大值
n = int(input())
a = [0]
f = [0]
sum = 0
for i in range(n):
    x = int(input())
    a.append(x)
    f.append(0)
    sum += x
k = int(sum / 2)
for i in range(k):
    f.append(0)
# 相当于01背包的不恰好装满的最值问题
for i in range(1, n + 1):
    for j in range(k, a[i] - 1, -1):
        f[j] = max(f[j], f[j - a[i]] + a[i])
print(sum - 2 * f[k])