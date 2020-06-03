'''
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。
一个数独。
答案被标成红色。

Note:
给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。
'''

'''
一种枚举子方块的提示是：
使用 方块索引= (行 / 3) * 3 + 列 / 3
其中 / 表示整数除法。

算法

现在准备好写回溯函数了
backtrack(row = 0, col = 0)。

从最左上角的方格开始 row = 0, col = 0。直到到达一个空方格。

从1 到 9 迭代循环数组，尝试放置数字 d 进入 (row, col) 的格子。

    如果数字 d 还没有出现在当前行，列和子方块中：

        将 d 放入 (row, col) 格子中。
        记录下 d 已经出现在当前行，列和子方块中。
        如果这是最后一个格子row == 8, col == 8 ：
            意味着已经找出了数独的解。
        否则
            放置接下来的数字。
        如果数独的解还没找到：
            将最后的数从 (row, col) 移除
'''
from collections import defaultdict


class Solution1:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def could_place(d, row, col):
            """
            Check if one could place a number d in (row, col) cell
            """
            return not (d in rows[row] or d in columns[col] or \
                        d in boxes[box_index(row, col)])

        def place_number(d, row, col):
            """
            Place a number d in (row, col) cell
            """
            rows[row][d] += 1  # 更新行字典
            columns[col][d] += 1  # 更新列字典
            boxes[box_index(row, col)][d] += 1  # 更新块字典
            board[row][col] = str(d)

        def remove_number(d, row, col):
            """
            Remove a number which didn't lead
            to a solution
            """
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'

        def place_next_numbers(row, col):
            """
            Call backtrack function in recursion
            to continue to place numbers
            till the moment we have a solution
            """
            # if we're in the last cell
            # that means we have the solution
            if col == N - 1 and row == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            # if not yet
            else:
                # if we're in the end of the row
                # go to the next row
                if col == N - 1:
                    backtrack(row + 1, 0)
                # go to the next column
                else:
                    backtrack(row, col + 1)

        def backtrack(row=0, col=0):
            """
            Backtracking
            """
            # if the cell is empty
            if board[row][col] == '.':
                # iterate over all numbers from 1 to 9
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        # if sudoku is solved, there is no need to backtrack
                        # since the single unique solution is promised
                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)

        # box size
        n = 3
        # row size
        N = n * n
        # lambda function to compute box index
        box_index = lambda row, col: (row // n) * n + col // n

        # init rows, columns and boxes
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        # 1.先初始化3个map
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)

        sudoku_solved = False
        # 2.开始回溯
        backtrack()


