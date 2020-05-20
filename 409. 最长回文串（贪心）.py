'''

给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
注意:
假设字符串的长度不会超过 1010。
示例 1:
输入:
"abccccdd"
输出:
7
解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
'''

# 贪心 核心思路，只选一个作为中心元素
from collections import Counter
from collections import defaultdict

a = defaultdict(int)
print(a)


class Solution:
    def longestPalindrome(self, s):
        ans = 0
        count = Counter(s)
        for v in count.values():
            ans += v // 2 * 2
            # 保证只有一个中心元素，这里保证只有一个中心元素
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans


# 自己的版本
from collections import defaultdict


class Solution1:
    def longestPalindrome(self, s: str) -> int:
        hash = defaultdict(int)
        res = 0
        for i in s:
            hash[i] += 1
        print(hash)
        for i in hash.values():
            res += i // 2 * 2
            # if res % 2 == 0 and i % 2 == 1:
            # 保证只有一个中心点
            if res & 1 == 0 and i & 1 == 1:
                res += 1
        return res


class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash = defaultdict(int)
        res = 0
        for i in s:
            hash[i] += 1
        flag = False
        for i in hash.values():
            res += i // 2 * 2
            # if res % 2 == 0 and i % 2 == 1:
            # 保证只有一个中心点
            if not flag and i & 1 == 1:
                res += 1
                flag = True
        return res
