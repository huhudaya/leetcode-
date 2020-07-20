'''

设计一个支持以下两种操作的数据结构：

void addWord(word)
bool search(word)
search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。

示例:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
说明:

你可以假设所有单词都是由小写字母 a-z 组成的。
'''
# 自己的版本
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        p = self.root
        for i in word:
            if i not in p:
                p[i] = {}
            p = p[i]
        p["end"] = "end"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        flag = False
        p = self.root
        for i, w in enumerate(word):
            if w == ".":
                for j in p:
                    flag = self.search(word[:i] + j + word[i + 1:]) or flag
                return flag
            elif w not in p:
                return False
            p = p[w]
        if "end" in p:
            return True
        else:
            return False
