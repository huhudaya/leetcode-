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

说明:

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
比较容易想到的是，使用同「力扣」第 46 题： “全排列” 
即使用回溯搜索的思想，依次得到全排列，输出所求的第 k 个全排列即可。
但事实上，我们不必求出所有的全排列。基于以下几点考虑：

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
# 总体思路，在子树中吗？不在就到下一个子树去判断
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def dfs(n, k, index, path):
            # 这里的index为当前的层数，当层数为n,则return
            if index == n:
                return
            # 这里和字典序的思想一样，计算step步长！
            # 这里是根据层数计算当前节点下有多少个节点，n-层数算有几种组合
            cnt = factorial[n - 1 - index]
            # 这个for循环用来判断是不是在当前子树中，如果在当前子树中，就要进入递归判断是当前子树中的哪一层
            for i in range(1, n + 1):
                if used[i]:
                    continue
                # 注意这里的剪枝，如果step小于k,说明不在这个子树中，这样就不会进入到后面的path.append和used[i]=True
                if cnt < k:
                    # 注意，这里我们将 k 减少了，说明不在这个子树中，需要剪枝
                    k -= cnt
                    continue
                # 如果走到这里，说明结果一定是在当前节点的子树中，这样就进入到递归去查找
                path.append(i)
                # 注意，这里只需要标记就可以
                used[i] = True
                # 如果执行到这里，说明一定在当前的子树下，所以需要index+1,表示第几层！
                # 注意，这里的dfs中的index只是为了计算当前的层次！！！！！！！！
                dfs(n, k, index + 1, path)

        if n == 0:
            return ""
        used = [False for _ in range(n + 1)]
        path = []
        factorial = [1 for _ in range(n + 1)]
        # 计算1-n的阶乘然后用一个列表保存
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i
        dfs(n, k, 0, path)
        return ''.join([str(num) for num in path])


print(Solution().getPermutation(1, 1))


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from itertools import permutations
        # 构造[1,2,3,4....n]
        list_n = list(range(n+1))
        list_n.pop(0)
        #构造全排列list
        arr = list(permutations(list_n))
        #返回第k个
        return ''.join(map(str, list(arr[k-1])))



class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        path = []
        n = 1
        def dfs(depth, path, k):
            if depth == n:
                return
            cnt = factorial[n - depth - 1]
            for i in range(1, n + 1):
                if used[i] is False:
                    # 不在当前子树中
                    if cnt < k:
                        k -= cnt
                        continue
                    # 否则在当前子树中
                    path.append(i)
                    used[i] = True
                    dfs(depth + 1, path, k)
        if n == 0:
            return ""
        used = [False for _ in range(n + 1)]
        path = []
        factorial = [1 for _ in range(n + 1)]
        # 计算1-n的阶乘然后用一个列表保存
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i
        dfs(0, path, k)
        return ''.join([str(num) for num in path])