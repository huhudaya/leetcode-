'''
给出方程式 A / B = k, 其中 A 和 B 均为用字符串表示的变量， k 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。如果结果不存在，则返回 -1.0。

输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

 

示例 1：

输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
解释：
给定：a / b = 2.0, b / c = 3.0
问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
返回：[6.0, 0.5, -1.0, 1.0, -1.0 ]
示例 2：

输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
输出：[3.75000,0.40000,5.00000,0.20000]
示例 3：

输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
输出：[0.50000,2.00000,-1.00000,-1.00000]
 

提示：

1 <= equations.length <= 20
equations[i].length == 2
1 <= equations[i][0].length, equations[i][1].length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= queries[i][0].length, queries[i][1].length <= 5
equations[i][0], equations[i][1], queries[i][0], queries[i][1] 由小写英文字母与数字组成
'''

# 这道题非常好,可以用的图的DFS 和 BFS来做.
# 首先,我们要把除法运算转化成图表示,比如a->b = 2.0 b->c = 3.0,a,b,c看出节点,相处所的值为权值.那么a/c = ?就是相当于,a->c <==> a->b->c = 2.0*3.0= 6,所以我们要把已知条件建图!
# 接下来,就是遍历方法,这里有两种方法,
# 一种是DFS,一种是BFS
# 这两种方法还是看代码一步一步理解较好!

# DFS
class Solution:
  def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        from collections import defaultdict
        graph = defaultdict(set)
        weight = defaultdict()
        lookup = {}
        # 建图
        for idx, equ in enumerate(equations):
            graph[equ[0]].add(equ[1])
            graph[equ[1]].add(equ[0])
            weight[tuple(equ)] = values[idx]
            weight[(equ[1], equ[0])] = float(1 / values[idx])

        # 深度遍历(DFS)
        def dfs(start, end, vistied):
            # 当图中有此边,直接输出
            if (start, end) in weight:
                return weight[(start, end)]
            # 图中没有这个点
            if start not in graph or end not in graph:
                return 0
            # 已经访问过
            if start in vistied:
                return 0
            vistied.add(start)
            res = 0
            for tmp in graph[start]:
                res = (dfs(tmp, end, vistied) * weight[(start, tmp)])
                # 只要遍历到有一个不是0的解就跳出
                if res != 0:
                    # 添加此边,以后访问节省时间
                    weight[(start, end)] = res
                    break
            vistied.remove(start)
            return res

        res = []
        for que in queries:
            # 用集合记录是否已经访问节点
            tmp = dfs(que[0], que[1], set())
            if tmp == 0:
                tmp = -1.0
            res.append(tmp)
        return res
# BFS
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict, deque
        graph = defaultdict(set)
        weight = defaultdict()
        lookup = {}
        # 建图
        for idx, equ in enumerate(equations):
            graph[equ[0]].add(equ[1])
            graph[equ[1]].add(equ[0])
            weight[tuple(equ)] = values[idx]
            weight[(equ[1], equ[0])] = float(1 / values[idx])
        res = []
        for start, end in queries:
            if (start, end) in weight:
                res.append(weight[(start, end)])
                continue
            if start not in graph or end not in graph:
                res.append(-1)
                continue
            if start == end:
                res.append(1.0)
                continue
            stack = deque()
            # 将从start点可以到达下一个节点压入栈内
            for tmp in graph[start]:
                stack.appendleft((tmp, weight[(start, tmp)]))
            # 记录访问节点
            visited = {start}
            # 为了跳出双循环
            flag = False
            while stack:
                c, w = stack.pop()
                if c == end:
                    flag = True
                    res.append(w)
                    break
                visited.add(c)
                for n in graph[c]:
                    if n not in visited:
                        weight[(start, n)] = w * weight[(c, n)]
                        stack.appendleft((n, w * weight[(c, n)]))
            if flag:
                continue
            res.append(-1.0)
        return res