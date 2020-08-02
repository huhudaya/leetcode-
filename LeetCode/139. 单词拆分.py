'''
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
'''
from typing import List
from collections import deque


# DFS
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = [None] * len(s)

        # 以索引i为起始到末尾的字符串能否由字典组成
        def dfs(i):
            # 长度超过s,返回True(空字符能组成)
            if i >= len(s):
                return True
            # 存在以i为起始的递归结果
            if memo[i] != None:
                return memo[i]
            # 递归
            for j in range(i, len(s)):
                if s[i:j + 1] in wordDict and dfs(j + 1):
                    # 在返回值之前结果必须先放入memo中
                    memo[i] = True
                    return True
            # 在返回值之前结果必须先放入memo中
            memo[i] = False
            return False

        return dfs(0)



'''
用BFS遍历节点。维护一个队列，依然用 start 指针代表节点的状态
如下图例子，起初队列推入 0，让它出列，考察指针 1,2,3,4,5,6,7,8
它们分别与指针 0 形成的前缀子串，如果不是单词表的单词，对应的指针就不能入列，否则可以入列
指针出列，考察它的子节点，能入列的就入列、再出列……重复
直到指针越过 s 串边界，并且形成的子串是单词表里的单词，返回 true
或者遍历结束都没有返回 true ，返回 false
'''
# BFS
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        visited = [False] * len(s)
        q = deque()
        q.append(0)

        while q:
            i = q.popleft()
            # 节点若访问则跳过
            if visited[i]:
                continue
            else:
                visited[i] = True
            # 扫描从索引i开始的字符串
            for j in range(i, len(s)):
                # 子字符串在字典中
                if s[i:j + 1] in wordDict:
                    # 并且到达结尾，返回True
                    if j == len(s) - 1:
                        return True
                    # 未到达结尾，则添加j+1起始索引到队列
                    else:
                        q.append(j + 1)

        return False


# 动态规划
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 动态规划
        # 前n个字符是否能由字典组成
        n = len(s)
        dp = [False] * (n + 1)
        # 初始状态
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i, -1, -1):
                # 转移公式
                # 倒序遍历，如果满足条件就提前剪枝
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]