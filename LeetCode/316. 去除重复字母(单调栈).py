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

'''

from collections import Counter

# 单调栈
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set()
        # 这里先用一个hash记录所有元素的个数，后序hash需要动态变化
        hash = Counter(s)
        stack = []
        # 单调栈维护字典序
        for char in s:
            # 如果 char 在seen中，就需要删除掉当前元素, 如果没有使用过就需要维护一个单调栈，使用过了就不需要计算了
            if char not in seen:
                # 维护一个单调min栈, 如果hash表中的元素的个数大于0，代表可以被删除
                while stack and stack[-1] > char and hash[stack[-1]] > 0:
                    seen.remove(stack.pop())
                seen.add(char)
                stack.append(char)
            # 已经遍历过得元素就不再考虑了
            hash[char] -= 1
        return "".join(stack)
print(Solution().removeDuplicateLetters("bcacb"))

# go
'''
func removeDuplicateLetters(s string) string {
    left := [26]int{}
    for _, ch := range s {
        left[ch-'a']++
    }
    stack := []byte{}
    inStack := [26]bool{}
    for i := range s {
        ch := s[i]
        if !inStack[ch-'a'] {
            for len(stack) > 0 && ch < stack[len(stack)-1] {
                last := stack[len(stack)-1] - 'a'
                if left[last] == 0 {
                    break
                }
                stack = stack[:len(stack)-1]
                inStack[last] = false
            }
            stack = append(stack, ch)
            inStack[ch-'a'] = true
        }
        left[ch-'a']--
    }
    return string(stack)
}
'''


