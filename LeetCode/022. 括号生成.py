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
            self.dfs(curStr + "(", left + 1, right, n, res)
        # // 什么时候可以用右边？例如，(((((()，此时 left > right，
        # // 不能用等号，因为只有先拼了左括号，才能拼上右括号
        if right < n and left > right:
            # 拼接上一个右括号，并且使用的右括号个数加 1
            self.dfs(curStr + ")", left, right + 1, n, res)


'''
class Solution {
    List<String> res = new ArrayList<>();
    public List<String> generateParenthesis(int n) {
        dfs(n, n, "");
        return res;
    }

    private void dfs(int left, int right, String curStr) {
        if (left == 0 && right == 0) { // 左右括号都不剩余了，递归终止
            res.add(curStr);
            return;
        }

        if (left > 0) { // 如果左括号还剩余的话，可以拼接左括号
            dfs(left - 1, right, curStr + "(");
        }
        if (right > left) { // 如果右括号剩余多于左括号剩余的话，可以拼接右括号
            dfs(left, right - 1, curStr + ")");
        }
    }
'''


# 做减法
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(res, n, n, '')
        return res

    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.dfs(res, left - 1, right, path + '(')
        if left < right:
            self.dfs(res, left, right - 1, path + ')')


from typing import List


# 做减法
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            """
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left: 左括号还可以使用的个数
            :param right: 右括号还可以使用的个数
            :return:
            """
            if left == 0 and right == 0:
                res.append(cur_str)
                return
            if right < left:
                return
            if left > 0:
                dfs(cur_str + '(', left - 1, right)
            if right > 0:
                dfs(cur_str + ')', left, right - 1)

        dfs(cur_str, n, n)
        return res


# 做加法
class Solution:
    def generateParenthesis(self, n: int):

        res = []
        cur_str = ''

        def dfs(cur_str, left, right, n):
            """
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left: 左括号已经使用的个数
            :param right: 右括号已经使用的个数
            :return:
            """
            if left == n and right == n:
                res.append(cur_str)
                return
            if left < right:
                return

            if left < n:
                dfs(cur_str + '(', left + 1, right, n)

            if right < n:
                dfs(cur_str + ')', left, right + 1, n)

        dfs(cur_str, 0, 0, n)
        return res


# 标准回溯模板
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        candidates = []
        res = []
        cur_str = ""
        for i in range(2 * n):
            if i < n:
                candidates.append("(")
            else:
                candidates.append(")")
        used = [False for _ in range(2 * n)]

        # 标准回溯模板
        def dfs(cur_str, used, left, right, n):
            if len(cur_str) == n:
                res.append(cur_str)
            for i in range(n):
                if not used[i]:
                    if i > 0 and used[i - 1] is False and candidates[i - 1] == candidates[i]:
                        continue
                    # 只要左边小于右边就剪枝
                    if left < right:
                        continue
                    used[i] = True
                    if candidates[i] == "(":
                        # left, right 用来记录当前的左右括号的个数
                        dfs(cur_str + candidates[i], used, left + 1, right, n)
                    else:
                        dfs(cur_str + candidates[i], used, left, right + 1, n)
                    used[i] = False

        dfs("", used, 0, 0, 2 * n)
        return res


'''
动态规划：
dp[i]表示i组括号的所有有效组合
dp[i] = "(dp[p]的所有有效组合)+【dp[q]的组合】"，其中 1 + p + q = i , p从0遍历到i-1, q则相应从i-1到0

'''

'''
首先，面向小白：什么是动态规划？在此题中，动态规划的思想类似于数学归纳法，当知道所有 i<n 的情况时，我们可以通过某种算法算出 i=n 的情况。
本题最核心的思想是，考虑 i=n 时相比 n-1 组括号增加的那一组括号的位置。

'''
'''
第 1 步：
    定义状态 dp[i]：使用 i 对括号能够生成的组合。
第 2 步：状态转移方程：
    i 对括号的一个组合，在 i - 1 对括号的基础上得到，这是思考 “状态转移方程” 的基础；
    i 对括号的一个组合，一定以左括号 "(" 开始，不一定以 ")" 结尾。为此，我们可以枚举新的右括号 ")" 可能所处的位置，得到所有的组合；
    枚举的方式就是枚举左括号 "(" 和右括号 ")" 中间可能的合法的括号对数，而剩下的合法的括号对数在与第一个左括号 "(" 配对的右括号 ")" 的后面，这就用到了以前的状态。
    状态转移方程是：
        dp[i] = "(" + dp[可能的括号对数] + ")" + dp[剩下的括号对数]
    整理得：
        dp[i] = "(" + dp[j] + ")" + dp[i- j - 1] , j = 0, 1, ..., i - 1
    
'''


# 动态规划
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n + 1)]  # dp[i]存放i组括号的所有有效组合
        dp[0] = [""]  # 初始化dp[0]
        for i in range(1, n + 1):  # 计算dp[i]
            for p in range(i):  # 遍历p
                l1 = dp[p]  # 得到dp[p]的所有有效组合
                l2 = dp[i - 1 - p]  # 得到dp[q]的所有有效组合
                for k1 in l1:
                    for k2 in l2:
                        dp[i].append("({0}){1}".format(k1, k2))

        return dp[n]


# 动态规划
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 动态规划
        if n == 0:
            return []
        # 使用 i 对括号能够生成的组合
        dp = [[] for i in range(n + 1)]
        dp[0] = [""]
        # 每遍历一次要添加一对括号
        for i in range(1, n + 1):
            for j in range(i):
                left = dp[j]
                right = dp[i - j - 1]
                # 两两拼接组合
                for s1 in left:
                    for s2 in right:
                        dp[i].append("(" + s1 + ")" + s2)
        return dp[n]