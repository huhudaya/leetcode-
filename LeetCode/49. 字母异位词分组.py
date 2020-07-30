'''
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
通过次数90,349提交次数143,95
'''
from typing import List
# 核心思路。将每个子串排序然后和hash对比
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        n = len(strs)
        # hash
        hash = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in hash:
                # 如果不在，则key对应的value添加一个列表
                hash[key] = [s]
            else:
                hash[key].append(s)
        return list(hash.values())