'''
输入整数数组 arr ，找出其中最小的 k 个数。
例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4
示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

示例 2：
输入：arr = [0,1,2,1], k = 1
输出：[0]

限制：
0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000
'''
from typing import List


# 排序 O(NlogN)
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]


# 堆 O(NlogK)

'''
我们用一个大根堆实时维护数组的前 k 小值。
首先将前 k 个数插入大根堆中，随后从第 k+1 个数开始遍历
如果当前遍历到的数比大根堆的堆顶的数要小，就把堆顶的数弹出，再插入当前遍历到的数
最后将大根堆里的数存入数组返回即可
在下面的代码中，由于 C++ 语言中的堆（即优先队列）为大根堆，我们可以这么做。
而 Python 语言中的对为小根堆，因此我们要对数组中所有的数取其相反数，才能使用小根堆维护前 k 小值。
python中默认是小根堆
'''
import heapq
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans


# 快排 平均的时间复杂度为O(N)
# 期望为 O(n)
'''
时间复杂度的推导
    partition的过程，时间是o(n)。
    我们在进行第一次partition的时候需要花费n
    第二次partition的时候，数据量减半了，所以只要花费n/2，同理第三次的时候只要花费n/4，以此类推。
    而n+n/2+n/4+...显然是小于2n的，所以这个方法的渐进时间只有o(n)
'''
'''
我们可以借鉴快速排序的思想。
我们知道快排的划分函数每次执行完后都能将数组分成两个部分
小于等于分界值 pivot 的元素的都会被放到数组的左边
大于的都会被放到数组的右边，然后返回分界值的下标。
与快速排序不同的是，快速排序会根据分界值的下标递归处理划分的两侧，而这里我们只处理划分的一边。
'''
# 本质其实就是求第K小的数，就是求第K小的数的索引，然后返回前K个元素就可以了
import random


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)

        # 快排的思想
        def partition(left, right, target):
            index = arr[target]
            arr[left], arr[target] = arr[target], arr[left]
            # 挖坑法
            while left < right:
                while left < right and arr[right] >= index:
                    right -= 1
                arr[left] = arr[right]
                while left < right and arr[left] <= index:
                    left += 1
                arr[right] = arr[left]
            arr[left] = index
            return left

        def partition1(left, right, target):
            index = arr[target]
            arr[left], arr[target] = arr[target], arr[left]
            k = left
            # 指针交换法
            while left < right and arr[right] >= target:
                right -= 1
            while left < right and arr[left] <= target:
                left += 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
            arr[left], arr[k] = arr[k], arr[left]
            return left

        def select(left, right):
            pivot = random.randint(left, right)
            index = partition(left, right, pivot)
            if index > k:
                select(left, index - 1)
            elif index < k:
                select(index + 1, right)
        #  直到index = k退出递归

        if k == 0:
            return []
        if k == n:
            return arr[:k]
        k = k - 1
        select(0, n - 1)
        return arr[:k + 1]

# 自己的版本
import random
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # 快速排序
        def partition(left, right):
            # 随机快排
            tmp = random.randint(left, right)
            arr[tmp], arr[left] = arr[left], arr[tmp]
            target = arr[left]
            while left < right:
                # 挖坑法
                while left < right and arr[right] >= target:
                    right -= 1
                arr[left] = arr[right]
                while left < right and arr[left] <= target:
                    left += 1
                arr[right] = arr[left]
            arr[right] = target
            return left
        n = len(arr)
        left = 0
        right = n - 1
        if k == 0:
            return []
        if k == n:
            return arr[:k]
        k -= 1
        # 错误写法
        # index = partition(left, right)
        # # 注意，这种写法是非常不好的！！！因为每次循环，并没有实际改变left和right，我们希望的是在每一次遍历完都会更新left和right的值
        # while index != k:
        #     if index < k:
        #         tmp = partition(index + 1, right)
        #     elif index > k:
        #         tmp = partition(left, index - 1)
        #     index = tmp
        # return arr[:k + 1]

        #正确写法
        # index = partition(left, right)
        # # 注意，这种写法是非常不好的！！！因为每次循环，并没有实际改变left和right，我们希望的是在每一次遍历完都会更新left和right的值
        # while index != k:
        #     if index < k:
        #         left = index + 1
        #         index = partition(left, right)
        #     elif index > k:
        #         right = index - 1
        #         index = partition(left, right)
        # return arr[:k + 1]
        while 1:
            # 每一次partition都相当于一次排序！
            idx = partition(left, right)
            if idx == k:
                return arr[:k+1]
            if idx < k:
                left = idx + 1
            if idx > k:
                right = idx - 1
        return arr[:k + 1]
