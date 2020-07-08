'''
链接：https://www.nowcoder.com/questionTerminal/bf877f837467488692be703735db84e6?answerType=1&f=discussion

牛牛准备参加学校组织的春游, 出发前牛牛准备往背包里装入一些零食, 牛牛的背包容量为w。
牛牛家里一共有n袋零食, 第i袋零食体积为v[i]。
牛牛想知道在总体积不超过背包容量的情况下,他一共有多少种零食放法(总体积为0也算一种放法)。

输入描述:
输入包括两行
第一行为两个正整数n和w(1 <= n <= 30, 1 <= w <= 2 * 10^9),表示零食的数量和背包的容量。
第二行n个正整数v[i](0 <= v[i] <= 10^9),表示每袋零食的体积。


输出描述:
输出一个正整数, 表示牛牛一共有多少种零食放法。
示例1
输入
3 10
1 2 4
输出
8
说明
三种零食总体积小于10,于是每种零食有放入和不放入两种情况，一共有2*2*2 = 8种情况。
'''

# 递归
N, W = list(map(int, input().split()))
V = list(map(int, input().split()))


def count(W, V):
    if W <= 0:
        return 1
    if len(V) <= 0:
        return 1
    if sum(V) <= W:
        return 2 ** len(V)
    if V[0] <= W:
        return count(W - V[0], V[1:]) + count(W, V[1:])
    else:
        return count(W, V[1:])


print(count(W, V))

# 动态规划
import sys

n, w = list(map(int, sys.stdin.readline().strip().split()))

weights = list(map(int, sys.stdin.readline().strip().split()))

d = [1 for i in range(w + 1)]

for i in range(n):
    for j in range(w, weights[i] - 1, -1):
        d[j] += d[j - weights[i]]

print(d[-1])

# Java
'''
import java.util.*;
public class Main{
    public static void main(String[] args){
        int sum=0;
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int w = sc.nextInt();
        int[] v = new int[n];
        int i,j;
         
        for(i=0;i<n;i++)
            v[i] = sc.nextInt();
        int[][] dp = new int[n+1][];
        for(i=0;i<=n;i++)
            dp[i] = new int[w+1];
        for(i=0;i<=n;i++)
            dp[i][0] = 0;
        for(j=0;j<=w;j++)
            dp[0][j] = 1;
        for(i=1;i<=n;i++){
            for(j=1;j<=w;j++){
                if(j>=v[i-1])
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-v[i-1]];
                else
                    dp[i][j] = dp[i-1][j];
            }
        }
        System.out.println(dp[n][w]);
         
    }
}
'''
