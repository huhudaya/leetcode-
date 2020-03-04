# 260只出现一次的数字.py
'''
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :
输入: [1,2,1,3,2,5]
输出: [3,5]
链接：https://leetcode-cn.com/problems/single-number-iii
'''
'''
1.对所有数字异或,一样的数字抵消,出现一次的两个数字异或运算后必定不为0;
2.这个数字和相反数做与运算得到一个二进制位最右边一位为1的数字;
3.mask和数组的每个数字做与运算,等于0的分为一组,等于mask的分为一组,同时也将两个不一样的数字分开;
4.完结。
'''
'''
    public int[] singleNumber(int[] nums) {
        int xor = 0;
        for (int i : nums)// 一样的抵消,不一样的两个数字异或运算结果必定有一位是1
            xor ^= i;

        int mask = xor & (-xor);

        int[] ans = new int[2];
        for (int i : nums) {
            if ((i & mask) == 0)//== 0、 == mask 两种结果
                ans[0] ^= i;
            else
                ans[1] ^= i;
        }
        return ans;
    }
'''
'''
在基础题目中，数组中所有数字异或得到单独数字；
那么在这个题目中，数组中所有数字异或得到这两个单独数字的异或，比如是x；
我们只需要把数组中所有数字分成两组
并且每一组中的仅包含一个单独数字
那么就把这个问题转化为基础问题了，比如：
数组:[a,b,c,d,a,b]转换为[a,a,c],[b,b,d]，或者是[a,a,d],[b,b,c]
这没区别，就把这个问题转换成了基础问题了，问题在于如何转换
x是两个不相同数字的异或，那么x必然不是0
我们只要找到x为1的某一位，比如第n位，或者m位，只要是x在这一位上为1。
那么在这一位上，c,d是不同的，异或运算才得到1，否则就是0
这就是区分c,d的关键
遍历数组，当第n位为1的时，归位一组，第n位不为1，归为另一组。这样就得到了两个组，将问题成功转换为夹出问题
'''
from functools import reduce

'''
1.对所有数字异或,一样的数字抵消,出现一次的两个数字异或运算后必定不为0;
2.这个数字和相反数做与运算得到一个二进制位最右边一位为1的数字;
3.mask和数组的每个数字做与运算,等于0的分为一组,等于mask的分为一组,同时也将两个不一样的数字分开;
4.完结
'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tmp = 0
        # 任意数 和 0 异或不变
        for i in nums:
            tmp ^= i
        # 等价于 tmp ^ tmp & (tmp-1),得到最右边的1对应的十进制数
        tmp = tmp & (-tmp)
        num1 = 0
        num2 = 0
        for i in nums:
            # 分组，等于0的分为一组
            if i & tmp:
                num1 ^= i
            # 不等于0的分为一组
            else:
                num2 ^= i
        return [num1, num2]
