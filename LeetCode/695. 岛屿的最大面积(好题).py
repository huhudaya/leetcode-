'''
给定一个包含了一些 0 和 1的非空二维数组 grid 
一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合
你可以假设二维矩阵的四个边缘都被水包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。

注意: 给定的矩阵grid 的长度和宽度都不超过 50。
'''

# 方法一:官方 dfs
'''
我们想知道网格中每个连通形状的面积，然后取最大值。

如果我们在一个土地上，以 4 个方向探索与之相连的每一个土地（以及与这些土地相连的土地），那么探索过的土地总数将是该连通形状的面积。

# 置0，避免重复遍历
为了确保每个土地访问不超过一次，我们每次经过一块土地时，将这块土地的值置为 0。
这样我们就不会多次访问同一土地。
'''
from typing import List
class Solution:
    def dfs(self, grid, cur_i, cur_j):
        # 有返回值的递归一定要先写递归结束条件，注意这里会判断一下grid[cur_i][cur_j]是否为0，如果为0就return 0
        if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
            return 0
        # 这里置0，避免重复遍历
        grid[cur_i][cur_j] = 0
        ans = 1
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i, next_j = cur_i + di, cur_j + dj
            ans += self.dfs(grid, next_i, next_j)
        return ans

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                ans = max(self.dfs(grid, i, j), ans)
        return ans

# java
'''
class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int res = 0; 
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 1) {
                    res = Math.max(res, dfs(i, j, grid));
                }
            }
        } 
        return res;
    }
    // 每次调用的时候默认num为1，进入后判断如果不是岛屿，则直接返回0，就可以避免预防错误的情况。
    // 每次找到岛屿，则直接把找到的岛屿改成0，这是传说中的沉岛思想，就是遇到岛屿就把他和周围的全部沉默。
    // ps：如果能用沉岛思想，那么自然可以用朋友圈思想。有兴趣的朋友可以去尝试。
    private int dfs(int i, int j, int[][] grid) {
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[i].length || grid[i][j] == 0) { 
            return 0;
        } 
        grid[i][j] = 0;
        int num = 1;
        num += dfs(i + 1, j, grid);
        num += dfs(i - 1, j, grid);
        num += dfs(i, j + 1, grid);
        num += dfs(i, j - 1, grid);
        return num;
        
    }
}
'''
# 方法一：自己的版本 dfs
class Solution:
    # 上右下左4个方向
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid and not grid[0]:
            return -1
        m = len(grid)
        n = len(grid[0])
        # 使用marked数组
        marked = [[0] * n for i in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                # 注意这里和200题一样，需要判断一下marked数组
                if marked[i][j] == 0 and grid[i][j] == 1:
                    res = max(self.dfs(grid, i, j, m, n, marked), res)
        return res
    def dfs(self, grid, i, j, m, n, marked):
        res = 1
        # 标记marked数组
        marked[i][j] = 1
        for di_x, di_y in self.directions:
            row = i + di_x
            col = j + di_y
            # 如果未使用
            if 0 <= row < m and 0 <= col < n and marked[row][col] == 0 and grid[row][col] == 1:
                res += self.dfs(grid, row, col, m, n, marked)
            # else:
            #     res += 0
        return res


# 方法二：栈实现dfs
'''
法

我们可以用栈来实现深度优先搜索算法。这种方法本质与方法一相同，唯一的区别是：

方法一通过函数的调用来表示接下来想要遍历哪些土地，让下一层函数来访问这些土地。
而方法二把接下来想要遍历的土地放在栈里，然后在取出这些土地的时候访问它们。

访问每一片土地时，我们将对围绕它四个方向进行探索，找到还未访问的土地，加入到栈 stack 中；

另外，只要栈 stack 不为空，就说明我们还有土地待访问，那么就从栈中取出一个元素并访问。
'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                cur = 0
                stack = [(i, j)]
                while stack:
                    cur_i, cur_j = stack.pop()
                    # 剪枝
                    if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
                        continue
                    # 每次遍历都+1
                    cur += 1
                    grid[cur_i][cur_j] = 0
                    # 每次弹出栈的时候都将周围的4个元素放入栈中
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        next_i, next_j = cur_i + di, cur_j + dj
                        stack.append((next_i, next_j))
                ans = max(ans, cur)
        return ans

# 方法三：广度优先搜索
'''
算法
我们把方法二中的栈改为队列，每次从队首取出土地，并将接下来想要遍历的土地放在队尾，就实现了广度优先搜索算法。
'''
from collections import deque
class Solution:
    directions = [[-1,0],[0, 1], [1, 0], [0, -1]]
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 使用BFS
        if not grid or not grid[0]:
            return -1
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        ans = 0
        for i in range(m):
            for j in range(n):
                cur = 0
                queue.append((i, j))
                while queue:
                    cur_i, cur_j = queue.popleft()
                    # 剪枝
                    if cur_i < 0 or cur_j < 0 or cur_i == m or cur_j == n or grid[cur_i][cur_j] == 0:
                        continue
                    # 每遍历一次，次数都+1
                    cur += 1
                    # 置0，防止重复遍历
                    grid[cur_i][cur_j] = 0
                    # 遍历四个方向
                    for di in self.directions:
                        x = cur_i + di[0]
                        y = cur_j + di[1]
                        queue.append((x, y))
                ans = max(ans, cur)
        return ans


print(Solution().maxAreaOfIsland([[1,1],[1,0]]))