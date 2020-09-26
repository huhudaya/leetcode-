'''
给定一个整数 n, 返回从 1 到 n 的字典顺序。

例如，

给定 n =1 3，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9] 。

请尽可能的优化算法的时间复杂度和空间复杂度。 输入的数据 n 小于等于 5,000,000。
'''
from typing import List

# 总体思路，构建将1-9开头的不大于N的树，最后先序返回,其实就是N叉树的先序遍历，在遍历过程中记录节点
'''
时间复杂度: O(N)，使用了递归，时间复杂度为进入递归函数的次数，我们遍历了每一个结点，所以时间复杂度是O(N)。
空间复杂度: O(1)
'''


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        """2020-04-27 字典序排数"""
        if n < 1:
            return []
        res = []

        def dfs(cur):
            if cur > n:
                return
            # 其实这样就相当于先序遍历
            res.append(cur)
            # N叉树遍历
            for j in range(10):  # 遍历0 ~ 9
                dfs(cur * 10 + j)

        # N叉树遍历
        for i in range(1, 10):  # 遍历1 ~ 9
            dfs(i)
        return res


# 复杂版本
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(cur, n, res):  # cur为根结点
            if cur > n:
                return
            else:
                res.append(cur)
                for i in range(10):
                    if 10 * cur + i > n:  # 比如叶子结点为14，而n是13，dfs就结束了
                        return
                    dfs(10 * cur + i, n, res)

        res = []
        # 对每棵树进行dfs
        for i in range(1, 10):
            dfs(i, n, res)
        return res


# java
'''
class Solution {
    ArrayList<Integer> res = new ArrayList<>();
    public List<Integer> lexicalOrder(int n) {
        for (int i = 1; i < 10; i ++){
            dfs(n, i);
        }
        return res;
    }
    private void dfs(int n, int cur){
        if (cur > n) return;
        res.add(cur);
        for (int i = 0; i < 10; i ++) {
            dfs(n, cur * 10 + i);
        }
    }
}
'''