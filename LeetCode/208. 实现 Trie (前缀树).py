'''

实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true
说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。
'''


class Node:
    def __init__(self):
        # 每个节点拥有一个列表用来保存这个节点可能指向的26个字母
        self.child = [None for _ in range(26)]
        # isEnd标志位用来标记当前位置是否是一个单词的尾部
        self.isEnd = False

    def contain_key(self, ch):
        return self.child[ord(ch) - ord('a')]

    def get(self, ch):
        return self.child[ord(ch) - ord('a')]

    def put(self, ch):
        self.child[ord(ch) - ord('a')] = Node()




# 字典树的构建方式也很简单，就是嵌套哈希表。
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    '''
    描述：向 Trie 中插入一个单词 word
    实现：这个操作和构建链表很像。首先从根结点的子结点开始与 word 第一个字符进行匹配
         一直匹配到前缀链上没有对应的字符，这时开始不断开辟新的结点，直到插入完 word 的最后一个字符
         同时还要将最后一个结点isEnd = true;，表示它是一个单词的末尾
    '''

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        for i in word:
            if not p.contain_key(i):
                p.put(i)
            # 注意，每轮循环，p的值都发生了变化
            p = p.get(i)
        p.isEnd = True

    '''
    描述：查找 Trie 中是否存在单词 word

    实现：从根结点的子结点开始，一直向下匹配即可，如果出现结点值为空就返回false，如果匹配到了最后一个字符，那我们只需判断node->isEnd即可。
    '''

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self.root
        for i in word:
            if not p.contain_key(i):
                return False
            else:
                p = p.get(i)
        return p.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.root
        for i in prefix:
            if not p.contain_key(i):
                return False
            else:
                p = p.get(i)
        return True


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                tree[a] = {}
            tree = tree[a]
        # 单词结束标志
        tree["#"] = "#"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                return False
            tree = tree[a]
        if "#" in tree:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.lookup
        for a in prefix:
            if a not in tree:
                return False
            tree = tree[a]
        return True

# 自己的版本
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 用字典中的k-v模拟树的父子节点
        # 用hash存储！相当于根节点
        self.lookup = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                # 相当于创建一个新的map
                tree[a] = {}
            tree = tree[a]
        # 特别注意，树的最后的叶子节点是一个{}
        # 添加一个单词的结束标志
        tree["end"] = "end"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                return False
            tree = tree[a]
        if "end" in tree:
            return True
        else:
            return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.lookup
        for a in prefix:
            if a not in tree:
                return False
            tree = tree[a]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)