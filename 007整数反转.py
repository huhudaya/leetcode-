# 007整数反转.py
'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。


int最大值是2147483647，最小值是-2147483648
'''
'''
思路
标签：数学
本题如果不考虑溢出问题，是非常简单的。解决溢出问题有两个思路，第一个思路是通过字符串转换加try catch的方式来解决，第二个思路就是通过数学计算来解决。
由于字符串转换的效率较低且使用较多库函数，所以解题方案不考虑该方法，而是通过数学计算来解决。
通过循环将数字x的每一位拆开，在计算新值时每一步都判断是否溢出。
溢出条件有两个，一个是大于整数最大值MAX_VALUE，另一个是小于整数最小值MIN_VALUE，设当前计算结果为ans，下一位为pop。
从ans * 10 + pop > MAX_VALUE这个溢出条件来看
	当出现 ans > MAX_VALUE / 10 且 还有pop需要添加 时，则一定溢出
	当出现 ans == MAX_VALUE / 10 且 pop > 7 时，则一定溢出，7是2^31 - 1的个位数
	从ans * 10 + pop < MIN_VALUE这个溢出条件来看
	当出现 ans < MIN_VALUE / 10 且 还有pop需要添加 时，则一定溢出
	当出现 ans == MIN_VALUE / 10 且 pop < -8 时，则一定溢出，8是-2^31的个位数
'''
# java 
'''


复杂度分析

时间复杂度：O(log(x))，xx 中大约有 log_10(x)位数字。
空间复杂度：O(1)O(1)。
class Solution {
    public int reverse(int x) {
        int ans = 0;
        while (x != 0) {
            int pop = x % 10;
            if (ans > Integer.MAX_VALUE / 10 || (ans == Integer.MAX_VALUE / 10 && pop > 7)) 
                return 0;
            if (ans < Integer.MIN_VALUE / 10 || (ans == Integer.MIN_VALUE / 10 && pop < -8)) 
                return 0;
            ans = ans * 10 + pop;
            x /= 10;
        }
        return ans;
    }
}
'''

# int最大值是2147483647，最小值是-2147483648


# 在不知道最大正数是2147683647的情况，可以用数学归纳法知道2的31次方个位数是8，从而最大正数 INT_MAX 个位数是7。
# 但是怎么知道 INT_MAX最大位是2？换句话说如果题目把整数范围限定在-2^31,2^31-1怎么知道开头数字是多少。


'''
解题思路：
算法思路： 为对当前数取对 1010 的余数，再一项项填入res尾部，即可完成 intint 翻转。
边界情况处理： intint 取值范围为 [-2^31, 2^31 - 1] ，如果翻转数字溢出，则立即返回 00 。
Python： 存储数字理论上是无限长度，因此每次计算完后判断res与of的大小关系即可；
Java： 数字计算会溢出，因此要判断res和of / 10的大小关系（即确定再添 11 位是否会溢出）。
Python的坑： 由于Python的 // 操作是向下取整，导致正负数取余 % 操作结果不一致，因此需要将原数字转为正数操作。


'''


'''
public int reverse(int x) {
	int ans = 0;
	while (x != 0) {
		if ((ans * 10) / 10 != ans) {
			ans = 0;
			break;
		}
		ans = ans * 10 + x % 10;
		x = x / 10;
	}
	return ans;
}

作弊
class Solution {
    public int reverse(int x) {
        long temp = 0;
       
        while(x != 0){
            int pop = x % 10;
            temp = temp * 10 + pop;
            
            if(temp > Integer.MAX_VALUE || temp < Integer.MIN_VALUE){
                return 0;
            }
            x /= 10;
        }
        return (int)temp;
    }
}
'''

# 利用绝对值进行整数反转，先将负数转成整数
class Solution:
    def reverse(self, x: int) -> int:
        y, res = abs(x), 0
        of = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            res = res * 10 + y % 10
            if res > of: return 0
            y //= 10
        return res if x > 0 else -res



class Solution:
    def reverse(self, x: int) -> int:
        # y // 10 去掉最低位
        # y % 10  得到最低位
        y = abs(x)
        res = 0
        # max(int)=======>[-2^31,2^31-1]
        # if x > 0: res < (2 ^ 31) - 1
        # if x < 0: abs(res) < 2 ^ 31
        of = (1 << 31) -1 if x > 0 else 1 << 31
        while y != 0:
            res = res * 10 + y % 10 
            if res > of:
                return 0
            y //= 10
        return res if x > 0 else -res