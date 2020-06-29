# 032最长有效括号.py
'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
'''
'''
看了这个题目的标签，动态规划是其的标签之一。这题目我第一反应可以使用栈来解决，但我们偏用动态规划看看解决的是什么样子的。

我们定义一个dp[i]数组，其中i表示字符串的下标，值是目前有效的子字符串。

我们将dp数组全部初始化为0。

 现在，很明显有效的子字符串一定以‘)’结尾。

 我们可以进一步得出结论：以‘(’的子字符串对应位置上的值必定为0。

 所以说我们只需要更新‘)’在dp数组中对应位置的值。

为了求出dp数组，我们每两个字符检查一次，如果满足如下条件

 s[i]=‘)’且s[i−1]=‘(’，形如‘‘…()..."，可以推出：dp[i]=dp[i−2]+2

 可以进行这样的转移，是因为结束部分的"()"是一个有效子字符串，并且将之前有效子字符串的长度增加了2。

 s[i]=‘)’且s[i−1]=‘)’，也就是字符串形如‘‘...))..."，我们可以推出：

如果s[i−dp[i−1]−1]=‘(’，则dp[i]=dp[i−1]+dp[i−dp[i−1]−2]+2

这背后的原因是如果倒数第二个‘)’是一个有效子字符串的一部分（记为s），对于最后一个‘)’，如果它是一个更长子字符串的一部分，那么它一定有一个对应的‘(’，它的位置在倒数第二个‘)’所在的有效子字符串(s)的前面。

 因此，如果子字符串s的前面恰好是‘(’，那么我们就用2加上s的长度（dp[i−1]）去更新dp[i]。

除此以外，我们也会把有效子字符串‘‘(,s,)"之前的有效子字符串的长度也加上，dp[i−dp[i−1]−2]。
'''
# 暴力法 java 
'''
public class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push('(');
            } else if (!stack.empty() && stack.peek() == '(') {
                stack.pop();
            } else {
                return false;
            }
        }
        return stack.empty();
    }
    public int longestValidParentheses(String s) {
        int maxlen = 0;
        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 2; j <= s.length(); j+=2) {
                if (isValid(s.substring(i, j))) {
                    maxlen = Math.max(maxlen, j - i);
                }
            }
        }
        return maxlen;
    }
}
'''

'''
时间复杂度： O(n) 遍历整个字符串一次，就可以将 dpdp 数组求出来
空间复杂度： O(n) 需要一个大小为 nn 的 dpdp 数组
'''


# 动态规划
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # dp
        dp = [0 for i in range(len(s))]
        if len(s) == 0:
            return 0
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i - 1] == "(":
                    if i >= 2:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                    if i - dp[i - 1] >= 2:
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                    else:
                        dp[i] = dp[i - 1] + 2
        return max(dp)


# 用栈
'''
与找到每个可能的子字符串后再判断它的有效性不同，我们可以用栈在遍历给定字符串的过程中去判断到目前为止扫描的子字符串的有效性，同时能的都最长有效字符串的长度。我们首先将 -1−1 放入栈顶。

对于遇到的每个"(",我们将它的下标放入栈中
对于遇到的每个")",我们弹出栈顶的元素并将当前元素的下标与弹出元素下标作差，得出当前有效括号字符串的长度。
通过这种方法，我们继续计算有效子字符串的长度，并最终返回最长有效子字符串的长度

'''
'''
public class Solution {

    public int longestValidParentheses(String s) {
        int maxans = 0;
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {
                stack.pop();
                if (stack.empty()) {
                    stack.push(i);
                } else {
                    maxans = Math.max(maxans, i - stack.peek());
                }
            }
        }
        return maxans;
    }
}
'''

