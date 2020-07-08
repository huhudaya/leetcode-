'''
链接：https://www.nowcoder.com/questionTerminal/86ef0d5042934ef7819035794377a507?f=discussion
来源：牛客网

扔n个骰子，第i个骰子有可能投掷出Xi种等概率的不同的结果，数字从1到Xi。
所有骰子的结果的最大值将作为最终结果。求最终结果的期望。

输入描述:
第一行一个整数n，表示有n个骰子。（1 <= n <= 50）
第二行n个整数，表示每个骰子的结果数Xi。(2 <= Xi <= 50)
输出描述:
输出最终结果的期望，保留两位小数。

示例1
输入
2
2 2

输出
1.75
'''

# 看了半天题目才看懂，服了
# 所有骰子的结果的最大值将作为最终结果：当有两个骰子，点数都是2，
# 此时排列组合为（1，1），（1，2），（2，1），（2，2）
# 每种可能的点数都是最大值为1，2，2，2，，
# 总共有2*2中可能，那么就有1*1/4 + 2*1/4 + 2*1/4 * 2*1/4= 1.75
# 上面的2*1中的2表示的是最大点数是2，有1/4中可能
# 可以转换为求联合概率分布

'''
概率论的知识
P(x = k) = P(x <= k) - P(x < k) 
比如2，3
P(x = 2) = P(2,2) - P(1,1)

'''

def main(n, nums):
    total = 1
    # 找出骰子点数最大的那个
    maxs = max(nums)
    ans = 0
    pre = 0
    for i in range(1, maxs + 1):
        cur = 1
        for j in range(n):
            cur *= min(i, nums[j]) / nums[j]
        ans += (cur - pre) * i
        pre = cur
    return ans

# n = int(input())
n = 2
# nn = list(map(int, input().split()))
nn = [2,2]
ans = main(n, nn)
print("%.2f" % ans)