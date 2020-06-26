# 067. 二进制求和.py
'''
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"

链接：https://leetcode-cn.com/problems/add-binary
'''
'''
整体思路是将两个字符串较短的用 00 补齐，使得两个字符串长度一致，然后从末尾进行遍历计算，得到最终结果。

本题解中大致思路与上述一致，但由于字符串操作原因，不确定最后的结果是否会多出一位进位，所以会有 2 种处理方式：

第一种，在进行计算时直接拼接字符串，会得到一个反向字符，需要最后再进行翻转
第二种，按照位置给结果字符赋值，最后如果有进位，则在前方进行字符串拼接添加进位
时间复杂度：O(n)
'''
'''
class Solution {
    public String addBinary(String a, String b) {
        StringBuilder ans = new StringBuilder();
        int ca = 0;
        for(int i = a.length() - 1, j = b.length() - 1;i >= 0 || j >= 0; i--, j--) {
            int sum = ca;
            sum += i >= 0 ? a.charAt(i) - '0' : 0;
            sum += j >= 0 ? b.charAt(j) - '0' : 0;
            ans.append(sum % 2);
            ca = sum / 2;
        }
        ans.append(ca == 1 ? ca : "");
        return ans.reverse().toString();
    }
}

//因为是字符串，所以需要用到ASCII码进行比值
StringBuilder ans = new StringBuilder();
        int ca = 0; //是否进一位 
        for (int i = a.length() - 1, j = b.length() - 1; i >= 0 || j >= 0; i--, j--) {
            int sum = ca;
            sum += (i >= 0 ? a.charAt(i) - '0' : 0); // 获取字符串a对应的某一位的值 当i<0是 sum+=0（向前补0） 否则取原值 ‘1’的char类型和‘0’的char类型刚好相差为1
            sum +=( j >= 0 ? b.charAt(j) - '0' : 0);// 获取字符串a对应的某一位的值 当i<0是 sum+=0（向前补0） 否则取原值 ‘1’的char类型和‘0’的char类型刚好相差为1
            ans.append(sum % 2);  如果二者都为1  那么sum%2应该刚好为0 否则为1
            ca = sum / 2;   如果二者都为1  那么ca 应该刚好为1 否则为0
        }
        ans.append(ca == 1 ? ca : "");// 判断最后一次计算是否有进位  有则在最前面加上1 否则原样输出
        return ans.reverse().toString();
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans, extra = '', 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            if i >= 0:
                extra += ord(a[i]) - ord('0')
            if j >= 0:
                extra += ord(b[j]) - ord('0')
            # 相加最多是 2
            ans += str(extra % 2)
            # 进位符号
            extra //= 2
            i, j = i - 1, j - 1
        if extra == 1:
            ans += '1'
        return ans[::-1]


# 模拟二进制
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        m = len(a) - 1
        n = len(b) - 1
        # 进位
        ca = 0
        while m >= 0 or n >= 0:
            if m >= 0:
                ca += int(a[m])
                # ca += ord(a[m]) - ord("0")
            if n >= 0:
                ca += int(b[n])
                # ca += ord(b[n]) - ord("0")
            # 每一轮都计算当前余数，res是一个字符串，每次加当前得到的结果
            res += str(ca % 2)
            # 当前得到的进位
            ca //= 2
            m, n = m - 1, n - 1
        if ca == 1:
            res += "1"
        return res[::-1]


# Python一行
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return format(int(a, 2) + int(b, 2), 'b')


# 位运算
'''
位运算模拟二进制加法运算。

异或运算的特点是a和b不一样才为1，刚好符合无进位的相加运算
与运算的特点是a和b同为1时才为1，否则为0，刚好可以逐步记录进位。
因此，我们可以利用位运算来避免使用加法运算的使用。



我们可以设计这样的算法来计算：

把 a 和 b 转换成整型数字 x 和 y，在接下来的过程中，x 保存结果，yy 保存进位。
当进位不为 0 时
    计算当前 x 和 y 的无进位相加结果：answer = x ^ y
    计算当前 x 和 y 的进位：carry = (x & y) << 1
    完成本次循环，更新 x = answer，y = carry
返回 x 的二进制形式
为什么这个方法是可行的呢？在第一轮计算中
    answer 的最后一位是 x 和 y 相加之后最后一位的结果
    carry 的倒数第二位是 x 和 y 相加的最后一位的进位
接着每一轮中，由于 carry 是由 x 和 y 按位与并且左移得到的，那么最后会补零，所以在下面计算的过程中后面的数位不受影
而每一轮都可以得到一个低 i 位的答案和它向低 i + 1 位的进位，也就模拟了加法的过程
'''



# 第一次，将x看成是一个数，然后和y要相加，这个时候y就相当于是一个进位
class Solution:
    def addBinary(self, a, b) -> str:
        # 先计算出十进制的值
        x = int(a, 2)  # x保存结果
        y = int(b, 2)  # y保存进位
        while y:  # 当进位不为0的时候
            answer = x ^ y  # x 和 y 相加之后的无进位结果，其中二进制表示的最后一位是两个数相加的无进位的最后一位
            carry = (x & y) << 1  # x 和 y 相加的进位，其中二进制表示的倒数第二位是两个数最后一位的进位
            x, y = answer, carry
        return bin(x)[2:]

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        atmp = eval('0b' + a)
        btmp = eval('0b' + b)
        while btmp:
            ans = (atmp ^ btmp)
            btmp = (atmp & btmp) << 1
            atmp = ans
        return bin(atmp)[2:]
# java
'''
public class Solution {

    public String addBinary(String a, String b) {
        int aLen = a.length();
        int bLen = b.length();
        int maxLen = Math.max(aLen, bLen);

        // 从个位开始加，个位在字符串的右边
        // 代码访问从左到右，因此先反转一下
        StringBuilder sbA = new StringBuilder(a).reverse();
        StringBuilder sbB = new StringBuilder(b).reverse();

        // 让两个字符补齐成一样的长度
        while (sbA.length() < maxLen) {
            sbA.append("0");
        }
        while (sbB.length() < maxLen) {
            sbB.append("0");
        }

        StringBuilder res = new StringBuilder();
        // 进位，初始时进位为 0
        int carry = 0;
        // 当前字符的 ASCII 值减去 '0' 的 ASCII 值，相当于将这个字符转换成数值
        int num1;
        int num2;
        for (int i = 0; i < maxLen; i++) {
            num1 = sbA.charAt(i) - '0';
            num2 = sbB.charAt(i) - '0';
            if (carry + num1 + num2 > 1) {
                // 因为是二进制，所以多余 2 的部分要减去
                res.append(carry + num1 + num2 - 2);
                // 表示要进位
                carry = 1;
            } else {
                res.append(carry + num1 + num2);
                carry = 0;
            }
        }
        // 对于最高位还要进位的情况，需要单独判断
        if (carry == 1) {
            res.append("1");
        }
        // 最后不要忘记再反转一次
        return res.reverse().toString();
    }

    public static void main(String[] args) {
        String a = "1010";
        String b = "1011";
        Solution solution = new Solution();
        String addBinary = solution.addBinary(a, b);
        System.out.println(addBinary);
    }
}
'''
