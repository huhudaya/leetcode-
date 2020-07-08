'''
在英语中，我们有一个叫做 词根(root)的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。
例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。

现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。
如果继承词有许多可以形成它的词根，则用最短的词根替换它。

你需要输出替换之后的句子。

示例：
输入：dict(词典) = ["cat", "bat", "rat"] sentence(句子) = "the cattle was rattled by the battery"
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
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        d = {}  # 字典树初始化
        for word in dict:  # 把前缀放进字典树
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
