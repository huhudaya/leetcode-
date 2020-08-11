'''
有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，5，7，9，15，21。

示例 1:

输入: k = 5

输出: 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/get-kth-magic-number-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
为了叙述方便，我们就把符合题目要求的这些数叫做丑数。

不难发现，一个丑数总是由前面的某一个丑数 x3 / x5 / x7 得到。
反过来说也是一样的，一个丑数 x3 / x5 / x7 就会得到某一个更大的丑数。

如果把丑数数列叫做 ugly[i]，那么考虑一下三个数列：
1. ugly[0]*3,ugly[1]*3,ugly[2]*3,ugly[3]*3,ugly[4]*3,ugly[5]*3……
2. ugly[0]*5,ugly[1]*5,ugly[2]*5,ugly[3]*5,ugly[4]*5,ugly[5]*5……
3. ugly[0]*7,ugly[1]*7,ugly[2]*7,ugly[3]*7,ugly[4]*7,ugly[5]*7……

上面这个三个数列合在一起就形成了新的、更长的丑数数列。

如果合在一起呢？这其实就是一个合并有序线性表的问题。

定义三个index 分别指向上面三个数列，下一个丑数一定是三个 index 代表的值中最小的那个。然后相应 index++ 即可。

举个例子
初始值 ugly[0]=1; index1=0; index2=0; index3=0


ugly[1]=Min(ugly[index1]*3,ugly[index2]*5,ugly[index3]*7)
=Min(1*3,1*5,1*7)
=3
于是 index1++;

ugly[2]=Min(ugly[index1]*3,ugly[index2]*5,ugly[index3]*7)
=Min(3*3,1*5,1*7)
=5
于是 index2++;
以此类推
'''
import heapq
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        # 堆实现
        pq = [1]
        heapq.heapify(pq)
        res = -1
        for i in range(k):
            res = heapq.heappop(pq)
            while pq and res == pq[0]:
                heapq.heappop(pq)
            for i in [res * 3, res * 5, res * 7]:
                heapq.heappush(pq, i)
        return res