'''
680. 验证回文字符串 Ⅱ
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:
字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        #双指针
        left = 0
        right = len(s) - 1
        while left < right:
            #准备删除元素
            if s[left] != s[right]:
                #删除左边字符 left+1
                tmp1 = s[left+1:right+1]
                #删除右边字符 right-1
                tmp2 = s[left:right]
                # 使用了[::-1]翻转，所以空间复杂度是O（N）
                if tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]:
                    return True
                else:
                    return False
            left += 1
            right -= 1
        return True


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return checkPalindrome(low + 1, high) or checkPalindrome(low, high - 1)
        return True