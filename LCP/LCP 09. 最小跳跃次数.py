'''
为了给刷题的同学一些奖励，力扣团队引入了一个弹簧游戏机。
游戏机由 N 个特殊弹簧排成一排，编号为 0 到 N-1。
初始有一个小球在编号 0 的弹簧处。
若小球在编号为 i 的弹簧处，通过按动弹簧，可以选择把小球向右弹射 jump[i] 的距离，或者向左弹射到任意左侧弹簧的位置。
也就是说，在编号为 i 弹簧处按动弹簧，小球可以弹向 0 到 i-1 中任意弹簧或者 i+jump[i] 的弹簧（若 i+jump[i]>=N ，则表示小球弹出了机器）。
小球位于编号 0 处的弹簧时不能再向左弹。
为了获得奖励，你需要将小球弹出机器。
请求出最少需要按动多少次弹簧，可以将小球从编号 0 弹簧弹出整个机器，即向右越过编号 N-1 的弹簧。

示例 1：
输入：jump = [2, 5, 1, 1, 1, 1]
输出：3
解释：小 Z 最少需要按动 3 次弹簧，小球依次到达的顺序为 0 -> 2 -> 1 -> 6，最终小球弹出了机器。
限制：
1 <= jump.length <= 10^6
1 <= jump[i] <= 10000
链接：https://leetcode-cn.com/problems/zui-xiao-tiao-yue-ci-shu
'''
# 动态规划dp
'''
我们可以利用一个巧妙的性质来使用动态规划：假设某一个位置只需要 w 步可以跳到，那么这个位置之前的步数，最多只需要 w+1 步。
所以我们可以用一个数组 maxdis[w] 表示 w 步可以跳到的最远位置。对于位置 i而言，满足 maxdis[w] > i 条件的最小 w+1 是往左跳到达 i 的最小操作次数。
因此递推方程为
    1.f[i] = min(f[i], w+1): 用往左跳到达 i 的最小操作数 w+1
    2.f[i+jump[i]] = min(f[i+jump[i],f[i]+1): 从 i 往右跳到 i+jump[i] 更新 f[i+jump[i]]
    3.maxdis[f[i+jump[i]]] = max(maxdis[f[i+jump[i]]], i+jump[i]): 更新 f[i+jump[i]] 次操作到达最远距离。
我们知道 maxdis 是单调的，所以只需要一个单调指针维护对应的 w 即可。

注意：
i 表示当前的位置
f[i]表示到达 i 位置最小需要多少步
数组 maxdis[w]的值 表示 w 步可以跳到的最远位置
'''

from typing import List


class Solution:
    def minJump(self, jump: List[int]) -> int:
        res = n = len(jump)
        f = [n] * (n + 1)  # f[i]表示到达 i 位置需要的的最小步数
        f[0] = 0
        max_dis = [0] * (n + 1)
        curr_min_num = 0
        for i in range(0, n):
            # 如果当前位置 i 超过了当前步数可以跳到的最大位置，则步数+1
            if i > max_dis[curr_min_num]:  # max_dis[w]表示 w 步可以到达的最远距离
                curr_min_num += 1  # 步数+1
            f[i] = min(f[i], curr_min_num + 1)  # 用往左跳到达 i 的最小操作数 w+1

            jump_tmp = i + jump[i]
            if jump_tmp >= n:
                res = min(res, f[i] + 1)
            else:
                f[jump_tmp] = min(f[jump_tmp], f[i] + 1)  # 从 i 往右跳到 i+jump[i] 更新 f[i+jump[i]]
                max_dis[f[i] + 1] = max(max_dis[f[i] + 1], jump_tmp)  # 更新 f[i+jump[i]] 次操作到达最远距离。
        return res



'''
常规广度优先搜索在处理弹簧往左跳的情况时，时间复杂度到达 O(N^2)。
在常规广度优先搜索的基础上，我们可以记录一个最大的 far 值进行优化，用来表示当前从 [0, far-1] 均已被搜索到。
因此当搜索到编号 i 弹簧时，往左跳的操作，仅需遍历 [far, i-1] 区间（ far <= i-1 ）；
搜索结束时，更新 far = max(far, i+1)。
由于 far 的更新操作，使往左跳操作的遍历区间是不存在重复的，因此往左跳遍历的总时间复杂度为 O(N)
'''


class Solution:
    def minJump(self, jump):
        res = n = len(jump)
        visited = [False] * (n + 1)
        queue = [[0, 1]]
        visited[0] = True
        curr, far = 0, 1
        while curr < len(queue):
            idx, step = queue[curr][0], queue[curr][1]
            curr += 1
            if idx + jump[idx] >= n:
                return step
            if not visited[idx + jump[idx]]:
                queue.append([idx + jump[idx], step + 1])
                visited[idx + jump[idx]] = True
            for j in range(far, idx):
                if not visited[j]:
                    queue.append([j, step + 1])
                    visited[j] = True
            far = max(far, idx + 1)
        return -1


'''
1.核心思想为BFS，记录当前位置及到达当前位置需要的jump数。
2.注意事项：记录已访问过的最大index，该index左边的弹簧均已被遍历，从而避免重复访问。
'''


class Solution:
    def minJump(self, jump: List[int]) -> int:
        visit = [0 for _ in range(len(jump))]
        # 队列，记录一个元组：（当前位置，当前jump次数）
        # 初始状态为（0，0）, 入队列
        q = [(0, 0)]
        visit[0] = 1
        # 该参数记录已访问过的最大index，该位置左边的弹簧均已被遍历
        # 对于i<=max_left_idx, visit[i]==1。
        max_left_idx = 0
        # BFS遍历
        while q:
            cur_idx, count = q.pop(0)
            # 情况1: 向右跳
            right_idx = cur_idx + jump[cur_idx]
            # 小球弹出机器只可能发生在向右跳的情况，小球弹出时返回答案
            if right_idx >= len(jump):
                return count + 1
            else:
                if not visit[right_idx]:
                    q.append((right_idx, count + 1))
                    visit[right_idx] = 1
            # 情况2: 向左跳
            # max_left_idx左边的弹簧已经遍历过，不需要再访问，直接从max_left_idx+1开始遍历至cur_idx
            # 如果不设置该参数，需要从0遍历置cur_idx，造成TLE错误
            for i in range(max_left_idx + 1, cur_idx):
                if not visit[i]:
                    q.append((i, count + 1))
                    visit[i] = 1
            # 更新max_left_idx的值，即当前cur_idx左边的弹簧已经遍历过
            max_left_idx = max(cur_idx, max_left_idx)
Solution().minJump([2, 5, 1, 1, 1, 1])


# 官方  bfs用一个队列替代递归函数来表示bfs
class Solution:
    def minJump(self, jump):
        res = n = len(jump)
        visited = [False] * (n + 1)
        # 定义一个队列
        queue = [[0, 1]]
        visited[0] = True
        # 最大的 far 值进行优化，用来表示当前从 [0, far-1] 均已被搜索到
        curr, far = 0, 1
        while curr < len(queue):
            idx, step = queue[curr][0], queue[curr][1]
            curr += 1
            if idx + jump[idx] >= n:
                return step
            if not visited[idx + jump[idx]]:
                queue.append([idx + jump[idx], step + 1])
                visited[idx + jump[idx]] = True
            for j in range(far, idx):
                if not visited[j]:
                    queue.append([j, step + 1])
                    visited[j] = True
            far = max(far, idx + 1)
        return -1
