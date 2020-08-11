'''
给你一个由大小写英文字母组成的字符串 s 。
一个整理好的字符串中，两个相邻字符 s[i] 和 s[i + 1] 不会同时满足下述条件：
0 <= i <= s.length - 2
s[i] 是小写字符，但 s[i + 1] 是相同的大写字符；反之亦然 。
请你将字符串整理好，每次你都可以从字符串中选出满足上述条件的 两个相邻 字符并删除，直到字符串整理好为止。
请返回整理好的 字符串 。题目保证在给出的约束条件下，测试样例对应的答案是唯一的。
注意：空字符串也属于整理好的字符串，尽管其中没有任何字符。

示例 1：

输入：s = "leEeetcode"
输出："leetcode"
解释：无论你第一次选的是 i = 1 还是 i = 2，都会使 "leEeetcode" 缩减为 "leetcode" 。

示例 2：
输入：s = "abBAcC"
输出：""
解释：存在多种不同情况，但所有的情况都会导致相同的结果。例如：
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

示例 3：
输入：s = "s"
输出："s"
提示：
1 <= s.length <= 100
s 只包含小写和大写英文字母
'''


# 回溯
class Solution:
    def makeGood(self, s: str) -> str:
        self.aA = abs(ord('a') - ord('A'))
        return self._makeGood(s, 0)

    def _makeGood(self, s, i):
        if i > len(s) - 2:
            return s
        if abs(ord(s[i]) - ord(s[i + 1])) == self.aA:
            s = s[:i] + s[i + 2:]
            i = max(0, i - 2)
        else:
            i += 1
        return self._makeGood(s, i)


class Solution:
    def makeGood(self, s: str) -> str:
        while s:
            t = s
            for i in range(len(s) - 1):
                if s[i].islower() ^ s[i + 1].islower() and s[i].lower() == s[i + 1].lower():
                    s = s[:i] + s[i + 2:]
                    break
            if t == s:
                break
        return s
# 栈
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if (c.islower() and c.upper() == stack[-1]) or (c.isupper() and c.lower() == stack[-1]):
                    stack.pop()
                else:
                    stack.append(c)
        return ''.join(stack)

# Java
'''
class Solution {
public:
    string makeGood(string s) {
        string ans;
        for(auto x : s){
            if(ans.size() && (abs(x-ans.back())==('a' - 'A'))){
                ans.pop_back();
                continue;
            }
            ans.push_back(x);
        }
        return ans;
    }
};
'''