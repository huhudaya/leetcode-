'''

在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。



示例 1：



输入：[[2,1,1],[1,1,0],[0,1,1]]
输出：4
示例 2：

输入：[[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
示例 3：

输入：[[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。


提示：

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] 仅为 0、1 或 2
'''
# java
'''
先找出腐烂的橘子，添加进 queue 中。
队列 queue 只让腐烂的橘子入队；
出队时，让当前腐烂橘子四周的新鲜橘子都变为腐烂，即 grid[newX][newY] = 2。
用 minute 记录腐烂的持续时间，每一层的橘子在内一层的橘子的腐烂时间基础之上自增 1，代表时间过了 1 分钟。
最后检查网格中是否还有新鲜的橘子：
有，返回 -1 代表 impossible。
没有则返回 minute。
'''
# 给橘子标记有时间
'''
class Pos {
    int x, y, minute;
    public Pos(int _x, int _y, int _minute) {
        x = _x;
        y = _y;
        minute = _minute;
    }
}
static int[][] dir = { {-1,0},{1,0},{0,-1},{0,1} };

public int orangesRotting(int[][] grid) {
    int R = grid.length;
    int C = grid[0].length;
    int minute = 0;
    Queue<Pos> queue = new LinkedList<>();

    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++)
        if (grid[i][j] == 2)                 //先找出腐烂的橘子
            queue.add(new Pos(i, j, minute));
    }
    while (!queue.isEmpty()) {
        Pos pos = queue.poll();
        minute = pos.minute;            //当前层橘子的腐烂周期
        for (int k = 0; k < 4; k++) {   //一个腐烂，四个方向的橘子都会腐烂
            int newX = pos.x + dir[k][0];
            int newY = pos.y + dir[k][1];
            if (newX >= 0 && newX < R && newY >= 0 && newY < C && grid[newX][newY] == 1) {
                grid[newX][newY] = 2;  //标记腐烂
                queue.add(new Pos(newX, newY, pos.minute + 1)); //外层橘子腐烂周期自增1
            }
        }
    }
    //check for fresh oranges
    for(int[] row : grid) {
        for (int i : row)
            if (i == 1) return -1;
    }
    return minute;
}
'''
# 题解
'''
BFS 可以看成是层序遍历
从某个结点出发，BFS 首先遍历到距离为 1 的结点，然后是距离为 2、3、4…… 的结点
因此，BFS 可以用来求最短路径问题。BFS 先搜索到的结点，一定是距离最近的结点

再看看这道题的题目要求：返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数
翻译一下，实际上就是求腐烂橘子到所有新鲜橘子的最短路径。那么这道题使用 BFS，应该是毫无疑问的了
我们都知道 BFS 需要使用队列，代码框架是这样子的（伪代码）：

Python
while queue 非空:
	node = queue.pop()
    for node 的所有相邻结点 m:
        if m 未访问过:
            queue.push(m)
但是用 BFS 来求最短路径的话，这个队列中第 1 层和第 2 层的结点会紧挨在一起，无法区分
因此，我们需要稍微修改一下代码，在每一层遍历开始前，记录队列中的结点数量 n ，然后一口气处理完这一层的 n 个结点

代码框架是这样的：
depth = 0 # 记录遍历到第几层
while queue 非空:
    depth += 1
    n = len(queue) #中的元素个数
    for i in range(n):
        node = queue.pop()
        for node 的所有相邻结点 m:
            if m 未访问过:
                queue.push(m)
'''
'''
有了计算最短路径的层序 BFS 代码框架，写这道题就很简单了
这道题的主要思路是：

一开始，我们找出所有腐烂的橘子，将它们放入队列，作为第 0 层的结点
然后进行 BFS 遍历，每个结点的相邻结点可能是上、下、左、右四个方向的结点，注意判断结点位于网格边界的特殊情况
由于可能存在无法被污染的橘子，我们需要记录新鲜橘子的数量

在 BFS 中
每遍历到一个橘子（污染了一个橘子），就将新鲜橘子的数量减一
如果 BFS 结束后这个数量仍未减为零，说明存在无法被污染的橘子

public int orangesRotting(int[][] grid) {
    int M = grid.length;
    int N = grid[0].length;
    Queue<int[]> queue = new LinkedList<>();

    int count = 0; // count 表示新鲜橘子的数量
    for (int r = 0; r < M; r++) {
        for (int c = 0; c < N; c++) {
            if (grid[r][c] == 1) {
                count++;
            } else if (grid[r][c] == 2) {
                queue.add(new int[]{r, c});
            }
        }
    }

    int round = 0; // round 表示腐烂的轮数，或者分钟数
    while (count > 0 && !queue.isEmpty()) {
        round++;
        int n = queue.size();
        for (int i = 0; i < n; i++) {
            int[] orange = queue.poll();
            int r = orange[0];
            int c = orange[1];
            if (r-1 >= 0 && grid[r-1][c] == 1) {
                grid[r-1][c] = 2;
                count--;
                queue.add(new int[]{r-1, c});
            }
            if (r+1 < M && grid[r+1][c] == 1) {
                grid[r+1][c] = 2;
                count--;
                queue.add(new int[]{r+1, c});
            }
            if (c-1 >= 0 && grid[r][c-1] == 1) {
                grid[r][c-1] = 2;
                count--;
                queue.add(new int[]{r, c-1});
            }
            if (c+1 < N && grid[r][c+1] == 1) {
                grid[r][c+1] = 2;
                count--;
                queue.add(new int[]{r, c+1});
            }
        }
    }

    if (count > 0) {
        return -1;
    } else {
        return round;
    }
}
'''

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 网格的长，宽
        m, n = len(grid), len(grid[0])
        # 网格每一个坐标的访问状态
        visit = [[False] * n for y in range(m)]
        # 找出最开始时，网格中所有坏橘子的坐标
        stack = [[y, x] for y in range(m) for x in range(n) if grid[y][x] == 2]
        # 坏橘子传染好橘子的四个方向，上下左右
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # 初始时间
        minute = 0

        # 开始坏橘子传染好橘子的循环，直到没有好橘子可以被传染
        while True:
            # 初始化一个stack_next，把这一轮变坏的橘子装进里面
            stack_next = []
            # 开始对坏橘子进行审查，主要是看上下左右有没有好橘子
            while stack:
                # 拿出坏橘子的坐标点
                y, x = stack.pop()
                # 再看坏橘子上下左右的坐标对应的坐标
                for d in direction:
                    y_new, x_new = y + d[0], x + d[1]
                    # 如果坐标在网格范围内，而且坐标没有被访问过，且这个坐标确实有个好橘子
                    if -1 < y_new < m and -1 < x_new < n and not visit[y_new][x_new] and grid[y_new][x_new] == 1:
                        # 观察慰问一下这个好橘子，表示已经访问过了
                        visit[y_new][x_new] = True
                        # 告诉这个好橘子，你已被隔壁的坏橘子感染，现在你也是坏橘子了
                        grid[y_new][x_new] = 2
                        # 放进stack_next里面，集中管理，精准隔离，方便排查下一轮会变坏的橘子
                        stack_next.append([y_new, x_new])
            # 如果橘子们都检查完了发现再无其他坏橘子，终止循环，宣布疫情结束
            if not stack_next: break
            # 把这一轮感染的坏橘子放进stack里，因为我们每一轮都是从stack开始搜索的
            stack = stack_next
            # 看来橘子们还没凉透，来，给橘子们续一秒，哦不，续一分钟
            minute += 1

        # 经过传染，审查，隔离的循环后，如果还有好橘子幸存，返回-1宣布胜利，否则返回橘子们的存活时间
        return -1 if ['survive' for y in range(m) for x in range(n) if grid[y][x] == 1] else minute


