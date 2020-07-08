'''
科室素拓进行游戏，游戏规则如下：
随机抽取9个人作为游戏参与人员，分别编号1至9
每轮要求k(k<=9且k>=0)个人自由组合使编号之和为n
。输出满足规则的所有可能的组合
要求组合内部编号升序输出，组合之间无顺序要求
'''

n, target = list(map(int, input().split()))
candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []


def dfs(remain, stack):
    if remain == 0 and len(stack) == n:
        result.append(stack)
        return

    for item in candidates:
        if item > remain:
            break
        # 剪枝
        if stack and item <= stack[-1]:
            continue
        else:
            dfs(remain - item, stack + [item])


dfs(target, [])
if result:
    for i in result:
        for j in i:
            print(j, end=' ')
        print('')
else:
    print('None')

# 自己的版本
import sys

k, n = list(map(int, input().strip().split()))
candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
size = len(candidates)
res = []


def dfs(cacandidates, target, path, start):
    if target == 0 and len(path) == k:
        res.append(path[:])
        return
    for i in range(start, size):
        path.append(candidates[i])
        dfs(candidates, target - candidates[i], path, i + 1)
        path.pop()


dfs(candidates, n, [], 0)
if res:
    for i in res:
        for j in i:
            print(j, end=" ")
        print("")
else:
    print(None)
