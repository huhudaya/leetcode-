'''
节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。

示例1:

 输入：n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
 输出：true
示例2:

 输入：n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], start = 0, target = 4
 输出 true
提示：

节点数量n在[0, 1e5]范围内。
节点编号大于等于 0 小于 n。
图中可能存在自环和平行边。
通过次数5,385提交次数10,180
'''
from collections import deque
from typing import List

# BFS
class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        n = len(graph)
        adj = [[] for _ in range(n)]
        # 转为邻接表
        for i, j in graph:
            adj[i].append(j)
        # BFS
        queue = deque()
        queue.append(start)
        while queue:
            tmp = queue.popleft()
            if tmp == target:
                return True
            for i in adj[tmp]:
                queue.append(i)
        return False

# BFS
class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        n = len(graph)
        adj = [[] for i in range(n)]
        for i, j in graph:
            adj[i].append(j)
        # 用一个标记数组来标记是否已经遍历过，如果已经遍历过，需要continue
        seen = [False for _ in range(n)]
        # DFS
        def dfs(start):
            seen[start] = True
            if start == target:
                return True
            for i in adj[start]:
                if not seen[i] and dfs(i):
                    return True
            return False

        return dfs(start)
