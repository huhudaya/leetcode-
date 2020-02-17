'''
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。


上图是一个部分填充的有效的数独。

数独部分空格内已填入了数字，空白格用 '.' 表示。

示例 1:

输入:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: true
示例 2:

输入:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: false
解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
     但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
说明:

一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
给定数独序列只包含数字 1-9 和字符 '.' 。
给定数独永远是 9x9 形式的。
'''

# 方法一
'''
一个简单的解决方案是遍历该 9 x 9 数独 三 次，以确保：

行中没有重复的数字。
列中没有重复的数字。
3 x 3 子数独内没有重复的数字。
实际上，所有这一切都可以在一次迭代中完成。

方法：一次迭代
首先，让我们来讨论下面两个问题：

如何枚举子数独？
可以使用 box_index = (row / 3) * 3 + columns / 3，其中 / 是整数除法。

如何确保行 / 列 / 子数独中没有重复项？
可以利用 value -> count 哈希映射来跟踪所有已经遇到的值。

现在，我们完成了这个算法的所有准备工作：

遍历数独。
检查看到每个单元格值是否已经在当前的行 / 列 / 子数独中出现过：
    如果出现重复，返回 false。
    如果没有，则保留此值以进行进一步跟踪。
返回 true。

时间复杂度：O(1)，因为我们只对 81 个单元格进行了一次迭代。
空间复杂度：O(1)。

'''


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # init data
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]
        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    # 这里的box_index是标志该条记录属于哪一个块状区域
                    box_index = (i // 3) * 3 + j // 3
                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True



# 自己的版本
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        核心思想
        行中没有重复的数字。
        列中没有重复的数字。
        3 x 3 子数独内没有重复的数字。
        '''
        # 遍历9行
        rows = [{} for _ in range(9)]
        # 遍历9列
        col = [{} for _ in range(9)]
        # 将9*9的网格分成 9 块
        boxes = [{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                # 当前元素的值
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3
                    # 行 hash 第i行的num值
                    rows[i][num] = rows[i].get(num, 0) + 1
                    # 列 hash 第j列的num值
                    col[j][num] = col[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    # check
                    if rows[i][num] > 1 or col[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True