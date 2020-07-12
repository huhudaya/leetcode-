'''
题目描述
已知一堆魔法石的重量，问如何分成两堆，使得它们质量和之差最大，但不能大于（可以等于）这些数中的最大数。
输入
       第一行一个数n(n ≤20)。
       接下来n行，每行一个正整数(每个数≤100000)。
输出
一个整数表示两组数字和的最大差。
样例输入 Copy
5
2 4 5 8 10
样例输出 Copy
9
解析
问题说把魔法石分成两堆，使其质量之差最大，但不能大于可以等于这些数的最大值。
假设他们的差值 最大为这些数的最大值(max1),他们的和为sum,所以可以其中一堆的值为（max1+sum)/2;
该问题就转 化成了把问题转化为从n个物品中取若干个，使其重量不超过（max1+sum)/2，且重量达到最大
x-y=max1
x+y=sum
'''
'''
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<map> 
#include<bits/stdc++.h> 
using namespace std;
typedef long long ll; 
inline int read()
{
    int x=0,f=1;char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    return x*f;
}
const int maxn=1e5;
int a[maxn],dp[maxn];
int n;
int sum;
int max1=0; 
int main(){
    cin>>n;
    for(int i=1;i<=n;i++){
        cin>>a[i];
        sum+=a[i];
        max1=max(max1,a[i]);
    }
    int t=(max1+sum)/2;
    for(int i=1;i<=n;i++){
        for(int j=t;j>=a[i];j--){
            dp[j]=max(dp[j],dp[j-a[i]]+a[i]);
        }
    }
    printf("%d\n",abs(sum-dp[t]-dp[t]));
}
'''