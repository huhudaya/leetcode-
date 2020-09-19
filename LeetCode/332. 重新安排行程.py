'''
给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点
对该行程进行重新规划排序。所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生
所以该行程必须从 JFK 开始

题意意思，找一条从JFK出发把所有路径走完，并按字典排序

说明:

如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。
例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
所有的机场都用三个大写字母表示（机场代码）
假定所有机票至少存在一种合理的行程。
示例 1:

输入: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
输出: ["JFK", "MUC", "LHR", "SFO", "SJC"]
示例 2:

输入: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
输出: ["JFK","ATL","JFK","SFO","ATL","SFO"]
解释: 另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后
'''

'''1.比较容易理解的方式：'''
# 类似大部分基本深搜，每次对当前出发点的“剩余可用目的地”循环，优先去名字值小的
# 但无论以递归入参还是全局变量的方式，每次进递归需层数+1，选择的ticket要暂时标为已用，即当前form-to的剩余可用次数-1
# 结束条件是层数达到完全遍历，若未达到又无可用目的地，说明这条路走不通了，回溯时需还原层数、可用次数

'''2.更烧脑但更简洁的方式：'''
# 因题目强调了“假定所有机票至少存在一种合理的行程”，所以可利用深搜一定会有结果这一点，无需任何标记、判定，仅单纯对每层进行循环及扣除
# 也就是每次进递归，还是对当前“剩余可用目的地”循环，但选择名字值小的进入下层时直接扣除这张机票
# 这样任意循环若还能进行，说明还有机票没用；反之一定是“基于已经出现的终点，自身成为更早部分的终点”
# 这里有点绕，举例来说第一个结束循环的一定是唯一一个这样的机场：他作为机票的终点的总次数，比作为起点的总次数多1
# 也就是说JFK恰好是唯一相反的机场，而其它机场作为起点和终点的总次数一定相同
# 所以最早结束循环的递归，一定是入参为终点时，将其加入行程数组；第二个出现的，则是之前行程中，唯一可作为终点的
# 以此类推……最后行程数组反向，即为答案

# 本人py3的代码：
import collections


class Solution:
    def findItinerary(self, tickets):
        paths = collections.defaultdict(list)
        for start, tar in tickets:
            paths[start].append(tar)
        for start in paths:
            paths[start].sort(reverse=True)
        s = []

        def search(start):
            while paths[start]:
                search(paths[start].pop())
            s.append(start)

        search("JFK")
        return s[::-1]


from typing import List
import heapq


# 我们注意到只有那个入度与出度差为 1 的节点会导致死胡同。
# 而该节点必然是最后一个遍历到的节点。我们可以改变入栈的规则
# 当我们遍历完一个节点所连的所有节点后，我们才将该节点入栈（即逆序入栈）
# 对于当前节点而言，从它的每一个非「死胡同」分支出发进行深度优先搜索，都将会搜回到当前节点。
# 而从它的「死胡同」分支出发进行深度优先搜索将不会搜回到当前节点。
# 也就是说当前节点的死胡同分支将会优先于其他非「死胡同」分支入栈。
'''
Hierholzer 算法用于在连通图中寻找欧拉路径，其流程如下：

    1.从起点出发，进行深度优先搜索。

    2.每次沿着某条边从某个顶点移动到另外一个顶点的时候，都需要删除这条边。

    3.如果没有可移动的路径，则将所在节点加入到栈中，并返回。
'''
# 时间复杂度O(mlogm),m是边的数量，对于每一条边都需要O(logm)的删除它
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(curr: str):
            while vec[curr]:
                # 弹出一个值，然后维护堆的数据结构，logN的时间复杂度
                tmp = heapq.heappop(vec[curr])
                # 继续dfs,直到遇到死路
                dfs(tmp)
            # 如果是死路一条，那么放入栈中
            stack.append(curr)

        vec = collections.defaultdict(list)
        for depart, arrive in tickets:
            vec[depart].append(arrive)

        for key in vec:
            heapq.heapify(vec[key])

        stack = list()
        dfs("JFK")
        return stack[::-1]


# 回溯
class Solution:
    def findItinerary(self, tickets):
        from collections import defaultdict
        ticket_dict = defaultdict(list)
        # 构建邻接表
        for item in tickets:
            ticket_dict[item[0]].append(item[1])

        path = ['JFK']

        def backtrack(cur_from):
            if len(path) == len(tickets) + 1:  # 结束条件
                return True
            ticket_dict[cur_from].sort()
            for _ in ticket_dict[cur_from]:
                cur_to = ticket_dict[cur_from].pop(0)  # 删除当前节点
                path.append(cur_to)  # 做选择
                if backtrack(cur_to):  # 进入下一层决策树
                    return True
                path.pop()  # 取消选择
                ticket_dict[cur_from].append(cur_to)  # 恢复当前节点
            return False

        backtrack('JFK')
        return path
