'''
累加数是一个字符串，组成它的数字可以形成累加序列。

一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。

给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。

说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。

示例 1:

输入: "112358"
输出: true
解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
示例 2:

输入: "199100199"
输出: true
解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
进阶:
你如何处理一个溢出的过大的整数输入?
'''


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        self.res = False  # 假定结果为False

        def backTrack(rest, tmp_cnt, last1, last2):
            """
            rest为剩余部分
            tmp_cnt为当前已选数字个数----"112358"-->1,1,2,3,5,8->tmp_cnt==6
            last1,last2为前两个数
            """
            if tmp_cnt <= 2 and not rest:  # 结果小于两个数，并且rest为空
                return
            if not rest:  # rest为空
                self.res = True
                return

            for i in range(len(rest)):
                if len(rest[:i + 1]) != len(str(int(rest[:i + 1]))):
                    # 剪枝--单个的0可以作为一个数，而01，02之类的不能，直接返回
                    return
                if tmp_cnt >= 2:  # 当tmp_cnt>=2时即已经分出两个数时才需要判断
                    if int(rest[:i + 1]) == last1 + last2:  # 剪枝--
                        backTrack(rest[i + 1:], tmp_cnt + 1, last2, int(rest[:i + 1]))
                else:
                    backTrack(rest[i + 1:], tmp_cnt + 1, last2, int(rest[:i + 1]))
                if self.res:  # 剪枝--当res已经为True时，可以不用继续回溯了，直接返回
                    return

        backTrack(num, 0, 0, 0)
        return self.res
