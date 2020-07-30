'''
你的初始能量为 P，初始分数为 0，只有一包令牌。

令牌的值为 token[i]，每个令牌最多只能使用一次，可能的两种使用方法如下：

如果你至少有 token[i] 点能量，可以将令牌置为正面朝上，失去 token[i] 点能量，并得到 1 分。
如果我们至少有 1 分，可以将令牌置为反面朝上，获得 token[i] 点能量，并失去 1 分。
在使用任意数量的令牌后，返回我们可以得到的最大分数。

 

示例 1：

输入：tokens = [100], P = 50
输出：0
示例 2：

输入：tokens = [100,200], P = 150
输出：1
示例 3：

输入：tokens = [100,200,300,400], P = 200
输出：2
 

提示：

tokens.length <= 1000
0 <= tokens[i] < 10000
0 <= P < 10000
'''

'''
方法一： 贪心
思路

如果让我们来玩令牌放置这个游戏，在让令牌正面朝上的时候，肯定要去找能量最小的令牌。同样的，在让令牌反面朝上的时候，肯定要去找能量最大的令牌。

算法

只要还有能量，就一直让令牌正面朝上，直到没有能量的时候，让一个令牌反面朝上从而获得能量继续之前的操作。

一定要小心处理边界条件，不然很有可能会写出错误的答案。

这里要牢牢记住，在有能量时候，只能让令牌正面朝上，直到能量不够用了才能让令牌反面朝上。

最终答案一定是在一次让令牌正常朝上操作之后产生的（永远不可能在让令牌反面朝上操作之后产生）
'''
# 核心思路就是消费的时候消费最小的，然后返回的时候返回最大的！
# 类似双指针，左右逼近
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        # 数组类问题没有思路就先排序，然后考虑双指针
        # 贪心
        n = len(tokens) - 1
        tokens.sort()
        cnt = 0
        cur_cum = 0
        if not tokens or P < tokens[0]:
            return 0
        i = 0
        while i <= n:
            # 能量不够
            if tokens[i] > P:
                # 当至少有一分，才将令牌置为反面朝上，这一步相当于双指针左右逼近，获得能量！
                if cnt > 0:
                    P += (tokens[n] - tokens[i])
                    n -= 1
                    i += 1
                else:
                    return cnt
            else:
                cnt += 1
                P -= tokens[i]
                i += 1
        return cnt

'''
int bagOfTokensScore(vector<int>& tokens, int P) {
        sort(tokens.begin(), tokens.end());
        int p = 0, q = tokens.size()-1;
        int score = 0;
        while(p <= q){
            if(tokens[p] > P){  //能量不够加分，从后找能量
                if(score > 0){
                    P += (tokens[q]-tokens[p]);
                    p++;q--;
                } else return score;
            } else {            //能量足够加分
                P -= tokens[p];
                p++;
                score++;
            }
        }
        return score;
    }
'''