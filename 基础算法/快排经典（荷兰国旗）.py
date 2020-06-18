import random


def quickSort(list):
    sortHelper(list, 0, len(list) - 1)


def sortHelper(list, l, r):
    # 随机数于数组最后一个值交换
    if l < r:  # 1在这里我自己写错了！！写成了while循环，应该是if
        random_num = l + int(random.random() * (r - l + 1))  # 取一个随机数和队尾进行交换
        list[random_num], list[r] = list[r], list[random_num]
        p = portition(list, l, r)
        sortHelper(list, l, p[0] - 1)
        sortHelper(list, p[1] + 1, r)  # fuck u 在这里又写错了，写成了p[1]+1,写成p[1]就行了


def portition(list, l, r):
    less = l - 1
    more = r  # 可以少写一个变量 空间复杂度减少
    while l < more:  # 这里的l就是我们常见的快排里的index,这里直接写l可以少写几个参数 ∑qwQ
        if list[l] < list[r]:  # 2fuck u 老子在这里又写错了，把r写成了more,所以死活不对！
            less = less + 1  # 3fuck u 这里必须进行交换！！！ 不交换就错了
            list[less], list[l] = list[l], list[less]
            l = l + 1
        elif list[l] > list[r]:
            more = more - 1
            list[l], list[more] = list[more], list[l]
        else:
            l = l + 1
            less += 1
        list[more], list[r] = list[r], list[more]
    # list[more] = list[more]^list[r]
    # list[r] = list[more]^list[r]
    # list[more] = list[more]^list[r]
    return less + 1, more


alist = [1, 4, 4, 26, 2, 2, 4, 4, 4, 2, 4, 6, 45, 5, 2]
quickSort(alist)
print(alist)