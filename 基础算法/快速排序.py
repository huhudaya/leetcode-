# 指针交换法，一开始基准数不参与
def quick_sort(list, low, high):
    """
    控制快速排序递归的主函数
    :param list:用户传入的待排序列表
    :param low:列表左下标
    :param high:列表右下标
    """
    # 可以不用return
    # if low >= high:
    #     return
    if low < high:
        k_index = deal_list(list, low, high)
        # 递归分界值左边的一组
        quick_sort(list, low, k_index - 1)
        # 递归分界值右边的一组
        quick_sort(list, k_index + 1, high)


def deal_list(list, low, high):
    """实现每趟排序,并找出分界值的下标k_index"""

    # 必须把low ,high保存起来,上面的主函数的left right始终不变
    left = low
    right = high

    # 将列表最左边的值赋值给k
    k = list[low]

    while left < right:  # 当左右"指针"未碰头时就一直比较移动下去
        # 从右边开始,如果比K大:right左移一位,继续比较
        while list[right] > k:  # 或者 list[right]>=k and left<right
            right -= 1

        # 从左边开始,如果比K小: left右移一位,继续比较
        while list[left] <= k and left < right:  # 注意 这里必须要加一个边界判断条件left<right 否则会越界，比如输入6，1
            left += 1

        # 若移动完，二者仍未相遇则交换下标对应的值
        if left < right:
            list[right], list[left] = list[left], list[right]

    # 若移动完，已经相遇，则交换right对应的值和k
    # list[low] = list[right]
    # list[right] = k
    list[low], list[right] = list[right], list[low]  # 最后要交换
    return right


if __name__ == '__main__':
    # list = '9 7 8 6 5 2 6 3 5 1'
    # list = list.split()
    # list = [int(i) for i in list]
    list = [9, 1, 5, 3, 5, 2, 6, 8, 7, 6,5,6,6,1,10,0]
    # list = [6,1]
    # list = [1,6,5,43,6,2,5,6]
    quick_sort(list, 0, len(list) - 1)
    print(list)


# 下面这种方法的好处是第一次右边找到比Key小的值的时候，就进行赋值，然后最后把Key值赋给left就可以

# 1）设置两个变量i、j，排序开始的时候：i=0，j=N-1；
# 2）以第一个数组元素作为关键数据，保存在key中，即key=A[0]；
# 3）从j开始向前搜索，即由后开始向前搜索(j--)，找到第一个小于key的值A[j]，用A[j]覆盖A[0],
# 4）从i开始向后搜索，即由前开始向后搜索(i++)，找到第一个大于key的A[i]，用A[i]覆盖A[j]  即每一次覆盖上一次的
# 5）重复第3、4步，直到i=j；找到符合条件的值，进行交换的时候i， j指针位置不变。另外，i==j这一过程一定正好是i+或j-完成的时候，此时令循环结束。
# 6) 将K还原
# 7) 第一遍快速排序不会直接得到最终结果，只会把比k大和比k小的数分到k的两边。为了得到最后结果，需要再次对下标2两边的数组分别执行此步骤，然后再分解数组，直到数组不能再分解为止（只有一个数据），才能得到正确结果。

# 挖坑法：这个是经常用的 一开始基准数参与 挖坑法会先丢失第一个元素 注意
def quick_sort(array, left, right):
    if left >= right:  # 注意 递归一定要有边界条件 一定要return 不然会一直循环 注意right是右边界，一定要保证没有超过右边界
        return  # 注意 下面的递归函数中的quick_sort中有可能left+1可能会比high大
    # if left<right:   #也可以不适用return，这个时候用if将里面的函数体包起来
    #     pass
    low = left
    high = right
    key = array[low]
    while left < right:
        # 先从右边开始 第一次左边的pivot处是一个坑
        while left < right and array[right] >= key:  # 这样的边界条件最后跳出循环的时候，一定是left=right
            right -= 1
        array[left] = array[right]  # 换新的坑
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    # print(right)
    quick_sort(array, low, right - 1)
    quick_sort(array, left + 1, high)  # left+1 可能超过right


# 快排Python简洁版本
# 这种缺点是会复制多个数组
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# print(quicksort([3, 6, 9, 8, 10, 1, 2, 1]))

# 快排
from typing import List
import random


class Solution:
    def randomized_partition(self, nums, l, r):
        pivot = random.randint(l, r)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l - 1
        for j in range(l, r):
            if nums[j] < nums[r]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def randomized_quicksort(self, nums, l, r):
        if r - l <= 0:
            return
        mid = self.randomized_partition(nums, l, r)
        self.randomized_quicksort(nums, l, mid - 1)
        self.randomized_quicksort(nums, mid + 1, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums





# 标准版本的快速排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 快速排序
        def partition(left, right):
            left_old = left
            temp = nums[left]
            # 指针交换法
            while left < right:
                while left < right and nums[right] >= temp:
                    right -= 1
                while left < right and nums[left] <= temp:
                    left += 1
                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]
            nums[left], nums[left_old] = nums[left_old], nums[left]
            return left

        # 挖坑法
        def partition2(left, right):
            rand_int = random.randint(left, right)
            nums[left], nums[rand_int] = nums[rand_int], nums[left]
            left_old = left
            temp = nums[left_old]
            while left < right:
                while left < right and nums[right] >= temp:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] <= temp:
                    left += 1
                nums[right] = nums[left]
            nums[left] = temp
            return left

        def quick_sort(nums, left, right):
            if left < right:
                index = partition2(left, right)
                quick_sort(nums, left, index - 1)
                quick_sort(nums, index + 1, right)

        n = len(nums)
        quick_sort(nums, 0, n - 1)
        return nums
