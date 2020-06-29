'''
设计一个函数把两个数字相加。不得使用 + 或者其他算术运算符。

示例:

输入: a = 1, b = 1
输出: 2
 

提示：

a, b 均可能是负数或 0
结果不会溢出 32 位整数
'''
# 二进制
# a ^ b 表示无进位相加
# a & b 表示a + b的进位
'''
class Solution {
    public int add(int a, int b) {
        // 第一次将b看成是进位，当进位不为0的时候，终止遍历，返回a,此时的a即无进位的和，因为进位b为0，所以结果就是此时的a
        while (b != 0) {
            int sum = (a ^ b);
            int carry = (a & b) << 1;
            a = sum;
            b = carry;
        }
        return a;
    }
}
'''
class Solution:
    def add(self, a: int, b: int) -> int:
        while b != 0:
            _sum = a ^ b
            carry = a & b << 1
            a = _sum
            b = carry
        return a
print(Solution().add(-1,2))

# 如果a,b是str的二进制类型
class Solution:
    def add(self, a: str, b: str) -> str:
        atmp = eval('0b' + a)
        btmp = eval('0b' + b)
        while btmp:
            ans = (atmp ^ btmp)
            btmp = (atmp & btmp) << 1
            atmp = ans
        return bin(atmp)[2:]
'''
python 由于不知道符号位具体是第几位,因此需要进行的操作是

将输入数字转化成无符号整数
计算无符号整数相加并的到结果
讲结果根据范围判定,映射为有符号整型
'''
class Solution:
    def add(self, a: int, b: int) -> int:
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b != 0:
            carry = a & b
            a ^= b
            b = ((carry) << 1) & 0xFFFFFFFF
        return a if a < 0x80000000 else ~(a^0xFFFFFFFF)
