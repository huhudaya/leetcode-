'''
给定一个正整数数组 w ，其中 w[i] 代表位置 i 的权重，请写一个函数 pickIndex ，它可以随机地获取位置 i，选取位置 i 的概率与 w[i] 成正比。

例如，给定一个值 [1，9] 的输入列表，当我们从中选择一个数字时，很有可能 10 次中有 9 次应该选择数字 9 作为答案。

 

示例 1：

输入：
["Solution","pickIndex"]
[[[1]],[]]
输出：[null,0]
示例 2：

输入：
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
输出：[null,0,1,1,1,0]
输入语法说明：
输入是两个列表：调用成员函数名和调用的参数。Solution 的构造函数有一个参数，即数组 w。pickIndex 没有参数。输入参数是一个列表，即使参数为空，也会输入一个 [] 空列表。

提示：
1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex 将被调用不超过 10000 次
'''
'''
思路：
对于w[i][1,3,5,6]我们需要根据权重获取随机数，所以需要从头开始将权重值进行逐步累积，累积后数组为：[1,4,9,15]
然后使用Random产生一个[1,15]之间的随机数，如果随机数落在[1]，对应元素为0，如果随机数落在[2,4]区间，对应元素为1，如果随机数落在[5,9]区间，对应元素为2，如果随机数落在[10,15]，对应元素为4
在得出随机数后如果顺序遍历效率比较低，这里的权重累积数组是递增的，所以可以考虑使用二分法，找到随机数对应的区间。
'''

from typing import List
from random import random
import bisect


class Solution:

    def __init__(self, w: List[int]):
        probability = [0] * len(w)
        _sum = sum(w)
        cur = 0
        for i in range(len(w)):
            cur += w[i]
            probability[i] = cur / _sum
        self.probability = probability

    def pickIndex(self) -> int:
        return bisect.bisect_right(self.probability, random.random())


# java
'''
class Solution {
    //权重累加数组
    int[] arr;

    public Solution(int[] w) {
        arr = new int[w.length];
        int sum = 0;
        for (int i = 0; i < w.length; i++) {
            sum += w[i];
            arr[i] = sum;
        }
    }
    public int pickIndex() {
        //产生随机数
        Random random = new Random();
        int randomNum = random.nextInt(arr[arr.length - 1]) + 1;
        //二分查找随机数所在的区间
        int left = 0, right = arr.length - 1;
        while (left < right) {
            int mid = left + ((right - left) >> 1);
            if (arr[mid] == randomNum) {
                return mid;
            } else if (arr[mid] > randomNum) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}
'''
import itertools


class Solution:

    def __init__(self, w: List[int]):
        self.cum = list(itertools.accumulate(w))
        self.total = self.cum[-1]

    def pickIndex(self) -> int:
        target = random.randint(0, self.total - 1)
        l, r = 0, len(self.cum) - 1
        while l < r:
            mid = (l + r) // 2
            if self.cum[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return l
