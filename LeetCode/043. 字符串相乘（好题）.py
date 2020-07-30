'''
给定两个以字符串形式表示的非负整数 num1 和 num2
返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

链接：https://leetcode-cn.com/problems/multiply-strings
'''

'''
string multiply(string num1, string num2) {
    int m = num1.size(), n = num2.size();
    // 结果最多为 m + n 位数
    vector<int> res(m + n, 0);
    // 从个位数开始逐位相乘
    for (int i = m - 1; i >= 0; i--)
        for (int j = n - 1; j >= 0; j--) {
            int mul = (num1[i]-'0') * (num2[j]-'0');
            // 乘积在 res 对应的索引位置
            int p1 = i + j, p2 = i + j + 1;
            // 叠加到 res 上
            int sum = mul + res[p2];
            res[p2] = sum % 10;
            res[p1] += sum / 10;
        }
    // 结果前缀可能存的 0（未使用的位）
    int i = 0;
    while (i < res.size() && res[i] == 0)
        i++;
    // 将计算结果转化成字符串
    string str;
    for (; i < res.size(); i++)
        str.push_back('0' + res[i]);
    
    return str.size() == 0 ? "0" : str;
}
'''


# https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247484466&idx=1&sn=0281340cc1f41230e4512e905b9d27dd&chksm=9bd7fa3aaca0732c95d25c637d42ad8d9b80f8165098ded837f83791c673b5d6a71721c738a3&scene=21#wechat_redirect
'''
整个计算过程大概是这样，有两个指针i，j在num1和num2上游走，计算乘积，同时将乘积叠加到res的正确位置：
现在还有一个关键问题，如何将乘积叠加到res的正确位置，或者说，如何通过i，j计算res的对应索引呢？
其实，细心观察之后就发现，num1[i]和num2[j]的乘积对应的就是res[i+j]和res[i+j+1]这两个位置。
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        res = [0 for _ in range(m + n)]
        # 需要倒着遍历！！！
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                sum = mul + res[p2]
                res[p2] = sum % 10
                # 注意，这里必须是 +=
                res[p1] += sum // 10
        print(res)
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        # 将结果转换为字符串
        ans = ""
        for i in range(i, len(res)):
            ans += str(res[i])
        if len(ans) == 0:
            return "0"
        else:
            return ans