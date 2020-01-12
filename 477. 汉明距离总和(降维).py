# 477. 汉明距离总和.py
'''
两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。

计算一个数组中，任意两个数之间汉明距离的总和。

示例:

输入: 4, 14, 2

输出: 6

解释: 在二进制表示中，4表示为0100，14表示为1110，2表示为0010。（这样表示是为了体现后四位之间关系）
所以答案为：
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
注意:

数组中元素的范围为从 0到 10^9。
数组的长度不超过 10^4。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/total-hamming-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from collections import defaultdict
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # 在纸上画一画 数学思维降维打击!
        '''
        设数组中第k位的元素的二进制的值,不足的部分补0

        1
        0
        1
        1
        0
        这样有2个0，3个1，每个0可以与3个1进行配对形成汉明距离，故第k位的汉明距离是k*(n-k)
        '''
        # 注意点，整形的范围为2^32，所以这里指定032b就可以了(0表示高位补0，32表示位数，b表示二进制)
        # zip(*) 是指zip函数的逆操作
        # return sum(b.count("0") * b.count("1") for b in zip(*map('{:032b}'.format,nums)))
        # 普通版本
        n = len(nums)
        d = defaultdict(int)
        for num in nums:
        # 对每一个数字n,进行循环判断，判断这个数字转换为二进制之后相应位置是1还是0，对相应的map进行增加。判断是否为0，当终止时候，二进制的所有位数都变成0
            while num != 0:
                # 计数，map中的key是翻译为int之后的值，value是对应的数量
                d[num ^ num & (num - 1)] += 1
                num &= num - 1
        return sum( j * (n - j) for i, j in d.items())
                
# 注意上面这段代码，n ^ n & (n - 1)，这样可以在先消除了最右边的1之后，然后与之前的数字相异或，就可以得到转换为二进制之后的数字最右边为1的位置对应为int时的值
# 比如n = 1001  1001 & 1000 = 1000 此时消除了最右边的1,1001^1000 = 1 
# 然后n &= n-1之后，n=1000, 1000 & 0111 = 0000,1000^0000 = 8
# 最后map中存储着数组中所有元素的每一位翻译为int之后的0和1的个数，最后需要用长度来计算对应位置为0的个数