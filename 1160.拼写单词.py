'''
给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
注意：每次拼写（指拼写词汇表中的一个单词）时，chars 中的每个字母都只能用一次。
返回词汇表 words 中你掌握的所有单词的 长度之和。
示例 1：

输入：words = ["cat","bt","hat","tree"], chars = "atach"
输出：6
解释：
可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。
示例 2：

输入：words = ["hello","world","leetcode"], chars = "welldonehoneyr"
输出：10
解释：
可以形成字符串 "hello" 和 "world"，所以答案是 5 + 5 = 10。
'''
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_cnt = collections.Counter(chars)
        ans = 0
        for word in words:
            word_cnt = collections.Counter(word)
            for c in word_cnt:
                if chars_cnt[c] < word_cnt[c]:
                    break
            else:
                ans += len(word)
        return ans



import collections
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        cnt = collections.Counter(chars)
        for w in words:
            c = collections.Counter(w)
            if all([c[i] <= cnt[i] for i in c]):
                ans += len(w)
        return ans

'''
友情提示：遇到有提示字符串仅包含小写（或者大写）英文字母的题，
都可以试着考虑能不能构造长度为26的每个元素分别代表一个字母的数组，来简化计算

对于这道题，用数组c来保存字母表里每个字母出现的次数
如法炮制，再对词汇表中的每个词汇都做一数组w，比较数组w与数组c的对应位置

如果w中的都不大于c，就说明该词可以被拼写出，长度计入结果
如果w其中有一个超过了c，则说明不可以被拼写，直接跳至下一个（这里用到了带label的continue语法）
'''
'''
class Solution {
    public int countCharacters(String[] words, String chars) {
        int[] c = new int[26];
        for(char cc : chars.toCharArray()) {
            c[(int)(cc - 'a')] += 1;
        }
        int res = 0;
        a: for(String word : words) {
            int[] w = new int[26];
            for(char ww : word.toCharArray()) {
                w[(int)(ww - 'a')] += 1;
            }
            for(int i=0; i<26; i++) {
                if(w[i] > c[i]) {
                    continue a;
                }
            }
            res += word.length();
        }
        return res;
    }
}
'''
'''
思路：

前提条件为chars当中的每一个字符只能使用一次，这也决定了，每个字符出现的次数必须符合要求，而不是出现一次就符合要求
如果words数组中每个字符串word的每个字符的出现次数都满足小于等于该字符在chars出现的次数，那么称该word则符合统计条件
需要一个工具来帮助我们统计每个字符的出现次数，可以理解为每个字符的计数器。
首先想到的就是HashMap，key为某个字符，value为出现的次数
其他答主巧妙的提出了可以使用int[26]来统计每个字符的出现次数。
因为题目说只包含小写字母，所以可以直接声明一个长度为26的数组。
下标[0,25]分别代表[a,z]，值为出现的次数。
关于如何存储至指定的下标，我们可以借助ASCII码。
字符可以转换为相应的整数，比如[a,z]对应[97,122]
可以看出代表的数字都是递增1的，所以我们可以把字符a当做一个基准，即可以使用当前字符-'a'来获得数组下标。
比如当前字符为a，那么'a'-'a'转换为数字即97-97结果为0，也就是我们需要存储的数组下标
'''


