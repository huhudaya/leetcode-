'''

在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。

每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。

请你返回最终形体的表面积。
示例 1：

输入：[[2]]
输出：10
示例 2：

输入：[[1,2],[3,4]]
输出：34
示例 3：

输入：[[1,0],[0,2]]
输出：16
示例 4：

输入：[[1,1,1],[1,0,1],[1,1,1]]
输出：32
示例 5：

输入：[[2,2,2],[2,1,2],[2,2,2]]
输出：46
提示：
1 <= N <= 50
0 <= grid[i][j] <= 50
'''
'''
发现只要是两个立方体有重合的部分，就得减去 2 个单位，因此只要计算一下重合的部分就好了。用这种思路把每一个示例都计算过去，发现是可行的。

1、垂直累加上去的；

这部分特别好计算，只要是当前单元格的值严格大于 11，就有重叠的部分，重叠的部分是当前单元格的值 - 1−1。

2、一行一行看，重叠的部分；

重叠的部分是相邻两个单元格在行的视角的值的最小值。

3、一列一列看，重叠的部分；

重叠的部分是相邻两个单元格在列的视角的值的最小值。
'''

# Java
'''
public class Solution {

    public int surfaceArea(int[][] grid) {
        // 习惯上应该做参数检查，但题目中给出了 N >= 1 ，故可以略去
        int rows = grid.length;
        // 题目保证了输入一定是 N * N，但为了使得程序适用性更强，还是单独把 cols 做赋值
        int cols = grid[0].length;

        int sum = 0;
        // 垂直重叠
        int verticalOverlap = 0;
        // 行重叠
        int rowOverlap = 0;
        // 列重叠
        int colOverlap = 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                sum += grid[i][j];
                // 垂直
                if (grid[i][j] > 1) {
                    verticalOverlap += (grid[i][j] - 1);
                }
                // 行
                if (j > 0) {
                    rowOverlap += Math.min(grid[i][j - 1], grid[i][j]);
                }
                // 列
                if (i > 0) {
                    colOverlap += Math.min(grid[i - 1][j], grid[i][j]);
                }
            }
        }
        return sum * 6 - (verticalOverlap + rowOverlap + colOverlap) * 2;
    }

    public static void main(String[] args) {
        // int[][] grid = {{2}};
        // int[][] grid = {{1, 2}, {3, 4}};
        // int[][] grid = {{1, 0}, {0, 2}};
        // int[][] grid = {{1, 1, 1}, {1, 0, 1}, {1, 1, 1}};

        int[][] grid = {{1, 0, 2}, {2, 1, 2}};
        Solution solution = new Solution();

        int res = solution.surfaceArea(grid);
        System.out.println(res);
    }
}
'''


# 思路主要有两个
#     1.直接计算有效面积
#     2.计算重叠的个数，然后总表面积-重叠部分的面积

# 直接计算法
class Solution(object):
    def surfaceArea(self, grid):
        N = len(grid)
        ans = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    ans += 2
                    # 计算四周
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        # 注意边界
                        if 0 <= nr < N and 0 <= nc < N:
                            # 垂直方向上
                            nval = grid[nr][nc]
                        else:
                            nval = 0
                        # 计算有效面积 即非挡住的部分 使用max确保有效面积只会计算一次
                        ans += max(grid[r][c] - nval, 0)
        return ans