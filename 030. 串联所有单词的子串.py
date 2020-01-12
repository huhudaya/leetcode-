# 030. 串联所有单词的子串.py
'''
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

 

示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]

链接：https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words
'''

# 这里有两个注意的地方，words中的单词都是长度相同的，不需要考虑words中的顺序


# 每次从 s 截取一定长度（固定）的字符串，看这段字符串出现单词个数是否和要匹配的单词个数相等!如下代码：
class Solution:
    def findSubstring(self, s: str, words):
        from collections import Counter
        if not s or not words:return []
        # 得到 words中所有单词的总长度
        all_len = sum(map(len, words))
        n = len(s)
        # 得到一个字典，counter进行计数{"a":2,"b":1}
        words = Counter(words)
        res = []
        # 每次截取固定的长度
        for i in range(0, n - all_len + 1):
            tmp = s[i:i+all_len]
            flag = True
            for key in words:
                if words[key] != tmp.count(key):
                    flag = False
                    break
            if flag:res.append(i)
        return res


'''
因为单词长度固定的，我们可以计算出截取字符串的单词个数是否和 words 里相等，所以我们可以借用哈希表。

一个是哈希表是 words，一个哈希表是截取的字符串，比较两个哈希是否相等！

因为遍历和比较都是线性的，所以时间复杂度：O(n^2)
'''
# O(N^2)(两个hash表)
# 我自己的版本
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # 用hash
        from collections import Counter
        if not s or not words:
            return []
        one_word = len(words[0])
        all_len = one_word * len(words)
        n = len(s)
        # hash key是words中的字符串，value是出现的个数
        words = Counter(words)
        # 记录索引
        res = []
        for i in range(0, n - all_len + 1):
            # 截取固定长度的字符串
            tmp = s[i : i+all_len]
            hash_tmp = []
            # 构建hash,这里利用counter构建hash字典
            for j in range(0, all_len, one_word):
                hash_tmp.append(tmp[j : j+one_word])
            if Counter(hash_tmp) == words:
                res.append(i)
        return res

# 优化---滑动窗口 时间复杂度O(N)
'''
滑动窗口！

我们一直在 s 维护着所有单词长度总和的一个长度队列！

时间复杂度：O(n)

还可以再优化，只是加一些判断，详细看代码吧！
'''

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        # 构建words的hash
        words = Counter(words)
        res = []
        # 这里有one_word种情况，总体来说时间复杂度是O(N)
        # 分one_word种情况的时候，每一个情况都按one_word_len的间隔,总体遍历了一次数组中的所有元素，别看while层数多。
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                cur_Counter[w] += 1
                cur_cnt += 1
                while cur_Counter[w] > words[w]:
                    left_w = s[left:left+one_word]
                    left += one_word
                    cur_Counter[left_w] -= 1
                    cur_cnt -= 1
                if cur_cnt == word_num :
                    res.append(left)
        return res

# 滑动窗口再优化
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        if n < one_word:return []
        words = Counter(words)
        res = []
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                if w not in words:
                    left = right
                    cur_Counter.clear()
                    cur_cnt = 0
                else:
                    cur_Counter[w] += 1
                    cur_cnt += 1
                    while cur_Counter[w] > words[w]:
                        left_w = s[left:left+one_word]
                        left += one_word
                        cur_Counter[left_w] -= 1
                        cur_cnt -= 1
                    if cur_cnt == word_num :
                        res.append(left)
        return res
# 两个hash
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        from collections import defaultdict
        res = []
        wordnum = len(words)
        if wordnum == 0:
            return res
        wordlen = len(words[0])
        allwords = dict(Counter(words))
        for i in range(len(s)-wordlen*wordnum+1):
            num = 0
            haswords = defaultdict(int)
            while num < wordnum:
                word = s[i+num*wordlen:i+(num+1)*wordlen]
                if word in allwords:
                    haswords[word] += 1
                    if haswords[word] > allwords[word]:
                        break
                else:
                    break
                num += 1
            if num == wordnum:
                res.append(i)
        return res



# java优化版本
'''
public List<Integer> findSubstring(String s, String[] words) {
    List<Integer> res = new ArrayList<Integer>();
    int wordNum = words.length;
    if (wordNum == 0) {
        return res;
    }
    int wordLen = words[0].length();
    HashMap<String, Integer> allWords = new HashMap<String, Integer>();
    for (String w : words) {
        int value = allWords.getOrDefault(w, 0);
        allWords.put(w, value + 1);
    }
    //将所有移动分成 wordlen 类情况
    for (int j = 0; j < wordLen; j++) {
        HashMap<String, Integer> hasWords = new HashMap<String, Integer>();
        int num = 0; //记录当前 HashMap2（这里的 hasWords 变量）中有多少个单词
		//每次移动一个单词长度
        for (int i = j; i < s.length() - wordNum * wordLen + 1; i = i + wordLen) {
            boolean hasRemoved = false; //防止情况三移除后，情况一继续移除
            while (num < wordNum) {	
                String word = s.substring(i + num * wordLen, i + (num + 1) * wordLen);
                if (allWords.containsKey(word)) {
                    int value = hasWords.getOrDefault(word, 0);
                    hasWords.put(word, value + 1);
                    //出现情况三，遇到了符合的单词，但是次数超了
                    if (hasWords.get(word) > allWords.get(word)) {
                        // hasWords.put(word, value);
                        hasRemoved = true;
                        int removeNum = 0;
                        //一直移除单词，直到次数符合了
                        while (hasWords.get(word) > allWords.get(word)) {
                            String firstWord = s.substring(i + removeNum * wordLen, i + (removeNum + 1) * wordLen);
                            int v = hasWords.get(firstWord);
                            hasWords.put(firstWord, v - 1);
                            removeNum++;
                        }
                        num = num - removeNum + 1; //加 1 是因为我们把当前单词加入到了 HashMap 2 中
                        i = i + (removeNum - 1) * wordLen; //这里依旧是考虑到了最外层的 for 循环，看情况二的解释
                        break;
                    }
                //出现情况二，遇到了不匹配的单词，直接将 i 移动到该单词的后边（但其实这里
                //只是移动到了出现问题单词的地方，因为最外层有 for 循环， i 还会移动一个单词
                //然后刚好就移动到了单词后边）
                } else {
                    hasWords.clear();
                    i = i + num * wordLen;
                    num = 0;
                    break;
                }
                num++;
            }
            if (num == wordNum) {
                res.add(i);
            }
            //出现情况一，子串完全匹配，我们将上一个子串的第一个单词从 HashMap2 中移除
            if (num > 0 && !hasRemoved) {
                String firstWord = s.substring(i, i + wordLen);
                int v = hasWords.get(firstWord);
                hasWords.put(firstWord, v - 1);
                num = num - 1;
            }
        }
    }
    return res;
}
'''