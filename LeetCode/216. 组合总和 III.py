'''
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数
并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
'''
from typing import List
from itertools import combinations as com
class Solution:
    # 简约版本
    def combinationSum31(self, k: int, n: int) -> List[List[int]]:
        tmp = list(map(list,list(com(range(1, 10), k))))
        res = []
        for i in tmp:
            if sum(i) == n:
                res.append(i)
        return res
    # 优化版
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [i for i in range(1, 10)]
        size = 9
        res = []
        def dfs(target, path, start):
            if len(path) == k:
                if target == 0:
                    res.append(path[:])
                return
            # len(path)越大,size - (k - len(path)) + 2越大
            # 剪枝
            for i in range(start, size - (k - len(path)) + 2):
                # 下面这两行写不写无所谓
                # if target < i:
                #     break
                path.append(i)
                dfs(target - i, path, i + 1)
                path.pop()
        dfs(n, [], 1)
        return res
    # 未优化版
    def combinationSum32(self, k: int, n: int) -> List[List[int]]:
        candidates = [i for i in range(1, 10)]
        size = 9
        res = []
        def dfs(target, path, start):
            if len(path) == k and target == 0:
                res.append(path[:])
                return
            for i in range(start, size + 1):
                path.append(i)
                dfs(target - i, path, i + 1)
                path.pop()
        dfs(n, [], 1)
        return res