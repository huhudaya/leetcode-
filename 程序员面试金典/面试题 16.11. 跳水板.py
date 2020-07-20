'''

你正在使用一堆木板建造跳水板。
有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。
你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。

返回的长度需要从小到大排列。

示例：

输入：
shorter = 1
longer = 2
k = 3
输出： {3,4,5,6}
提示：

0 < shorter <= longer
0 <= k <= 100000
'''
# 这个方法不对，不用看 回溯法，超时
from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        # 要求具体的组合，所以一帮用回溯
        candidates = [shorter, longer]
        res = set()
        if k == 0:
            return []

        def dfs(start, path, target):
            if target == 0:
                res.add(len(path))
            for i in range(start, 2):
                # 大剪枝
                if target < candidates[i]:
                    break
                path.append(i)
                dfs(start, path, target - candidates[i])
                path.pop()

        dfs(0, [], k)
        return list(res)


# 两种板子，板子A，板子B，在k块中，板子B的个数从0-k逐渐增加，即0,1,2,3,4,5...k，共k+1。
# 数学法
'''
class Solution {
    public int[] divingBoard(int shorter, int longer, int k) {
        if (k == 0) {
            return new int[0];
        }
        if (shorter == longer) {
            return new int[]{shorter * k};
        }
        int[] lengths = new int[k + 1];
        for (int i = 0; i <= k; i++) {
            lengths[i] = shorter * (k - i) + longer * i;
        }
        return lengths;
    }
}
'''


# 核心思路，构建一个等差数列的列表
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if shorter == longer:
            return [shorter * k]
        delta = longer - shorter
        return [k * shorter + delta * i for i in range(k + 1)]


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if longer == shorter:
            return [k * longer]
        return list(range(shorter * k, longer * k + 1, (longer - shorter)))

# 自己的版本
# 核心思路，从全是短木板开始一块一块的替换为长模板，构成公差为两个木板的差的一个等差数列
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        # 核心思路
        # 先考虑k为0的情况，并且考虑两个木板长度相同的情况
        # 对全部由最短的木板组成的组合依次替换为长木板
        if k == 0:
            return []
        if shorter == longer:
            return [shorter * k]
        # 构建等差数列
        delta = longer - shorter
        # 可以换k次，加上全是最短的模板的组合，总共有k+1个组合
        return [shorter * k + delta * i for i in range(k + 1)]