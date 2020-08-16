'''

给你一个仅包含小写字母的字符串，请你去除字符串中重复的字母，使得每个字母只出现一次
需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）

示例 1:
输入: "bcabc"
输出: "abc"

示例 2:
输入: "cbacdcbc"
输出: "acdb"

注意：该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters 相同

通过次数17,465提交次数43,386
'''

from collections import Counter

# 单调栈
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        seen = set()
        hash = Counter(s)
        stack = []
        # 单调栈维护字典序
        for char in s:
            # 如果 char 在senn中，就需要删除掉当前元素
            if char not in seen:
                # 维护一个单调min栈, 如果hash表中的元素的个数大于0，代表可以被删除
                while stack and stack[-1] > char and hash[stack[-1]] > 0:
                    seen.remove(stack.pop())
                seen.add(char)
                stack.append(char)
            # 已经遍历过得元素就不再考虑了
            hash[char] -= 1
        return "".join(stack)


Solution().removeDuplicateLetters("bcabc")
