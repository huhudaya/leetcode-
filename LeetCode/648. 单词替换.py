'''
在英语中，我们有一个叫做 词根(root)的概念，
它可以跟着其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。
例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。

现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。
如果继承词有许多可以形成它的词根，则用最短的词根替换它。

你需要输出替换之后的句子。

示例：
输入：dict(词典) = ["cat", "bat", "rat"]
     sentence(句子) = "the cattle was rattled by the battery"
输出："the cat was rat by the bat"

提示：

输入只包含小写字母。
1 <= dict.length <= 1000
1 <= dict[i].length <= 100
1 <= 句中词语数 <= 1000
1 <= 句中词语长度 <= 1000
'''
# 前缀函数
from typing import List


# 暴力方法
# O(∑w2）其中 wi是第 i 个单词的长度。检查第 i 个单词的所有前缀花费时间 O(wi^2)
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        dict.sort()
        s = sentence.split(' ')
        for i, word in enumerate(s):
            for j in dict:
                if word.startswith(j):
                    s[i] = j
                    break
        return ' '.join(s)


# 简洁版本（模板）
class TrieNode():
    def __init__(self):  # 不要漏写了 self,否则显示少一个参数
        self.isEnd = False
        self.val = {}


class Trie():
    def __init__(self):
        self.root = TrieNode()  # 这里不是 {}

    def prefix(self, word):  # 返回存在的前缀
        p = self.root
        ans = ""
        for x in word:
            ans += x
            if x not in p.val:
                return word
            else:
                p = p.val[x]
                if p.isEnd == True:
                    return ans
        return word

    def insert(self, word):
        p = self.root
        for x in word:
            if x not in p.val:
                p.val[x] = TrieNode()
            p = p.val[x]
        p.isEnd = True


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        trie = Trie()
        for x in dict:
            trie.insert(x)
        ans = []
        for x in sentence.split():
            ans.append(trie.prefix(x))
        return " ".join(x for x in ans)


# 自己的版本
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        root = {}

        # 字典树
        def insert(root, word):
            tmp = root
            for i in word:
                if i not in tmp:
                    tmp[i] = {}
                tmp = tmp[i]
            tmp["end"] = "end"

        def find(root, word):
            p = root
            res = ""
            for i in word:
                res += i
                if i not in p:
                    return word
                else:
                    p = p[i]
                    # 只要第一次符合要求，即最短的词根，立即返回
                    if "end" in p:
                        return res
            return word

        for x in dict:
            insert(root, x)
        res = []
        for i in sentence.split():
            res.append(find(root, i))
        return " ".join(res)
