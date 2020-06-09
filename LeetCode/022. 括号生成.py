# 022. 括号生成.py
'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

链接：https://leetcode-cn.com/problems/generate-parentheses
'''
# 核心思路
# 回溯说白了就是深度优先遍历的特殊形式！！！
'''
画图以后，可以分析出的结论：

当前左右括号都有大于 0 个可以使用的时候，才产生分支

产生左分支的时候，只看当前是否还有左括号可以使用

产生右分支的时候，还受到左分支的限制，右边剩余可以使用的括号数量一定得在严格大于左边剩余的数量的时候，才可以产生分支

在左边和右边剩余的括号数都等于 0 的时候结算
'''

# 回溯法
class Solution:
    def generateParenthesis(self, n: int):
        res = []
        if n == 0:
            return res
        self.dfs("", 0, 0, n, res)
        return res
    '''
     * @param curStr 当前递归得到的结果
     * @param left   左括号用了几个
     * @param right  右括号用了几个
     * @param n      左括号、右括号一共用几个
     * @param res    结果集
    '''
    def dfs(self, curStr, left, right, n, res):
        # 递归结束条件
        if left == n and right == n:
            res.append(curStr)
            return 
        # 如果左括号还没凑够，继续凑
        if left < n:
            # 拼接上一个左括号，并且使用的左括号个数加 1
            self.dfs(curStr+"(", left + 1, right, n, res)
        # // 什么时候可以用右边？例如，(((((()，此时 left > right，
        # // 不能用等号，因为只有先拼了左括号，才能拼上右括号
        if right < n and left > right:
            # 拼接上一个右括号，并且使用的右括号个数加 1
            self.dfs(curStr + ")", left, right + 1, n, res)