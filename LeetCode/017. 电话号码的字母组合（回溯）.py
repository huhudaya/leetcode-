# 017. 电话号码的字母组合.py
'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
'''


# pythonic风格
class Solution:
    def letterCombinations(self, digits: str) :
        m = {
            '2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz'),
            }
        if not digits: return []
        ls1 = ['']
        for i in digits:
            ls1 = [x + y for x in ls1 for y in m[i]]
        return ls1

# 回溯
'''
复杂度分析

时间复杂度:	O(3^N*4^M)
其中:		N 是输入数字中对应 3 个字母的数目（比方说 2，3，4，5，6，8）
 			M 是输入数字中对应 4 个字母的数目（比方说 7，9），N+M 是输入数字的总数。

空间复杂度：O(3^N*4^M)
'''
'''
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择

其核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」，特别简单。


for 选择 in 选择列表:
    # 做选择
    将该选择从选择列表移除
    路径.add(选择)
    backtrack(路径, 选择列表)
    # 撤销选择
    路径.remove(选择)
'''
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                
        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])
                    
        output = []
        if digits:
            backtrack("", digits)
        return output

# 标准模板的写法
class Solution:
    def letterCombinations(self, digits: str):
        # 回溯法模板
        '''
        result = []
        def backtrack(路径, 选择列表):
            if 满足结束条件:
                result.add(路径)
                return
            for 选择 in 选择列表:
                做选择
                backtrack(路径, 选择列表)
                撤销选择
        其核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」，特别简单。
        for 选择 in 选择列表:
            # 做选择
            将该选择从选择列表移除
            路径.add(选择)
            backtrack(路径, 选择列表)
            # 撤销选择
            路径.remove(选择)
        '''
        # 字典模拟
        phone = {'2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']}
        # 回溯函数
        def backtrack(combination, digits):
            # 满足条件
            if len(digits) == 0:
                res.append(combination)
            else:
                for str in phone[digits[0]]:
                    # 做选择 下面这样写就错了，要传一个变量进去,因为str是不可变类型，所以每次都是一个新的str
                    combination += str
                    # backtrack(路径, 选择列表)
                    backtrack(combination, digits[1:])
                    # 这里因为是字符串，每次都是新的字符串，所以不用撤销选择
                    combination = combination[:-len(str)]
        res = []
        if digits:
            backtrack("", digits)
        return res
# 简约
class Solution:
    def letterCombinations(self, digits: str):
        # 回溯法模板
        '''
        result = []
        def backtrack(路径, 选择列表):
            if 满足结束条件:
                result.add(路径)
                return
            for 选择 in 选择列表:
                做选择
                backtrack(路径, 选择列表)
                撤销选择
        其核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」，特别简单。
        for 选择 in 选择列表:
            # 做选择
            将该选择从选择列表移除
            路径.add(选择)
            backtrack(路径, 选择列表)
            # 撤销选择
            路径.remove(选择)
        '''
        # 字典模拟
        phone = {'2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']}
        # 回溯函数
        def backtrack(combination, digits):
            # 满足条件
            if len(digits) == 0:
                res.append(combination)
            else:
                for str in phone[digits[0]]:
                    # 做选择 下面这样写就错了，要传一个变量进去,因为str是不可变类型，所以每次都是一个新的str
                    # combination += str
                    # backtrack(路径, 选择列表)
                    backtrack(combination + str, digits[1:])
                    # 这里因为是字符串，每次都是新的字符串，所以不用撤销选择
        res = []
        if digits:
            backtrack("", digits)
        return res