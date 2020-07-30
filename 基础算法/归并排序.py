# 思路是利用递归 注意递归的三要素
# 一定要有递归结束条件，不断调用自身，不断向递归结束条件靠近
# 核心思想，先递归sort，然后merge,不同于快排，快排是先排序，然后递归子快排
# 谁小移动谁
# 使用递归的时候需要注意一点，当不需要返回值得时候 不需要return，当需要有返回值的时候，一定要设置return
# 归并排序的空间复杂度有点高啊!
# 每次都需要一个子的空间
def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        # 当使用list[:], 此时left和right是两个新开辟的链表
        left = alist[0:mid]
        right = alist[mid:]
        mergeSort(left)
        mergeSort(right)  # 递归过程
        # merge过程
        i = 0
        j = 0
        k = 0  # 用k来表示新的数组 其实可以用一个新的数组，arr_new，但是增加了空间消耗，所以可以使用原数组
        # merge的过程
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]  # 因为数组是可变类型，所以直接对列表进行值修改
                i += 1
            # print(1)
            else:
                alist[k] = right[j]
                j += 1
            k += 1  # 每次k+1
        while i < len(left):  # 总有一个要越界
            alist[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            alist[k] = right[j]
            k += 1
            j += 1
    return alist


list = [6, 1, 23, 4, 234, 1, 2, 5, 2, 4, 1]
list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
list = [-2, 3, 2]
mergeSort(list)
print(list)
list = [1, 2, 3]
list[0] = 2
num = list
print(num)
