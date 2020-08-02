'''
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
剑指offer45题
'''

'''
快速排序凭借出色的算法效率和经典的算法思想（分治法），在算法领域有着难以撼动的地位。其中中的partition()函数也成为了很多问题的有效解法。
下面再次温习一下的思想和python代码:

从要排序的数据中取出一个数为“基准数”
通过一趟排序将要排序的数据分割成两部分，其中左边部分都比“基准数”小，右边部分都比“基准数”大。
然后再按步骤2对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
结合本题的特点，在partition()函数中进行比较操作的时候，原始的比较函数一般是遍历过程中的指针index与privot的大小比较，这里可以换成字符串的大小比较：
反证法的思想比较基础，首先我们假设一个有序的数列出现了一对大小方向错误的数值，不妨记为x, y，根据序列中的大小关系，Ay-1<Ay肯定是成立的，我们把Ay前移，直到到达Ax，这样一路交换得到的新序列一定大于原来的序列；然后又因为Ax-1<Ax，所以我们把Ax后移，直到Ay，这样得到的新序列刚好是x,y的位置发生了交换。按照我们的假设（一个有序的数列出现了一对大小方向错误的数值，不妨记为x, y），交换以后的新序列应该是大小方向正确，即达到了最小序列的标准，但是从不等号的方向来看，我们的新序列是大于原序列的。所以与假设矛盾，这样我们就证明了Qsort中比较函数的有效性。
def cmp_(a, b):
    return int(str(a)+str(b))<=int(str(b)+str(a))
'''

# 快排
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 快排
        def fast_sort(strs):
            if len(strs) <= 1:
                return strs
            big, small = [], []
            p = strs.pop()
            for i in strs:
                # 注意排序规则
                if i + p > p + i:
                    big.append(i)
                else:
                    small.append(i)
            return fast_sort(big) + [p] + fast_sort(small)

        strs = [str(num) for num in nums]
        res = fast_sort(strs)
        if res[0] == "0":
            return "0"
        return ''.join(res)


# PYTHON3
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        if not nums:
            return ''
        nums = map(str, nums)
        # 比如10,2  201 - 102 > 0所以需要重新排序，即变成 2,10
        key = cmp_to_key(lambda x, y: int(y + x) - int(x + y))
        # lstrip() 方法: 截掉字符串左边的空格或指定字符  0012->12
        res = ''.join(sorted(nums, key=key)).lstrip('0')
        # 000->''
        return res or '0'


# JAVA STREAM
'''
class Solution {
        public String largestNumber(int[] nums) {
            StringBuilder sb = new StringBuilder();

            for (String s :
                    Arrays.stream(nums)
                            .boxed()
                            .map(Object::toString)
                            .sorted((o1, o2) -> (o2 + o1).compareTo(o1 + o2))
                            .collect(Collectors.toList())) {
                sb.append(s);
            }

            String result = sb.toString();

            return result.startsWith("0") ? "0" : result;
        }
    }
'''

'''
public int compare(Object o1, Object o2)
本来的顺序就bai是参数的先后顺序o1、o2；
如果保持du这个顺序就返回zhi-1，交换顺dao序就返回1，什么都不做就返回0；
所以 升序的话 如果o1<o2，就返回-1。
'''
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_list = map(str, nums)

        def cmp(x, y):
            if x + y == y + x:
                return 0
            elif x + y > y + x:
                return 1
            else:
                return -1

        str_list = sorted(str_list, key=cmp_to_key(cmp), reverse=True)
        return ''.join(str_list) if str_list[0] != '0' else '0'
