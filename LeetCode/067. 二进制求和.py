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
        ans, extra = '',0 
        i,j=len(a)-1,len(b)-1
        while i>=0 or j>=0:
            if i >= 0:
                extra += ord(a[i]) - ord('0')
            if j >= 0:
                extra += ord(b[j]) - ord('0')
            # 相加最多是 2
            ans += str(extra % 2)
            # 进位符号
            extra //= 2
            i,j = i-1,j-1
        if extra == 1:
            ans += '1'
        return ans[::-1]

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        m = len(a) - 1
        n = len(b) - 1
        ca = 0
        while m >= 0 or n >= 0:
            if m >= 0:
                ca += ord(a[m]) - ord("0")
            if n >= 0:
                ca += ord(b[n]) - ord("0")
            # 结果
            res += str(ca % 2)
            # 进位
            ca //= 2
            m, n = m-1, n-1
        if ca == 1:
            res += "1"
        return res[::-1]