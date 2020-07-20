'''
给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。

返回使 A 中的每个值都是唯一的最少操作次数。
示例 1:
输入：[1,2,2]
输出：1
解释：经过一次 move 操作，数组将变为 [1, 2, 3]。
示例 2:

输入：[3,2,1,2,1,7]
输出：6
解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
提示：
0 <= A.length <= 40000
0 <= A[i] < 40000
'''
# 计数 O(L)
'''
 就是总的需要操作次数，比如数组【1，1，1，1，6】中间缺了 2,3，4,5
 有三个重复的数字1，那么操作最少的次数为（2-1）+（3-1）+（4-1）=（2+3+4）-（1+1+1）
 它是先ans减去x*y (x表示重复的数字，y表示这个数字重复的次数，这里：x =1,y =3)
 这时候 ans = 0 - 1*3 = -3，然后遇到数组里面没有出现的数字（也就是出现次数为0的数字）就把ans加上这个数字
 第一次是2 ，ans = -3+2=-1, 然后是 3，ans =-1+3 = 2, 最后是 4， ans= 2+4 = 6
'''
from typing import List


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        count = [0] * 80000
        # 构建一个计数数组（桶）
        for x in A:
            count[x] += 1

        ans = taken = 0
        for x in range(80000):
            if count[x] >= 2:
                # token表示多重复的个数
                taken += count[x] - 1
                ans -= x * (count[x] - 1)  # 先减去
            # 如果新找到一个数之前没有存在过
            elif taken > 0 and count[x] == 0:
                taken -= 1
                ans += x  # 直到找见一个数

        return ans


Solution().minIncrementForUnique([1, 1, 1, 3, 7, 9])


# 先排序，再依次遍历数组元素，若当前元素小于等于它前一个元素，则将其变为前一个数 +1
# 贪心
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        # 贪心算法
        A.sort()
        count = 0
        for i in range(1, len(A)):
            if A[i] <= A[i - 1]:
                count += A[i - 1] - A[i] + 1
                A[i] = A[i - 1] + 1
        return count


# java
'''
public int minIncrementForUnique(int[] A) {
    Arrays.sort(A); // 先排序
    int curmax = -1; // 当前数组最大值
    int res = 0;
    for (int i = 0; i < A.length; i++) {
        if (A[i] <= curmax) {
            // 当前元素 A[i] 需要增加到 curmax + 1
            res += (curmax + 1 - A[i]); // 记录自增次数
        }
        curmax = Math.max(curmax + 1, A[i]);
    }
    return res;
}
'''


# 自己的版本
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        # 排序
        A.sort()
        n = len(A)
        # 使用一个变量记录前一个值
        pre_max = A[0]
        res = 0
        for i in range(1, n):
            if A[i] <= pre_max:
                res += pre_max + 1 - A[i]
                pre_max = pre_max + 1
            if A[i] > pre_max:
                pre_max = A[i]
        return res
