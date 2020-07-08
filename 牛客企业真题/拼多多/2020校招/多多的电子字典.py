'''
多多鸡打算造一本自己的电子字典，里面的所有单词都只由a和b组成。
每个单词的组成里a的数量不能超过N个且b的数量不能超过M个。
多多鸡的幸运数字是K，它打算把所有满足条件的单词里的字典序第K小的单词找出来，作为字典的封面。
输入描述:
共一行，三个整数N, M, K。(0 < N, M < 50, 0 < K < 1,000,000,000,000,000)

输出描述:
共一行，为字典序第K小的单词。

输入例子1:
2 1 4
输出例子1:
ab


例子说明1:
满足条件的单词里，按照字典序从小到大排列的结果是
a
aa
aab
ab
aba
b
ba
baa
'''

# 回溯法 超时
import sys

# line = list(map(int, sys.stdin.readline().strip().split))
# m = line[0]
# n = line[1]
# k = line[2]
m, n, k = 2, 1, 4
candidates = []
used = [False for _ in range(m + n)]
for i in range(m + n):
    if i < m:
        candidates.append("a")
    else:
        candidates.append("b")


# 回溯遍历
def dfs(nums, used, path, res, depth, size):
    for i in range(len(nums)):
        if depth == size:
            return
        if not used[i]:
            if i > 0 and used[i - 1] == False and nums[i - 1] == nums[i]:
                continue
            used[i] = True
            path.append(nums[i])
            res.append(path[:])
            dfs(nums, used, path, res, depth + 1, size)
            path.pop()
            used[i] = False
    return res


# res = dfs(candidates, used, [], [], 0, m + n)
# print("".join(res[k-1]))


# 添加全局变量
import sys

line = list(map(int, sys.stdin.readline().strip().split()))
m = line[0]
n = line[1]
k = line[2]
candidates = []
used = [False for _ in range(m + n)]
cnt = 0
for i in range(m + n):
    if i < m:
        candidates.append("a")
    else:
        candidates.append("b")
ans = []


# 回溯遍历
def dfs(nums, used, path, res, depth, size):
    global cnt
    if cnt == k:
        return
    for i in range(len(nums)):
        if depth == size:
            return
        if not used[i]:
            if i > 0 and used[i - 1] == False and nums[i - 1] == nums[i]:
                continue
            used[i] = True
            cnt += 1
            path.append(nums[i])
            if cnt == k:
                ans.append(path[:])
                break
            dfs(nums, used, path, res, depth + 1, size)
            path.pop()
            used[i] = False


dfs(candidates, used, [], [], 0, m + n)
print("".join(ans[0]))


# 动态规划
def duoduoDict(m, n, k):
    # dp[i][j] 表示i个a,j个b所能构成的字母组合
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for i in range(m + 1):
        dp[0][i] = i
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            '''
            解释一下为什么其他回答的递归为dp[m][n] = dp[m][n - 1] + dp[m-1][n] + 2吧。
            假设m个a，n个b：
            那么第一个字母为a的个数为dp[m - 1][n] + 1 （额外加1是为了包括总长度为1的情况, 即'a'）
                (比如aab,dp[2][1]=dp[1][1] + dp[2][0] + 2,
                 这里的dp[1][1]表示以a开头，因为要以a开头，所以占用了一个位置，只有1个a可以用了
                 这个时候dp[1][1]=a,ab,b,ba；与a开头结合，这样就为aa,aab,ab,aba,这样还需要一个a!所以a开头的总共有dp[1][1]+1)
            那么第一个字母为b的个数为dp[m][n - 1] + 1 （额外的1是为了包括总长度为1的情况，即'b'）(我觉的应该是最后加一个b)
            所以，dp[m][n] = dp[m][n - 1] + dp[m-1][n] + 2。
            '''
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + 2
    return dp[m][n]


# print(duoduoDict(1, 1, 1))


# 递归法：计算m个A，n个B可以组合成多少种全排列(位数都相同)问题？
def Pai(m, n):
    if m == 0 or n == 0:
        return 1
    # 以A开头的+以B开头的组合
    return Pai(m - 1, n) + Pai(m, n - 1)


# 如果不是求全排列，求排列（位数可以不同）呢？

# print(Pai(2, 1))

# 自己的版本
class Solution:
    map = dict()

    def findKthNumber(self, n: int, m: int, k: int) -> int:
        # dp[i][j] 表示i个a,j个b所能构成的字母组合
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = i
        for i in range(m + 1):
            dp[0][i] = i
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # i个a和j个b组成的个数为以a开头的和以b开头的加上特殊的a和b
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + 2

        def cal_step(n, m):
            # 注意，这里为什么要+1呢？这是因为dp[n][m]表示的只是以某个字母开头的个数大于1的组合数量，需要加上原始的一个字符
            return dp[n][m] + 1

        cur = "a"
        # 第一次，应该是以'a'开头的
        n -= 1
        k -= 1
        while k > 0 and (n or m):
            step = cal_step(n, m)
            if step <= k:  # k在下一个子树中
                k -= step
                # 此时的n,m是为了计算dp[m][n]
                # 一轮过后，需要计算以b开头的，所以m-=1,n+=1
                n += 1
                m -= 1
                cur = cur[:-1] + "b"
            else:  # 在子树中
                k -= 1
                if n:
                    cur += "a"
                    n -= 1
                else:
                    cur += "b"
                    m -= 1
        return cur


print(Solution().findKthNumber(2,1,8))

def getcount(map, m, n):
    if not m:
        map[(m, n)] = n
    if not n:
        map[(m, n)] = m
    elif (m, n) in map:
        return map[(m, n)]
    else:
        # ＋'a'就是getcount(map,m-1,n)+1，加'b'同理
        map[(m, n)] = getcount(map, m - 1, n) + getcount(map, m, n - 1) + 2
    return map[(m, n)]


def mink(n, m, k):
    cur = ""
    map = {}
    while k > 0:
        if n > 0 and m == 0:  # 只有'a'存在
            k -= 1
            cur += "a"
            n -= 1
        elif m > 0 and n == 0:  # 只有'b'存在
            cur += 'b'
            k -= 1
            m -= 1
        elif n > 0 and m > 0:  # 都存在时
            # 计算a下所有子节点的和
            cnt = getcount(map, n - 1, m) + 1
            if cnt >= k:  # 在a子树下
                cur += 'a'
                k -= 1  # k相当于横向遍历，每次向右遍历一个节点
                n -= 1
            else:  # 在b子树下
                cur += 'b'
                m -= 1
                k -= (cnt + 1)  # k要减去a子树的所有节点个数
    return cur


# from collections import defaultdict
#
# ss = list(map(int, input().split()))
# n = ss[0]
# m = ss[1]
# k = ss[2]
# p = mink(n, m, k)
# print(p)
