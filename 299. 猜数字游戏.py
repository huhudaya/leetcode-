'''
你正在和你的朋友玩 猜数字（Bulls and Cows）游戏：你写下一个数字让你的朋友猜。每次他猜测后，你给他一个提示，告诉他有多少位数字和确切位置都猜对了（称为“Bulls”, 公牛），有多少位数字猜对了但是位置不对（称为“Cows”, 奶牛）。你的朋友将会根据提示继续猜，直到猜出秘密数字。

请写出一个根据秘密数字和朋友的猜测数返回提示的函数，用 A 表示公牛，用 B 表示奶牛。

请注意秘密数字和朋友的猜测数都可能含有重复数字。

示例 1:

输入: secret = "1807", guess = "7810"

输出: "1A3B"

解释: 1 公牛和 3 奶牛。公牛是 8，奶牛是 0, 1 和 7。
示例 2:

输入: secret = "1123", guess = "0111"

输出: "1A1B"

解释: 朋友猜测数中的第一个 1 是公牛，第二个或第三个 1 可被视为奶牛。
说明: 你可以假设秘密数字和朋友的猜测数都只包含数字，并且它们的长度永远相等。
'''
from typing import List
from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        from collections import Counter
        # 准备两个hashMap
        s_c = Counter(secret)
        g_c = Counter(guess)
        res = [0, 0]
        for x, y in zip(secret, guess):
            if x == y:
                s_c[x] -= 1
                g_c[y] -= 1
                res[0] += 1
        # 也是找重叠的，当位置不匹配但是数量上匹配的字符。要用min
        for k in s_c & g_c:
            res[1] += min(s_c[k], g_c[k])
        return "{}A{}B".format(res[0], res[1])


# java
'''
class Solution {
    public String getHint(String secret, String guess) {
        int len = secret.length();
        int A = 0;//公牛的数量
        int B = 0;//奶牛的数量
        char[] h1 = new char[10];//secret中不是公牛的数字统计
        char[] h2 = new char[10];//guess中不是公牛的数字统计
        char[] sc = secret.toCharArray();
        char[] gc = guess.toCharArray();
        for (int i = 0; i < len; i++) {
            if(sc[i] == gc[i]) A++;
            else {
                int ids = sc[i] - '0';
                int idg = gc[i] - '0';
                h1[ids]++;
                h2[idg]++;
            }
        }
        for (int i = 0; i < 10; i++) {
            //取secret与guess的重叠部分
            B += Math.min(h1[i], h2[i]);
        }
        String ans = A + "A" + B + "B";
        return ans;
    }
}
'''

# java
'''
方法二：由于猜的数字只包括0~9这九位数字，因此我们可以定义两个10位数组来存储某个数出现的次数
索引代表数值，索引处的值代表次数。
思路如下：先遍历一次字符串，如果字符相等，公牛数加一，否则，将它们对应的数组中的次数加一。
第一次遍历完毕后可以得到两个数组，分别对应了两个字符串中某一个数出现的次数(匹配的字符不算)
然后我们可以再进行一次遍历，两个数组每一个索引处的最小值相加即可得到母牛数。
'''
'''
    /*
        Time complexity: O(n)
        Space complexity: O(1)
     */
    public String getHint(String secret, String guess) {
        int aCount = 0;     // 公牛数
        int bCount = 0;     // 母牛数
        //int mapS[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        //int mapG[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        int[] mapS[] = new int[10];
        int[] mapG[] = new int[10];

        for (int i = 0; i < secret.length(); i++) {
            char temp = secret.charAt(i);
            if (temp == guess.charAt(i))
                aCount++;
            else {
                mapS[temp - '0']++;
                mapG[guess.charAt(i) - '0']++;
            }
        }
        for (int i = 0; i < 10; i++) {
            bCount += Math.min(mapG[i], mapS[i]);
        }
        return aCount + "A" + bCount + "B";
    }
'''


# 自己的版本
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # 因为数字在0-9 所以准备两个数组
        n = len(secret)
        sc = [0 for _ in range(10)]
        ge = [0 for _ in range(10)]
        resA = 0
        resB = 0
        # 遍历
        for i in range(n):
            if secret[i] == guess[i]:
                resA += 1
            # 不匹配的数字，在对应的索引上累加数量
            else:
                sc[int(secret[i])] += 1
                ge[int(guess[i])] += 1
        print(sc)
        print(ge)
        # 遍历不位置上不匹配，但是数量上匹配的结果,注意这里是range(10),我第一次写成了reange(n)
        for i in range(10):
            resB += min(sc[i], ge[i])
        return "{resA}A{resB}B".format(resA=resA, resB=resB)
