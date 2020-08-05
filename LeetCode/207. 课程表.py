'''
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

示例 1:
输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。

示例 2:
输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。

提示：
输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
1 <= numCourses <= 10^5
'''
# 拓扑排序
# BFS
from typing import List
from collections import deque


class Solution:

    # 思想：该方法的每一步总是输出当前无前趋（即入度为零）的顶点

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        :type numCourses: int 课程门数
        :type prerequisites: List[List[int]] 课程与课程之间的关系
        :rtype: bool
        """
        # 课程的长度
        clen = len(prerequisites)
        if clen == 0:
            # 没有课程，当然可以完成课程的学习
            return True

        # 步骤1：统计每个顶点的入度
        # 入度数组，记录了指向它的结点的个数，一开始全部为 0
        in_degrees = [0 for _ in range(numCourses)]
        # 邻接表，使用散列表是为了去重
        adj = [set() for _ in range(numCourses)]
        # 想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
        # [0, 1] 表示 1 在先，0 在后
        # 注意：邻接表存放的是后继 successor 结点的集合
        for second, first in prerequisites:
            in_degrees[second] += 1
            adj[first].add(second)

        # 步骤2：拓扑排序开始之前，先把所有入度为 0 的结点加入到一个队列中
        # 首先遍历一遍，把所有入度为 0 的结点都加入队列
        queue = deque()
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)

        counter = 0
        while queue:
            top = queue.popleft()
            counter += 1
            # 步骤3：把这个结点的所有后继结点的入度减去 1，如果发现入度为 0 ，就马上添加到队列中
            for successor in adj[top]:
                in_degrees[successor] -= 1
                if in_degrees[successor] == 0:
                    queue.append(successor)

        return counter == numCourses


# DFS
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        # 记录
        visited = set()
        # 建图
        # 感觉这里用的很妙，学到了，这里泡菜哥跟我上面建的图不太一样，他找的是当前节点的上一个节点，而我上面是找的当前节点的下一个节点，所以我从原始节点开始删。
        for x, y in prerequisites:
            graph[y].append(x)

        # print(graph)
        # defaultdict(<class 'list'>, {1: [0], 2: [0], 3: [1, 2], 4: [2]})

        # 深度遍历
        def dfs(i, being_visited):
            if i in being_visited: return False
            # 说明该节点被第二次遍历到，有环
            if i in visited: return True
            # 在一次递归当中，being_visited和visited是同时增加的，当递归结束时，being_visited元素会被移除，而visited的则会被保留
            visited.add(i)
            being_visited.add(i)
            for j in graph[i]:
                # 如果键值不存在，返回[],其中没有数据
                # print(j,graph[0])
                if not dfs(j, being_visited): return False
                # 递归看倒序遍历并用being_visited记录到过节点的会不会被重新遍历，
                # 如果重新遍历到的话，说明有环
            being_visited.remove(i)
            # 因为检查的是每一个节点往下走会不会有环，所以在检查下一个节点时需要重置being_visited
            return True

        # 检测每门功课起始是否存在环
        for i in range(numCourses):
            # 已经访问过
            if i in visited: continue
            if not dfs(i, set()): return False
        return True
