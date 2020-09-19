'''
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

 

示例 1:

输入: [10,2]
输出: "102"
示例 2:

输入: [3,30,34,5,9]
输出: "3033459"

'''

# 内置排序
# 相当于一个排序的过程，先两两排序？？好像是这样？
from typing import List
import functools
# lambda
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def sort_rule(x, y):
            a, b = x + y, y + x
            return b > a

        strs = [str(num) for num in nums]
        strs.sort(key=functools.cmp_to_key(sort_rule))
        return ''.join(strs)
# java
'''
class Solution {
    public String minNumber(int[] nums) {
        List<String> list = new ArrayList<>();
        for (int num : nums) {
            list.add(String.valueOf(num));
        }
        list.sort((o1, o2) -> (o1 + o2).compareTo(o2 + o1));
        return String.join("", list);
    }
}
'''


from typing import List
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def cmp_(a, b):
            return int(str(a) + str(b)) <= int(str(b) + str(a))

        def partition(left: int, right: int):
            privot = right
            small = left - 1
            for index in range(left, right):
                # if nums[index]<nums[privot]:
                if cmp_(nums[index], nums[privot]):
                    small += 1
                    nums[small], nums[index] = nums[index], nums[small]
            nums[small + 1], nums[privot] = nums[privot], nums[small + 1]
            return small + 1

        def q_sort(l: int, r: int):
            if l >= r:
                return nums
            p = partition(l, r)
            q_sort(l, p - 1)
            q_sort(p, r)
            return nums

        q_sort(0, len(nums) - 1)
        return "".join([str(x) for x in nums])



from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 放一个快排搁着
        def fast_sort(strs):
            if len(strs) <= 1:
                return strs
            less, greater = [], []
            p = strs.pop()
            for i in strs:
                if i + p < p + i:
                    less.append(i)
                else:
                    greater.append(i)
            return fast_sort(less) + [p] + fast_sort(greater)

        strs = [str(num) for num in nums]
        res = fast_sort(strs)
        if res[0] == "0":
            return "0"
        return ''.join(res)
