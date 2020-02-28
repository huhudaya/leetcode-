'''

给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

# 注意是 1 到 N
# 和全排列问题一样，这是一道使用回溯算法解决的经典问题。
# 而分析回溯问题，我们常常需要画图来帮助我们理清思路和寻找边界条件。
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 特判
        if n <= 0 or k <= 0 or k > n:
            return []
        res = []
        self.__dfs(1, k, n, [], res)
        return res

    def __dfs(self, start, k, n, pre, res):
        if len(pre) == k:
            res.append(pre[:])
            return

        # 注意：这里 i 的上限是归纳得到的  剪枝
        for i in range(start, n - (k - len(pre)) + 2):
            pre.append(i)
            self.__dfs(i + 1, k, n, pre, res)
            pre.pop()


# 未优化版
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 先把不符合条件的情况去掉
        if n <= 0 or k <= 0 or k > n:
            return []
        res = []
        self.__dfs(1, k, n, [], res)
        return res

    def __dfs(self, start, k, n, pre, res):
        # 当前已经找到的组合存储在 pre 中，需要从 start 开始搜索新的元素
        # 在第 k 层结算
        if len(pre) == k:
            res.append(pre[:])
            return

        for i in range(start, n + 1):
            pre.append(i)
            # 因为已经把 i 加入到 pre 中，下一轮就从 i + 1 开始
            # 注意和全排列问题的区别，因为按顺序选择，因此无须使用 used 数组
            self.__dfs(i + 1, k, n, pre, res)
            # 回溯的时候，状态重置
            pre.pop()


# 自己的版本
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0 or n < k:
            return []
        res = []
        self._dfs(n, k, 0, [], res)
        return res

    def _dfs(self, n, k, start, path, res):
        # 递归结束条件
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(start, n):
            # 选择列表
            path.append(i + 1)
            # 从当前元素之后开始遍历，不包括当前元素
            self._dfs(n, k, i + 1, path, res)
            # 撤销选择
            path.pop()


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0 or n < k:
            return []
        res = []
        self._dfs(n, k, 0, [], res)
        return res

    def _dfs(self, n, k, start, path, res):
        # 递归结束条件
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(start, n - (k - len(path)) + 1):
            # 选择列表
            path.append(i + 1)
            # 从当前元素之后开始遍历，不包括当前元素
            self._dfs(n, k, i + 1, path, res)
            # 撤销选择
            path.pop()
'''
上面的代码中，我们发现：其实如果 pre 已经选择到 [1,4,5] 或者 [2,4,5] 或者 [3,4,5] ，后序的代码就没有必要执行，继续走也不能发现新的满足题意的组合。干了类似于下面事情，其实有很多步骤是多余的：选择了 [1,4,5] 以后， 5 弹出 [1,4,5] 成为 [1,4] , 4 弹出 [1,4] 成为 4 ，然后 5 进来，成为 [1,5]，在进来发现 for 循环都进不了（因为没有可选的元素），然后 5 又弹出，接着 1 弹出。

发现多余操作：那么我们如何发现多余的步骤呢，其实也是有规律可寻的，就在 for 循环中：

for (int i = start; i <= n; i++) {
    pre.add(i);
    generateCombinations(n, k, i + 1, pre);
    pre.remove(pre.size() - 1);
}
这个函数干的事情，是从 [i, n] 这个区间里（注意，左右都是闭区间），找到 k - pre.zize() 个元素。 i <= n 不是每一次都要走完的， i 有一个上限。

寻找规律：我们再看图，可以发现一些边界情况，帮助我们发现规律:

当选定了一个元素，即 pre.size() == 1 的时候，接下来要选择 2 个元素， i 最大的值是 4 ，因为从 5 开始选择，就无解了；
当选定了两个元素，即 pre.size() == 2 的时候，接下来要选择 1 个元素， i 最大的值是 5 ，因为从 6 开始选择，就无解了。

再如：如果 n = 6 ，k = 4，
pre.size() == 1 的时候，接下来要选择 3 个元素， i 最大的值是 4，最后一个被选的是 [4,5,6]；
pre.size() == 2 的时候，接下来要选择 2 个元素， i 最大的值是 5，最后一个被选的是 [5,6]；
pre.size() == 3 的时候，接下来要选择 1 个元素， i 最大的值是 6，最后一个被选的是 [6]；

再如：如果 n = 15 ，k = 4，
pre.size() == 1 的时候，接下来要选择 3 个元素，i 最大的值是 13，最后一个被选的是 [13,14,15]；
pre.size() == 2 的时候，接下来要选择 2 个元素， i 最大的值是 14，最后一个被选的是 [14,15]；
pre.size() == 3 的时候，接下来要选择 1 个元素， i 最大的值是 15，最后一个被选的是 [15]；

多写几遍（发现 max(i) 是我们倒着写出来），我么就可以发现 max(i) 与 接下来要选择的元素貌似有一点关系，很容易知道：
max(i) + 接下来要选择的元素个数 - 1 = n，其中， 接下来要选择的元素个数 = k - pre.size()，整理得到：

max(i) = n - (k - pre.size()) + 1
所以，我们的剪枝过程就是：把 i <= n 改成 i <= n - (k - pre.size()) + 1 ：

'''