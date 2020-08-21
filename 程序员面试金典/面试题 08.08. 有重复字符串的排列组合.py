'''

有重复字符串的排列组合。
编写一种方法，计算某字符串的所有排列组合。

示例1:

 输入：S = "qqe"
 输出：["eqq","qeq","qqe"]
示例2:

 输入：S = "ab"
 输出：["ab", "ba"]
提示:

'''
from typing import List


class Solution:
    def permutation(self, S: str) -> List[str]:
        S = "".join(sorted(list(S)))
        res = []
        n = len(S)
        used = [False for i in range(n)]

        def dfs(path, depth):
            if depth == n:
                res.append(path[:])
            for i in range(n):
                # 小剪枝
                if used[i] == True:
                    continue
                if i > 0 and S[i] == S[i - 1] and used[i - 1] == False:
                    continue
                used[i] = True
                dfs(path + S[i], depth + 1)
                used[i] = False

        dfs("", 0)
        return res
