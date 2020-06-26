'''
链接：https://ac.nowcoder.com/acm/contest/320/H
来源：牛客网

对输入的字符串进行排序后输出
输入描述:
输入有两行，第一行n

第二行是n个空格隔开的字符串
输出描述:
输出一行排序后的字符串，空格隔开，无结尾空格
示例1
输入
5
c d a bb e

输出
a bb c d e
'''
# n = int(input())
# nums = list(map(str, input().strip().split()))
# sort_nums = sorted(nums)
# print(" ".join(sort_nums))



'''
链接：https://ac.nowcoder.com/acm/contest/320/I
来源：牛客网

示例1
输入
a c bb
f dddd
nowcoder

输出
a bb c
dddd f
nowcoder

'''
# import sys
# for line in sys.stdin:
#     nums = list(map(str, line.strip().split()))
#     nums.sort()
#     print(" ".join(nums))

import sys
from collections import defaultdict
m, n = [int(i) for i in input().strip().split()]
hashmap = dict()
res = defaultdict(int)
out = []
for i in range(m):
    nums = [str(j) for j in input().split()]
    hashmap[nums[0]] = set()
    hashmap[nums[0]].add(nums[1])
    if nums[2] != "*":
        hashmap[nums[0]].add(nums[2])
for i in hashmap.keys():
    res[i] += len(hashmap[i])
    for j in hashmap[i]:
        if j in hashmap:
            res[i] += len(hashmap[j])
for i in res.keys():
    if res[i] > n:
        out.append(i)
print(" ".join(out))