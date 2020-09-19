'''
给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。
返回所有可能得到的字符串集合。

示例：
输入：S = "a1b2"
输出：["a1b2", "a1B2", "A1b2", "A1B2"]

输入：S = "3z4"
输出：["3z4", "3Z4"]
输入：S = "12345"
输出：["12345"]

提示：
S 的长度不超过12。
S 仅由数字和字母组成。
'''

import itertools


class Solution(object):
    def letterCasePermutation(self, S):
        f = lambda x: (x.lower(), x.upper()) if x.isalpha() else x
        return map("".join, itertools.product(*map(f, S)))


# 二分掩码
'''
思路
假设字符串 S 有 BB 个字母，那么全排列就有 2^B2 
B
  个字符串，且可以用位掩码 bits 唯一地表示。
例如，可以用 00 表示 a7b， 01 表示 a7B， 10 表示 A7b， 11 表示 A7B。注意数字不是掩码的一部分。
算法
根据位掩码，构造正确的全排列结果。如果下一个字符是字母，则根据位掩码添加小写或大写字母。 否则添加对应的数字。
'''


class Solution(object):
    def letterCasePermutation(self, S):
        B = sum(letter.isalpha() for letter in S)
        ans = []

        for bits in range(1 << B):
            b = 0
            word = []
            for letter in S:
                if letter.isalpha():
                    if (bits >> b) & 1:
                        word.append(letter.lower())
                    else:
                        word.append(letter.upper())

                    b += 1
                else:
                    word.append(letter)

            ans.append("".join(word))
        return ans


'''
既然数字涉及不到分支，遇到它的时候，不妨继续往后搜，因此对于一个数字只需搜 1 次
但对于单个字母来说，我们需要搜 2 次：小写的时候搜一次，大写的时候再搜一次
再具体一点：遇到数字直接 index + 1 继续递归
遇到字母则连续递归 2 次，即当字母为小写的时候递归一次(index+1)
然后回溯时将字母转为大写，又去递归一次
'''


class Solution(object):
    def letterCasePermutation(self, S):
        ans = [[]]

        for char in S:
            n = len(ans)
            if char.isalpha():
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(char.lower())
                    ans[n + i].append(char.upper())
            else:
                for i in range(n):
                    ans[i].append(char)

        return map("".join, ans)


# java
'''
class Solution {
    public static void dfs(StringBuilder s, int index, List<String> res) {
		if(index >= s.length()) {
			res.add(s.toString());
			return; 
		}
		char ch = s.charAt(index);
		if(ch >= 65 && ch <= 90 || ch >= 97 && ch <= 122) {
			dfs(s, index+1, res);					// 搜索原字母的组合
			s.setCharAt(index, (char)(ch ^ 32));
			dfs(s, index+1, res);					// 搜索转换字母大小写后的组合
		} else dfs(s, index+1, res);				// 该位为数字，直接往后搜
	}
	
	public static List<String> letterCasePermutation(String S) {
		List<String> res = new ArrayList<String>();
		dfs(new StringBuilder(S), 0, res);
		return res;
	}
}
'''

# 自己的版本
from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        n = len(S)
        res = []

        # 注意，这道题的顺序是固定的
        def dfs(start, s):
            if start == n:
                res.append(s)
                return
            # 如果是字母就dfs两次
            if s[start].isalpha():
                # print(s[start].lower(), s[start])
                dfs(start + 1, s[:start] + s[start].lower() + s[start + 1:])
                dfs(start + 1, s[:start] + s[start].upper() + s[start + 1:])
            else:
                dfs(start + 1, s)

        dfs(0, S)
        return res
