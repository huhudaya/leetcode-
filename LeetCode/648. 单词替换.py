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

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/replace-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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


# 字典树
# 把所有的词根放入前缀树中，在树上查找每个单词的最短词根，该操作可在线性时间内完成。
# 时间复杂度：O(N)，其中 NN 是 sentence 的长度。每次查询操作为线性时间复杂度
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        d = {}  # 字典树初始化
        for word in dict:  # 把前缀词放进字典树
            t = d
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['end'] = True

        def f(word):  # 单词前缀判断
            t = d
            for i, c in enumerate(word):
                if 'end' in t:
                    return word[: i]  # 存在前缀就返回前缀
                elif c not in t:
                    break  # 不存在前缀就跳出循环并返回原词
                t = t[c]
            return word

        return ' '.join(map(f, sentence.split(' ')))


# 字典序
import collections


class Solution(object):
    def replaceWords(self, roots, sentence):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for root in roots:
            reduce(dict.__getitem__, root, trie)[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur: break
                cur = cur[letter]
            return cur.get(END, word)

        return " ".join(map(replace, sentence.split()))


class Solution:
    def replaceWords(self, dict, sentence: str) -> str:
        contain = collections.defaultdict(int)
        for dic in dict:
            contain[dic] = len(dic)
        result = sorted(contain.items(), key=lambda ky: (ky[1], ky[0]))
        words = sentence.split(" ")
        for i in range(len(words)):
            for sub_word, length in result:
                if sub_word == words[i][:length]:
                    words[i] = sub_word
                    break
        return " ".join(words)


class TrieNode:
    def __init__(self, val=None, isEnd=False):
        self.val = val
        self.isEnd = isEnd
        self.children = {}


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        # insert node to trie tree
        def insertWord(word):
            cur = root
            for w in word:
                if w not in cur.children:
                    cur.children[w] = TrieNode(w, False)
                cur = cur.children[w]
            cur.isEnd = True

        # find the word's replacement in the trie tree
        def find(word):
            cur = root
            # res用于保存前路径
            res = []
            for w in word:
                # 达到某个词根处，立即返回该词根
                if cur.isEnd:
                    return ''.join(res)
                # 未达到词根先出现tree之外的字符
                # 不进行替换
                if w not in cur.children:
                    return word
                # 记录到路径
                res.append(w)
                # 树继续往下走
                cur = cur.children[w]
            else:
                return ''.join(res)

        # Build Trie Tree
        root = TrieNode('')
        for word in dict:
            insertWord(word)
        # replace
        # 依次替换并返回
        words = sentence.split()
        res = []
        for word in words:
            res.append(find(word))
        return ' '.join(res)


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
