'''
给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。
回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。
回文串不一定是字典当中的单词。

示例1：

输入："tactcoa"
输出：true（排列有"tacocat"、"atcocta"，等等）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-permutation-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from collections import defaultdict


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # 只有一次机会为奇数
        n = len(s)
        hash = defaultdict(int)
        for i in range(n):
            hash[s[i]] += 1
        cnt = 0
        for val in hash.values():
            if val & 1:
                cnt += 1
            if cnt > 1:
                return False
        return True
