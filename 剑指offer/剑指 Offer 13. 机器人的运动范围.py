'''

地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动
它每次可以向左、右、上、下移动一格（不能移动到方格外）
也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？



示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20
通过次数45,319提交次数92
'''


# dfs
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        used = [[False] * n for i in range(m)]

        def cal_num(str1, str2):
            n = 0
            for i in str(str1):
                n += int(i)
            for i in str(str2):
                n += int(i)
            return n

        # dfs
        def dfs(x, y):
            res = 1
            used[x][y] = True
            for di in directions:
                row = x + di[0]
                col = y + di[1]
                if row >= 0 and row < m and col < n and col >= 0 and used[row][col] is False and cal_num(row, col) <= k:
                    res += dfs(row, col)
            return res

        return dfs(0, 0)

# bfs
# bfs(队列)
from collections import deque
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        marked = [[False] * n for i in range(m)]
        def digitsum(n, m):
            ans = 0
            while n:
                ans += n % 10
                n //= 10
            while m:
                ans += m % 10
                m //= 10
            return ans
        def bfs(x, y):
            res = 1
            queue = deque()
            queue.append((x, y))
            marked[x][y] = True
            while queue:
                x, y = queue.popleft()
                for di in directions:
                    row = x + di[0]
                    col = y + di[1]
                    if row >= 0 and row < m and col < n and col >= 0 and not marked[row][col] and digitsum(row, col) <= k:
                        res += 1
                        queue.append((row, col))
                        marked[row][col] = True
            return res
        return bfs(0, 0)
