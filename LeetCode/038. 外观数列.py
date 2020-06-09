'''
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
注意：整数序列中的每一项将表示为一个字符串。
示例 1:
输入: 1
输出: "1"
解释：这是一个基本样例。
示例 2:
输入: 4
输出: "1211"
解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"
也就是出现频次 = 1 而 值 = 2；类似 "1" 可以读作 "11"。
所以答案是 "12" 和 "11" 组合在一起，也就是 "1211"。
'''

'''
1
11
21
1211
111221
一步一步来
给一个数，这个数是1
描述上一步的数，这个数是 1 即一个1，故写作11
描述上一步的数，这个数是11即两个1，故写作21
描述上一步的数，这个数是21即一个2一个1，故写作12-11
描述上一步的数，这个数是1211即一个1一个2两个1，故写作11-12-21
'''

'''
循环含义
每次外循环含义为给定上一个人报的数，求下一个人报的数
每次内循环为遍历上一个人报的数
具体思路
先设置上一人为'1'
开始外循环
每次外循环先置下一人为空字符串，置待处理的字符num为上一人的第一位，置记录出现的次数为1
开始内循环，遍历上一人的数，如果数是和num一致，则count增加。
若不一致，则将count和num一同添加到next_person报的数中，同时更新num和count
别忘了更新next_person的最后两个数为上一个人最后一个字符以及其出现次数！
'''


class Solution:
    def countAndSay(self, n: int) -> str:
        prev_person = '1'
        for i in range(1, n):
            next_person, num, count = '', prev_person[0], 1
            for j in range(1, len(prev_person)):
                if prev_person[j] == num:
                    count += 1
                else:
                    next_person += str(count) + num
                    num = prev_person[j]
                    count = 1
            next_person += str(count) + num
            prev_person = next_person
        return prev_person


class Solution:
    def countAndSay(self, n: int) -> str:
        arr = ["1"]
        for i in range(n - 1):
            tmp = ""
            j = 0
            while j < len(arr[i]):
                num = arr[i][j]
                time = 0
                while j < len(arr[i]) and num == arr[i][j]:
                    j += 1  # 同上一个相同则继续找
                    time += 1  # 次数加一
                tmp = tmp + str(time) + num
            arr.append(tmp)
        return arr[n - 1]


# 递归
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            new_str = ''
            last_str = self.countAndSay(n - 1)  # 获取上次的报数
            cur = last_str[0]  # 当前要统计的字符，初始值为last_str的首字符
            cur_t = 0  # 当前字符出现的次数

            for i in last_str:
                if i == cur:
                    # 如果相等，则计数+1
                    cur_t += 1
                else:
                    # 否则先报一次数，然后重新初始化开始统计
                    new_str += str(cur_t) + cur
                    cur = i
                    cur_t = 1
            # 循环结束后，还要再报一次，因为如果最后是以if条件退出循环的，最后几个相同的字符并未报出来
            new_str += str(cur_t) + cur
            return new_str