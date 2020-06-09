# 014.最长公共前缀.py
'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
链接：https://leetcode-cn.com/problems/longest-common-prefix
'''



'''
a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)     # 打包为元组的列表
[(1, 4), (2, 5), (3, 6)]
zip(a,c)              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
[(1, 2, 3), (4, 5, 6)]

nums = ['flower','flow','flight']
for i in zip(*nums):
    print(i)

输出结果：
('f', 'f', 'f')
('l', 'l', 'l')
('o', 'o', 'i')
('w', 'w', 'g')

'''

# 利用解包
class Solution:
    def longestCommonPrefix(self, strs) -> str:     
        s = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                s += i[0]
            else:
                break           
        return s    
# 利用 try-catch
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        i = 0
        try:
            while(1):
                c_set = set()
                for s in strs:
                    c_set.add(s[i])
                    if(len(c_set) > 1):
                        return res
                res += strs[0][i]
                i += 1
        except BaseException:
            return res


# 水平扫描法(前缀减少法)  O(S) S是所有字符串的字符数量之和
# 最坏的情况下，n 个字符串都是相同的。算法会将 S1 与其他字符串 [S_2...S_n]都做一次比较。
# 这样就会进行 S 次字符比较，其中 S 是输入数据中所有字符数量
# 空间复杂度：O(1)，我们只需要使用常数级别的额外空间
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        prefix = strs[0]  # 从第1个字符串开始
        for i in range(len(strs)):
            # 不是其他字符串的前缀，则为-1，如果是前缀则是匹配的第一个index即0
            # 水平扫描，当i等于1的时候，这个时候得到的prefix是i=0和i=1的公共前缀，如果find的值是0，说明有公共前缀，否则while中prefix一直减小
            while(strs[i].find(prefix) != 0):
                # prefix = prefix[0: len(prefix)-1]  # 减少前缀
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

# 自己的版本。。。。感觉好乱
import sys
class Solution:
    def longestCommonPrefix(self, strs):
        n = len(strs)
        index = 0
        min_len = sys.maxsize
        if n == 0:
            return ""
        if n == 1:
            return strs[0]
        for i in range(len(strs)):
            min_len = min(min_len, len(strs[i]))
        if min_len == 0:
            return ""
        for index in range(min_len):
            for i in range(1, n):
                if ord(strs[0][index]) ^ ord(strs[i][index]) != 0:
                    return strs[0][0:index]
        return strs[0][0:min_len]




a = ["adf","dadf","adf"]
# print(list(zip(*a)))
a = "asdaf"

print(a[:-1])