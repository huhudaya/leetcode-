'''
一开始有N根柱子，第i根柱子的高度是hi.
一开始小易站在第一根柱子上。小易能从第i根柱子跳到第j根柱子，当且仅当hj <= hi且1<= j-i <=k。其中k为指定的一个数字。
另外小易拥有一次释放超能力的机会。这个超能力能让小易从柱子i跳到任意满足1<= j-i <=k的柱子j而无视柱子高度的限制。
现在小易想知道，小易是否能到达第n根柱子
'''

# 核心思想其实就是找出状态和选择
# 本题的 状态 就是：
#   1.当前的柱子
#   2.当前允许使用的剩余超能力的次数（本题cnt=1）
#   3.是否可以到达当前的柱子（如果可以到达，就有了选择，即是否使用了超能力）
# 本题的 选择 就是：
#   使用或者不使用超能力
# 明确状态转义图：
# 1.如果可以到达，则有两种可能，一种是没有使用超能力，一种是使用了超能力
# 2.如果不可以到达，则有一种可能，以前使用过超能力，现在不可达
# 所以可以使用一个二维数组来表示状态
# 状态转移：
# 1.dp[i][k][0] = dp[i-1][k][0] || dp[i-1][k][1]
# 2.dp[i][k][1] = dp[i-1][k-1][0] || dp[i-1][k-1][1] #因为使用了超能力，所以需要将K-1,然后看之前的柱子是否满足条件
# dp[i][k][0]解释一下，第i个柱子，在k次跳跃的机会下，不使用超能力时是否可以到达
# 当k=1，这个时候dp[i][0][1] = False,因为k=0，所以不能使用超能力
# 当k=1，这个时候dp[i][0][0] = dp[i-1][0][0]
# dp[-1][0][0] = True
# dp[-1][0][1] = False
# dp[i][0][1] = False
# basecase:
# dp[-1][k][0] = True
# dp[-1][k][1] = True
# dp[i][0][1] = False
'''
参考股票受益的相关题目
注意，动态规划的题目都需要明确初始值！
一般这种题目的动态规划，限制的条件值需要减少，即当前操作依赖于前面的dp,比如当前是dp[i][k],满足条件的前一个是dp[i-1][k-1]
'''
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    li = list(map(int, input().split()))
    # flase表示不可达 1表示未使用超能力
    dp = [[False, 1] for _ in range(n)]
    dp[0][0] = True
    for i in range(1, n):
        # 相当于是在每一轮中，立一个标志位，表示是否使用了超能力，在结合之前是否使用超能力可以判断是否可达
        flag = False
        max1 = 0
        for j in range(max(0, i - k), i):
            if dp[j][0] == False:
                continue
            elif li[j] >= li[i]:
                dp[i] = dp[j].copy()
                max1 = max(max1, dp[j][1])
                dp[i][1] = max1
                flag = True
            elif li[j] < li[i] and not flag and dp[j][1]:
                dp[i] = dp[j].copy()
                dp[i][1] = 0
    if dp[-1][0]:
        print('YES')
    else:
        print('NO')

# class Solution:
#     def skip(self, nums, k):
#         size = nums
#         left = 0
#         right = 0
#         dp = [-1 for i in range(size)]
#         # 0:success 1:fail 2:super
#         dp[0] = 0
#         for i in range(size):
#             for j in range(i, i - k - 1, -1):
#                 if j < 0:
#                     continue
#                 elif nums[i] < nums[j] and (dp[j] == 2 or dp[j] == 0):
#                     dp[i] = 0
#                     continue
#                 else:


def skip(nums, k):
    used = [False for _ in range(k)]
    unused = used[:]
    unused[0] = True
    n = len(nums)
    for i in range(k):
        for j in range(i):
            if unused[j] and nums[j] >= nums[i]:
                unused[i] = True
                break
        used[i] = True
    for i in range(k, n):
        for j in range(i-k, i):
            if unused[j]:
                used[i] = True
                if nums[j] >= nums[i]:
                    unused[i] = True
                    break
            if used[j]:
                if nums[j] >= nums[i]:
                    used[i] = True
    if unused[n - 1] or used[n - 1]:
        return "YES"
    else:
        return  "NO"

num = [6,2,4,3,8]
print(skip(num,3))


'''
import java.util.*;
public class Main{
    public static void main(String []args){
        Scanner in = new Scanner(System.in);
        int op=in.nextInt();
        while(op-->0)
        { 
            int n = in.nextInt(),
            int k = in.nextInt();
            long []num = new long[n];
            for(int i = 0; i < n; i++)
            {
                num[i] = in.nextLong();
            }
            boolean [][]jump = new boolean[n][2];//记录每个柱子能否到达
            jump[0][0] = true;//表示没有使用超能力可以到达
            jump[0][1] = true;//表示使用超能力可以到达
            for(int i = 0; i < n; i++)
            {
                for(int j = 1; j <= k && j + i < n; j++)
                {
                    if(num[j + i] <= num[i])//可以通过普通跳跃到达
                    {//更新状态跟出发柱子相同
                        jump[j + i][0] |= jump[i][0];//没有使用超能力两者都要更新
                        jump[j + i][1] |= jump[i][1];//不需要使用超能力，所以需要看之前柱子是否使用超能力，如果使用了超能力，则本次不能使用超能力
                    }
                    else {
                        jump[j + i][1] |= jump[i][0];//使用了超能力只更新[j+i][1]，这个值只能从没使用超能力的状态到达
                        //该位置没使用超能力的情况仍是不能到达，其他状态不能从这个位置下再使用超能力（或者说不可达）
                    }
                }
                 
            }
            if(jump[n - 1][0] || jump[n - 1][1])
                    System.out.println("YES");
                else System.out.println("NO");
        }
    }
}
'''