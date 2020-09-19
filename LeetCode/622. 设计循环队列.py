'''
设计你的循环队列实现。
 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。
 它也被称为“环形缓冲器”。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。
在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：

MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。
 

示例：

MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3
circularQueue.enQueue(1);  // 返回 true
circularQueue.enQueue(2);  // 返回 true
circularQueue.enQueue(3);  // 返回 true
circularQueue.enQueue(4);  // 返回 false，队列已满
circularQueue.Rear();  // 返回 3
circularQueue.isFull();  // 返回 true
circularQueue.deQueue();  // 返回 true
circularQueue.enQueue(4);  // 返回 true
circularQueue.Rear();  // 返回 4
 

提示：

所有的值都在 0 至 1000 的范围内；
操作数将在 1 至 1000 的范围内；
请不要使用内置的队列库。
'''
# 基本的定义
'''
要注意的地方有：

1、 定义循环变量 front 和 rear 。一直保持这个定义，到底是先赋值还是先移动指针就很容易想清楚了。

    front：指向队列头部第 1 个有效数据的位置；
    rear：指向队列尾部（即最后 1 个有效数据）的下一个位置，即下一个从队尾入队元素的位置。
    
    （说明：这个定义是依据“动态数组”的定义模仿而来。）

2、 为了避免“队列为空”和“队列为满”的判别条件冲突，我们有意浪费了一个位置。
    浪费一个位置是指：循环数组中任何时刻一定至少有一个位置不存放有效元素。
    判别队列为空的条件是：front == rear;
    判别队列为满的条件是：(rear + 1) % capacity == front;。可以这样理解，当 rear 循环到数组的前面，要从后面追上 front，还差一格的时候，判定队列为满。

3、 因为有循环的出现，要特别注意处理数组下标可能越界的情况。指针后移的时候，索引 + 1，并且要注意取模。
'''
# 自己的版本
class MyCircularQueue:

    def __init__(self, k: int):
        # 指向第一个存放元素的索引
        self.front = 0
        # 指向队尾的下一个位置的索引
        self.rear = 0
        # 因为我们需要一个空余的位置，所以这里capcity = 实际容量 + 1
        self.capacity = k + 1
        self.arr = [0 for _ in range(self.capacity)]

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        # 入队，先将rear填充新值，然后移动rear到下一个索引
        self.arr[self.rear] = value
        # rear指向下一个位置
        self.rear = (self.rear + 1) % self.capacity
        return True

    def deQueue(self) -> bool:
        # 出队此时移动front到下一个位置，只需要移动front即可
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        # 注意，这里需要将rear - 1之后对 capacity 取余
        return self.arr[(self.rear - 1 + self.capacity) % self.capacity]

    def isEmpty(self) -> bool:
        if self.rear == self.front:
            return True
        return False

    def isFull(self) -> bool:
        if (self.rear + 1) % self.capacity == self.front:
            return True
        return False
