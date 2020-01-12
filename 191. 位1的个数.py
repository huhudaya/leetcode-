# 191. 位1的个数.py
'''
编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。

 

示例 1：

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
示例 2：

输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
示例 3：

输入：11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
 

提示：

请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3。
 

进阶:
如果多次调用这个函数，你将如何优化你的算法？

链接：https://leetcode-cn.com/problems/number-of-1-bits
'''

# 解一
# 调用函数懒蛋法。

# Python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

# 解二
# 手动循环计算 1 的个数。
# Python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = bin(n)
        count = 0
        for c in n:
            if c == "1":
                count += 1
        return count  
# 解三
# 十进制转二进制的方式。每次对 2 取余判断是否是 1，是的话就 count = count + 1。
# Python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            res = n % 2
            if res == 1:
                count += 1
            n //= 2
        return count
# 解四
# 位运算法。
# 把 n 与 1 进行与运算，将得到 n 的最低位数字。因此可以取出最低位数，再将 n 右移一位。循环此步骤，直到 n 等于零。
# Python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += n&1
            n >>= 1
        return count

'''
//技巧：直接去掉二进制中位置最靠后的1
//可以分情况讨论n末尾是1还是0来验证这个算法
int hammingWeight(uint32_t n) {
        int ans=0;
        while(n)
        {
            ans++;
            n &= n-1;
        }
        return ans;
    }
'''
'''
//直接判断二进制最低为的数是不是1
int hammingWeight(uint32_t n) {
        int ans=0;
        while(n)
        {
            ans+=n&1;
            n>>=1; //去掉最低位
        }
        return ans;
    }
'''
'''
//除K取余法
int hammingWeight(uint32_t n) {
        int ans=0;
        while(n)
        {
            ans+=n%2;
            n>>=1;
        }
        return ans;
    }
'''





