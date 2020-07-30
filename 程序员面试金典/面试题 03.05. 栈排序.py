'''

栈排序。 编写程序，对栈进行排序使最小元素位于栈顶。最多只能使用一个其他的临时栈存放数据，但不得将元素复制到别的数据结构（如数组）中。该栈支持如下操作：push、pop、peek 和 isEmpty。当栈为空时，peek 返回 -1。

示例1:

 输入：
["SortedStack", "push", "push", "peek", "pop", "peek"]
[[], [1], [2], [], [], []]
 输出：
[null,null,null,1,null,2]
示例2:

 输入：
["SortedStack", "pop", "pop", "push", "pop", "isEmpty"]
[[], [], [], [1], [], []]
 输出：
[null,null,null,null,null,true]
说明:

栈中的元素数目在[0, 5000]范围内。
'''



class SortedStack:
    def __init__(self):
        self.ret = []

    def push(self, val: int) -> None:
        import bisect
        bisect.insort(self.ret, val)

    def pop(self) -> None:
        try:
            self.ret.pop(0)
        except:
            pass

    def peek(self) -> int:
        try:
            return self.ret[0]
        except:
            return -1

    def isEmpty(self) -> bool:
        return self.ret == []


# 两个栈
class SortedStack:
    def __init__(self):
        self.data = []
        self.helper = []

    def push(self, val: int) -> None:

        if not self.data: # 如果 data 为空，直接将元素添加到data中
            self.data.append(val)
        else:
            # 如果 data 顶的元素比val小，将 data 中比 val 小的元素倒到 helper 中
            #然后将 val 放入 data 顶
            if self.data[-1] < val:
                while self.data and self.data[-1] < val:
                    self.helper.append(self.data.pop(-1))
                self.data.append(val)
            # 如果 data 顶的元素等于 val，直接将 val 放在 data 顶
            elif self.data[-1] == val:
                self.data.append(val)
            else:
                # 此时的情况为：val < sel.data[-1]，需要把 helper 中比 val 大的元素倒到data顶去
                # case 1, 如果helper 为空，或者 val 大于等于 helper 顶的元素
                # 直接将val 放到 data 顶
                if not self.helper or self.helper[-1] <= val:
                    self.data.append(val)
                else:
                    # case 2, val 小于 helper 的栈顶元素，则把小于 val 的元素倒回 data 中
                    # 然后把 val 放在 data 栈顶
                    while self.helper and val < self.helper[-1]:
                        self.data.append(self.helper.pop())
                    self.data.append(val)

    def pop(self) -> None:
        if not self.data:
            return -1
        # 由于 helper 中会放有较小的元素，
        # 首先检查 helper 是否有元素，有的话将其倒入 data 中
        # pop data 顶的元素（当前最小值）
        while self.helper:
            self.data.append(self.helper.pop())
        return self.data.pop()

    def peek(self) -> int:
        if not self.data:
            return -1
        while self.helper:
            self.data.append(self.helper.pop())
        return self.data[-1]

    def isEmpty(self) -> bool:
        return self.data == []