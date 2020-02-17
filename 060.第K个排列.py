'''
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"

链接：https://leetcode-cn.com/problems/permutation-sequence
'''


'''
比较容易想到的是，使用同「力扣」第 46 题： “全排列” ，即使用回溯搜索的思想，依次得到全排列，输出所求的第 k 个全排列即可。但事实上，我们不必求出所有的全排列。基于以下几点考虑：

1、我们知道所求排列一定在叶子结点处得到。
事实上，进入每一个分支的时候，我们都可以通过递归的层数，直接计算这一分支可以得到的叶子结点的个数；

这是因为：进入一个分支的时候，我们可以根据已经选定的数的个数
进而确定还未选定的数的个数，然后计算阶乘，就知道这一个分支的叶子结点有多少个。

2、如果 k 大于这一个分支将要产生的叶子结点数，直接跳过这个分支，这个操作叫“剪枝”；

3、如果 k 小于等于这一个分支将要产生的叶子结点数，
那说明所求的全排列一定在这一个分支将要产生的叶子结点里，需要递归求解；

4、计算阶乘的时候，你可以使用循环计算，特别注意：0!=1
它表示了没有数可选的时候，即表示到达叶子结点了，排列数只剩下 1 个；

又因为题目中说“给定 n 的范围是 [1,9]”，故可以实现把从 0 到 9 的阶乘计算好，
在一个数组里，可以根据索引直接获得阶乘值

下面以示例 2：输入: n = 4,k=9，介绍如何使用“回溯 + 剪枝” 的思想得到输出 "2314"。
'''


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def dfs(n, k, index, path):
            if index == n:
                return
            cnt = factorial[n - 1 - index]
            for i in range(1, n + 1):
                if used[i]:
                    continue
                if cnt < k:
                    k -= cnt
                    continue
                path.append(i)
                used[i] = True
                dfs(n, k, index + 1, path)
        if n == 0:
            return ""
        used = [False for _ in range(n + 1)]
        path = []
        factorial = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i
        dfs(n, k, 0, path)
        return ''.join([str(num) for num in path])


print(Solution().getPermutation(1,1))