'''
/**
 * 分析
 * 1.判断直接返回0的条件
 *     1.1-words为空或长度为0
 *     1.2-chars为空或者长度为0
 * 2.判断words中某个word不用参与统计的条件
 *     2.1-word为空或者长度为0
 *     2.2-word的长度>chars的长度
 * 3.判断chars是否能拼成words，需要记录words的每个字符出现的次数以及chars每个字符出现的次数
 * 如果words中每个字符出现的次数都小于等于该字符在chars中出现的次数，那么则可以拼成该字母，否则不能
 * 4.存储容器
 *     3.1-hashMap：key为每个字符，value为个数
 *     3.2-数组，长度为26，因为都是小写字母，下标0的元素代表'a'出现的次数，下标1的元素代表'b'出现的次数...下标25的元素代表'z'出现的菜蔬
 *     下标 = 字符 - 'a'，例如'a' - 'a' = 0，'b' - 'a' = 1
 */
class Solution {

    static final int SIZE = 26; // 数组大小为26-26个小写字母

    /**
     * 数组版本
     * @param words
     * @param chars
     * @return
     */
    public int countCharacters(String[] words, String chars) {
        /* 如果words为空或者长度为0
           如果chars为空或者长度为0
           直接返回0 */
        if (words == null || words.length == 0 || chars == null || chars.length() == 0)
            return 0;

        int spellOut = 0; // 可以拼出的字母的长度
        // boolean canSpell;    // 标识位，用来标识能否拼出
        int[] wordCounter;    // words字符计数器
        int[] charCounter = new int[SIZE];    // chars字符计数器

        /* 记录chars中每个字符出现的次数 */
        for (char c: chars.toCharArray()) {
            charCounter[c - 'a'] ++;
        }

        /* 记录words中的每个word的每个字符的出现的次数
           并与chars计数器比较 */
        loop:  // 标签，用来处理内部循环与外部循环之间的通信，如不使用，可以在循环使用一个boolean类型的变量来判断是否符合条件
        for (String w: words) {
            /* 如果w为空或者w长度为0或者w的长度>chars的长度，不参与统计 */
            if (w == null || w.length() == 0 || w.length() > chars.length())
                continue;

            wordCounter = new int[SIZE];
            // flag = true;
            for (char c: w.toCharArray()) {
                // 判断该字符是否在chars中出现
                if (charCounter[c - 'a'] == 0) continue loop; // canSpell = false;
                wordCounter[c - 'a'] ++;
            }
            /* 判断每个word的字符出现次数是否至少在chars中同样出现
               即word的字符出现次数是否<=chars出现的次数 */
            for (int i = 0; i < SIZE; i ++) {
                if (wordCounter[i] > charCounter[i])
                    continue loop;  // canSpell = false亦可；
            }
            //if (canSpell)
            spellOut += w.length();
        }
        return spellOut;
    }

    /**
     * hashMap版本
     * @param words
     * @param chars
     * @return
     */
    public int countCharacters2(String[] words, String chars) {
        /* 如果words为空或者长度为0
           如果chars为空或者长度为0
           直接返回0 */
        if (words == null || words.length == 0 || chars == null || chars.length() == 0)
            return 0;

        int spellOut = 0; // 可以拼出的字母的长度
        // boolean canSpell;    // 标识位，用来标识能否拼出
        Map<Character, Integer> wordCounter;    // words字符计数器
        Map<Character, Integer> charCounter = new HashMap<>();    // chars字符计数器

        /* 记录chars中每个字符出现的次数 */
        for (char c: chars.toCharArray()) {
            charCounter.put(c, charCounter.getOrDefault(c, 0) + 1);
        }

        /* 记录words中的每个word的每个字符的出现的次数
           并与chars计数器比较 */
        loop:  // 标签，用来处理内部循环与外部循环之间的通信，如不使用，可以在循环使用一个boolean类型的变量来判断是否符合条件
        for (String w: words) {
            /* 如果w为空或者w长度为0或者w的长度>chars的长度，不参与统计 */
            if (w == null || w.length() == 0 || w.length() > chars.length())
                continue;

            wordCounter = new HashMap<>();
            // flag = true;
            for (char c: w.toCharArray()) {
                // 判断该字符是否在chars中出现
                if (!charCounter.containsKey(c)) continue loop; // canSpell = false;
                wordCounter.put(c, wordCounter.getOrDefault(c, 0) + 1);
            }
            /* 判断每个word的字符出现次数是否至少在chars中同样出现
               即word的字符出现次数是否<=chars出现的次数 */
            for (char c: wordCounter.keySet()) {
                if (wordCounter.get(c) > charCounter.getOrDefault(c, 0))
                    continue loop;  // canSpell = false亦可；
            }
            //if (canSpell)
            spellOut += w.length();
        }
        return spellOut;
    }
}
'''


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        # 构建hash数组
        hash = [0 for i in range(26)]
        for i in chars:
            hash[ord(i) - 97] += 1
        for word in words:
            word_hash = [0 for i in range(26)]
            for w in word:
                word_hash[ord(w) - 97] += 1
                if word_hash[ord(w) - 97] > hash[ord(w) - 97]:
                    break
            # 注意这里的用法, 不熟悉这个语法的话也可以用一个 flag 来标记  相当于todo
            else:
                res += len(word)
        return res
print(Solution().countCharacters(["hello","world","leetcode"],"welldonehoneyr"))