# bfs
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col, time = len(grid), len(grid[0]), 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = []
        # add the rotten orange to the queue
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j, time))
        # bfs
        while queue:
            i, j, time = queue.pop(0)
            for di, dj in directions:
                if 0 <= i + di < row and 0 <= j + dj < col and grid[i + di][j + dj] == 1:
                    grid[i + di][j + dj] = 2
                    queue.append((i + di, j + dj, time + 1))
        # if there are still fresh oranges, return -1
        for row in grid:
            if 1 in row:
                return -1

        return time


# 另外的思路
'''
先遍历数组，如果为2且相邻为1，则将相邻的数变为2，并用flag来标记说明有新的腐坏的橘子，说明下次还要再遍历。
flag有变化，则minute也加1.
最后完成循环之后，再看看数组中有没有值为1的元素，有则返回-1，否则返回时间数

'''
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 方向dir
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        cnt = 0
        _deque = deque()
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # 统计新鲜的橘子的个数
                    cnt += 1
                elif grid[i][j] == 2:
                    _deque.append((i, j))
        # 腐烂的分钟数
        minute = 0
        while cnt > 0 and _deque:
            minute += 1
            size = len(_deque)
            for i in range(size):
                # 记得是popleft
                cur_x, cur_y = _deque.popleft()
                for tmp_i, tmp_j in directions:
                    new_x = cur_x + tmp_i
                    new_y = cur_y + tmp_j
                    if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        cnt -= 1
                        _deque.append((new_x, new_y))
        if cnt > 0:
            return -1
        else:
            return minute

print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))