'''
无重复字符串的排列组合。
编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。
示例1:

 输入：S = "qwe"
 输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]
示例2:

 输入：S = "ab"
 输出：["ab", "ba"]
提示:

字符都是英文字母。
字符串长度在[1, 9]之间。
'''
from typing import List
class Solution:
    def permutation(self, S: str) -> List[str]:
        n = len(S)
        res = []
        def dfs(path, depath):
            if depath == n:
                res.append(path[:])
            for i in range(n):
                if S[i] in path:
                    continue
                dfs(path + S[i], depath + 1)
        dfs("", 0)
        return res