'''
    /**
     * 回溯
     * 回溯解法：https://leetcode-cn.com/problems/sudoku-solver/solution/zi-cong-wo-xue-hui-liao-hui-su-suan-fa-zhong-yu-hu/
     * 逐行，从左到右，在每一个位置上试探1-9，成功就进入下一个位置，失败就取消本次选择，做下一个选择
     * 当前行试探完毕就换行，知道换到最后一行
     *
     * @param board
     */
    public void solution(char[][] board) {
        // 非法数独
        if (board == null || board.length != 9 || board[0] == null || board[0].length != 9)
            return;
        // 回溯法解决
        backTrace(board, 0, 0);
    }

    private boolean backTrace(char[][] board, int row, int col){
        int n = board.length; // 9
        // 当前行已全部试探过，换到下一行第一个位置
        if (col == 9)
            return backTrace(board, row + 1, 0);
        // 满足结束条件，全部行全部位置都已试探过
        if (row == n)
            // 最后一行最后一个位置[8][8]试探过后会试探[8][9]，会执行[9][0]，返回
            return true;
        // 这个位置数字已给出，不需要试探，直接试探下一个位置
        if (board[row][col] != '.')
            return backTrace(board, row, col + 1);
        // 遍历可选择列表(各选择之间并列)
        for (char c = '1'; c <= '9'; c++){
            // 排除不合法的选择
            if (!isValid(board, row, col, c))
                continue;
            // 做选择
            board[row][col] = c;
            // 进行下一步试探，发现当前选择能成功进行下去，就继续往下
            if (backTrace(board, row, col + 1))
                return true;
            // 撤销本次选择，并列进行下一次选择的试探
            board[row][col] = '.';
        }
        // 这个位置把1-9都试过了，都无法继续下去，说明上一次的选择失败，需要回溯
        return false;
    }

    /**
     * 判断 board[row][col]位置放入字符 ch,是否合理
     * 也就判断这个字符有没有在 同一行，同一列，同一个子数独中出现过
     * 行列比较容易，就是一个for循环
     * 而对于 给定的 board[i][j]，它所在的子数独的索引是 (i / 3) * 3 + j / 3
     * 要扫描这个子数独中的全部9个元素，for循环可以这样写
     * boardIndex = (i / 3) * 3 + j / 3
     * for(int k = 0; k < 9; k++){
     * board[(i/3)*3 + k/3][(j/3)*3 + k % 3]
     * }
     * 因为 i和j是确定的，所以 i / 3 * 3可以确定他所在的子数独在第一个三行，还是第二个三行，还是第三个三行
     * j / 3 * 3可以确定它所在的子数独是前三列还是中散列还是后三列，
     * 相当于这两个只是确定了这个【子数独的左上角坐标】，而需要借助 k 完全对这个9个位置的扫描
     *
     * @param board
     * @param row
     * @param col
     * @param ch
     * @return
     */
    private boolean isValid(char[][] board, int row, int col, char ch) {
        // 三个方向，任一方向重复，ch就不能放在这个位置
        for (int k = 0; k < 9; k++) {
            // 同一行九个位置已出现 ch
            if (board[row][k] == ch) return false;
            // 同一列九个位置中已出现 ch
            if (board[k][col] == ch) return false;
            // 同一个子数独九个位置中已出现 ch
            if (board[(row / 3) * 3 + k / 3][(col / 3) * 3 + k % 3] == ch) return false;
        }
        return true;
    }

'''
from collections import defaultdict
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 非法数独
        if not board or len(board) != 9 or len(board[0]) != 9 or not board[0]:
            return
        N = 9
        n = 3
        box_index = lambda row, col: (row // n) * n + col // n
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        # 1.先初始化3个map
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    # 注意，这里第二个索引应该是d!
                    rows[i][d] += 1
                    columns[j][d] += 1
                    boxes[box_index(i, j)][d] += 1  # 更新块字典

        def backTrace(board, row, col):
            def isValid(board, row, col, d):
                return not (d in rows[row] or d in columns[col] or d in boxes[box_index(row, col)])

            def place_number(d, row, col):
                rows[row][d] += 1  # 更新行字典
                columns[col][d] += 1  # 更新列字典
                boxes[box_index(row, col)][d] += 1  # 更新块字典
                # board[row][col] = str(d)

            def remove_number(d, row, col):
                del rows[row][d]
                del columns[col][d]
                del boxes[box_index(row, col)][d]
                board[row][col] = '.'

            if col == 9:
                # 这里需要return，因为在回溯的时候需要判断下一个节点是否合法
                return backTrace(board, row + 1, 0)
            if row == 9:
                return True
            if board[row][col] != ".":
                return backTrace(board, row, col + 1)
            for c in range(1, 10):
                if not isValid(board, row, col, c):
                    continue
                # 选择
                place_number(c, row, col)
                board[row][col] = str(c)
                # 回溯，进行下一步试探，发现当前选择能成功进行下去，就继续往下
                if backTrace(board, row, col + 1):
                    return True
                # 撤销选择
                board[row][col] = "."
                remove_number(c, row, col)
            return False

        backTrace(board, 0, 0)


print(Solution().solveSudoku(
    [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
