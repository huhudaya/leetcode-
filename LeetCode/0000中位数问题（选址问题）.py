'''
直线上有N棵树木，需要在直线上修水塔，使水塔到所有树木的距离最短，时间复杂度为O(N)。
（水塔的安装位置在整数处，安装水塔的位置不能有树木）
输入：第一行 树的数目N。第二行N棵数目的坐标值
2<=N<=10^5,
树木的坐标0<=ai<=2^31
输入：
4
0 1 4 6
输出：
9
解释：在第三个位置上修水塔，距离为3+2+1+3=9
'''

# 好文https://blog.csdn.net/zhang20072844/article/details/13372753

# 一边遍历取距离最小
def one_steps():
    n = input()
    n = int(n)
    a = [int(i) for i in input().split()]
    pos = int((n) / 2)
    ans = 0
    a.sort()
    for i in range(0, n):
        ans += abs(a[i] - a[pos])
    print(ans)

# 双指针 中位数模板
def two_point():
    n = int(input())
    nums = list(map(int, input().strip().split()))
    left = 0
    right = n - 1
    sum = 0
    # 核心思想是左右两边的个数相同！这样差的和是最小的
    while left <= right:
        sum += nums[right] - nums[left]
        left += 1
        right -= 1
    print(sum)
two_point()