# 424. 替换后的最长重复字符.py
'''
给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符
总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。

注意:
字符串长度 和 k 不会超过 104。

示例 1:

输入:
s = "ABAB", k = 2

输出:
4

解释:
用两个'A'替换为两个'B',反之亦然。
示例 2:

输入:
s = "AABABBA", k = 1

输出:
4

解释:
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。

链接：https://leetcode-cn.com/problems/longest-repeating-character-replacement
'''



'''
问题在于怎么知道当前窗口中数量最多的字符的数量
因为需要替换的字符就是当前窗口的大小减去窗口中数量最多的字符的数量。
'''

'''
public int characterReplacement(String s, int k) {
    if (s == null || s.length() == 0) {
        return 0;
    }

    char[] sArr = s.toCharArray();

    int[] hash = new int[26];

    int l = 0, maxCount = 0, result = 0;
    for (int r = 0; r < sArr.length; ++r) {
        hash[sArr[r] - 'A']++;

        maxCount = Math.max(maxCount, hash[sArr[r] - 'A']);

        while (r - l + 1 - maxCount > k) {
            hash[sArr[l] - 'A']--;
            l++;
        }

        result = Math.max(r - l + 1, result);
    }

    return result;
}
'''
# 特殊情况 AABCD   K=1
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 滑动窗口
        if s is None or len(s) == 0:
            return 0
        hash = defaultdict(int)
        n = len(s)
        left = 0
        maxCount = 0
        res = 0
        for right in range(n):
            hash[s[right]] += 1
            # 当前窗口中元素最多的字符的数量
            maxCount = max(maxCount, hash[s[right]])
            # 注意这里为什么是while循环，举个特列 AABCD K=1,左指针必须移动到条件r-l+1不大于K
            # while right - left + 1 - maxCount > k:
            # 其实不用while，用 if 判断一下就可以了
            # if right - left + 1 - maxCount > k:
            while right - left + 1 - maxCount > k:
                hash[s[left]] -= 1
                left += 1
                # 这里按理也需要判断一下maxCount,为什么不判断了呢，相当于maxCount只大不小？
                # 这是由于我们只找满足条件的最大值，当大于maxcount的值出现，表示right-left+1的值更大!
            res = max(right - left + 1, res)
        return res
print(Solution().characterReplacement([1,1,1,0,0,0,1,1,1,1,0],2))