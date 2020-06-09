'''
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
示例:
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
'''
# 暴力法
'''
我们要知道IP的格式,每位是在0~255之间,
注意: 不能出现以0开头的两位以上数字,比如012,08...
'''
# 注意理解题意，要求复原，所以这里的顺序是不能变的，因此直接循环遍历就可以了 参考四数之和
from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []
        # 判读是否满足ip的条件
        def helper(tmp):
            if not tmp or (tmp[0] == "0" and len(tmp) > 1) or int(tmp) > 255:
                return False
            return True
        # 三个循环,把数字分成四份
        for i in range(3):
            for j in range(i + 1, i + 4):
                for k in range(j + 1, j + 4):
                    if i < n and j < n and k < n:
                        tmp1 = s[:i + 1]
                        tmp2 = s[i + 1:j + 1]
                        tmp3 = s[j + 1:k + 1]
                        tmp4 = s[k + 1:]
                        # print(tmp1, tmp2, tmp3, tmp4)
                        # all 用来判断可迭代参数iterable中所有的元素是否都是True
                        if all(map(helper, [tmp1, tmp2, tmp3, tmp4])):
                            res.append(tmp1 + "." + tmp2 + "." + tmp3 + "." + tmp4)
        return res
print(Solution().restoreIpAddresses('25525511135'))

'''
public List<String> restoreIpAddresses(String s) {
    List<String> res = new ArrayList<String>();
    int len = s.length();
    //i < 4 保证第一部分不超过 3 位数
    //i < len - 2 保证剩余的字符串还能分成 3 部分
    for(int i = 1; i<4 && i<len-2; i++){
        for(int j = i+1; j<i+4 && j<len-1; j++){
            for(int k = j+1; k<j+4 && k<len; k++){
                //保存四部分的字符串
                String s1 = s.substring(0,i), s2 = s.substring(i,j), s3 = s.substring(j,k), s4 = s.substring(k,len);
                //判断是否合法
                if(isValid(s1) && isValid(s2) && isValid(s3) && isValid(s4)){
                    res.add(s1+"."+s2+"."+s3+"."+s4);
                }
            }
        }
    }
    return res;
}
public boolean isValid(String s){
    if(s.length()>3 || s.length()==0 || (s.charAt(0)=='0' && s.length()>1) || Integer.parseInt(s)>255)
        return false;
    return true;
}
'''

# dfs
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []
        tmpList = []
        self.dfs(s, tmpList)
        return self.res

    #dfs遍历，s为待处理字段，tmp存储所有ip小段
    def dfs(self, s, tmpList):
        if len(tmpList) == 4:   #递归出口，凑够4段
            if len(s) == 0:     #s没有剩余，说明找到一个合法ip，否则返回
                self.res.append('.'.join(tmpList))
            return
        for i in range(1, 4):   #遍历取s的头，长度从1到3
            if i <= len(s):     #防止越界
                if int(s[:i]) > 255:    #数字超出范围
                    return
                elif i > 1 and s[0] == '0':    #除去0开头，且长度大于1情况
                    return
                self.dfs(s[i:], tmpList + [s[:i]])  #截断s，并将本次截取内容写入tmp


# 回溯DFS
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)

        def backtrack(i, tmp, flag):
            if i == n and flag == 0:
                res.append(tmp[:-1])
                return
            if flag < 0:
                return
            for j in range(i, i + 3):
                if j < n:
                    if i == j and s[j] == "0":
                        backtrack(j + 1, tmp + s[j] + ".", flag - 1)
                        break
                    if 0 < int(s[i:j + 1]) <= 255:
                        backtrack(j + 1, tmp + s[i:j + 1] + ".", flag - 1)

        backtrack(0, "", 4)
        return res

'''
public List<String> restoreIpAddresses(String s) {
    List<String> ans = new ArrayList<>(); //保存最终的所有结果
    getAns(s, 0, new StringBuilder(), ans, 0);
    return ans;
}

/**
* @param:  start 字符串开始部分
* @param:  temp 已经划分的部分
* @param:  ans 保存所有的解
* @param:  count 当前已经加入了几部分
*/
private void getAns(String s, int start, StringBuilder temp, List<String> ans, int count) {
    //如果剩余的长度大于剩下的部分都取 3 位数的长度，那么直接结束
    //例如 s = 121231312312, length = 12
    //当前 start = 1，count 等于 1
    //剩余字符串长度 11，剩余部分 4 - count = 3 部分，最多 3 * 3 是 9
    //所以一定是非法的，直接结束
    if (s.length() - start > 3 * (4 - count)) {
        return;
    }
    //当前刚好到达了末尾
    if (start == s.length()) {
        //当前刚好是 4 部分，将结果加入
        if (count == 4) {
            ans.add(new String(temp.substring(0, temp.length() - 1)));
        }
        return;
    }
    //当前超过末位，或者已经到达了 4 部分结束掉
    if (start > s.length() || count == 4) {
        return;
    }
    //保存的当前的解
    StringBuilder before = new StringBuilder(temp);

    //加入 1 位数
    temp.append(s.charAt(start) + "" + '.');
    getAns(s, start + 1, temp, ans, count + 1);

    //如果开头是 0，直接结束
    if (s.charAt(start) == '0')
        return;

    //加入 2 位数
    if (start + 1 < s.length()) {
        temp = new StringBuilder(before);//恢复为之前的解
        temp.append(s.substring(start, start + 2) + "" + '.');
        getAns(s, start + 2, temp, ans, count + 1);
    }

    //加入 3 位数
    if (start + 2 < s.length()) {
        temp = new StringBuilder(before);
        int num = Integer.parseInt(s.substring(start, start + 3));
        if (num >= 0 && num <= 255) {
            temp.append(s.substring(start, start + 3) + "" + '.');
            getAns(s, start + 3, temp, ans, count + 1);
        }
    }

}

'''
