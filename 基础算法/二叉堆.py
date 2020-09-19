# 小根堆 顶点的值最小
# 核心思想，建立percDown即heapfy
class BinHeap:
    def __init__(self):
        self.heapList = [0]  # 设置0位置为0,为了以后方便
        self.currentSize = 0

    def percUp(self, i):  # 相当于java中的heapinsert
        while i // 2 > 0:  # 当父节点存在
            if self.heapList[i] < self.heapList[i // 2]:  # 子节点小于父节点 则两者交换
                tmp = self.heapList[i // 2]  # 交换，保存父节点到变量tmp
                self.heapList[i // 2] = self.heapList[i]  # 子节点和父节点交换
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):  # 在堆中插入一个新的元素
        self.heapList.append(k)  # 在堆数组中append一个新的元素
        self.currentSize = self.currentSize + 1  # 当前的堆的容量+1
        self.percUp(self.currentSize)  # 向上调整

    def percDown(self, i):  # 相当于heapfy 向下调整
        # 这里需要循环判断，直到没有子节点
        while (i * 2) <= self.currentSize:  # 判断是否有子节点 即判断是否越界
            mc = self.minChild(i)  # 获得值最小的值的节点
            if self.heapList[i] > self.heapList[mc]:  # 如果当前节点大于它的子节点的最小值的节点，则交换
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            # 这里别忘了更新 i 为 mc
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]  # 先取数组中第一个值，是最小的
        self.heapList[1] = self.heapList[self.currentSize]  # 和最后一个节点的值交换
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):  # 因为已经在0位置设置了0,所以最后一个节点就是len(alist)
        i = len(alist) // 2  # len(alist)表示有几个节点，current//2表示父节点 len(alist)//2表示最后一个节点的父节点
        # 只要最后一个节点的父节点先执行percDown,然后依次i-1，即先底部排好堆，然后依次i-1继续进行排堆
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1


bh = BinHeap()
alist = [9, 5, 6, 2, 3, 1, 9]
bh.buildHeap(alist)
print("传入的列表长度为:{}".format(len(alist)))
list = []
print(bh.heapList)
for i in range(len(alist)):  # 相当于0到(len(alist)-1)
    # print(bh.delMin())
    list.append(bh.delMin())  # 相当于弹len(alist)-1次
print(list)


# 创建大根堆import math
def buildMaxHeap(arr):
    for i in range(len(arr) // 2, -1, -1):
        heapify(arr, i)


# 因为是列表是从0开始的，不同于之前的我们默认给添加了一个0项
def heapify(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right
    # 交换之后 到被交换的点继续heapify
    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)  # 在这里largest已经变成了最大的子节点的位置,在这里我们递归的调用heapfy方法


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr) - 1, 0, -1):
        swap(arr, 0, i)
        arrLen -= 1
        heapify(arr, 0)
    return arr


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(heapSort(alist))

# Test---------------------Test
li = list()
for i in range(len(alist), -1, -1):
    li.append(i)
print(li)
