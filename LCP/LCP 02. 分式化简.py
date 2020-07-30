'''
有一个同学在学习分式。他需要将一个连分数化成最简分数，你能帮助他吗？



连分数是形如上图的分式。在本题中，所有系数都是大于等于0的整数。

 

输入的cont代表连分数的系数（cont[0]代表上图的a0，以此类推）。返回一个长度为2的数组[n, m]，使得连分数的值等于n / m，且n, m最大公约数为1。

 

示例 1：

输入：cont = [3, 2, 0, 2]
输出：[13, 4]
解释：原连分数等价于3 + (1 / (2 + (1 / (0 + 1 / 2))))。注意[26, 8], [-13, -4]都不是正确答案。
示例 2：

输入：cont = [0, 0, 3]
输出：[3, 1]
解释：如果答案是整数，令分母为1即可。
限制：

cont[i] >= 0
1 <= cont的长度 <= 10
cont最后一个元素不等于0
答案的n, m的取值都能被32位int整型存下（即不超过2 ^ 31 - 1）。
'''
'''
思路：从an处开始计算，依次向前推进。
line3,line4:分别为1/an的分子和分母；
line5:因为从最后的分式向前计算，循环也从后向前进行；
line6:交换分子分母，实际上是将第n个分式的分母交换到第n-1个分式的分子位置上；
line7:计算第n-1个分式的分母；
line8:返回最终结果。
在传统笔算里，一般是先通分、相加，最后分子分母互换，但在程序里，顺序恰好相反。
'''
from typing import List


class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        if not cont:
            return []
        n = len(cont)
        up = cont[-1]
        down = 1
        for i in range(n - 1, 0, -1):
            up, down = down, up
            up = down * cont[i - 1] + up
        return [up, down]

Solution().fraction([3,2])