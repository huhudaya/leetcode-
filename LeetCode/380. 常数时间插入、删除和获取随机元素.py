'''
设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。
注意，本题中元素不重复

insert(val)：当元素 val 不存在时，向集合中插入该项。
remove(val)：元素 val 存在时，从集合中移除该项。
getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。
示例 :

// 初始化一个空的集合。
RandomizedSet randomSet = new RandomizedSet();

// 向集合中插入 1 。返回 true 表示 1 被成功地插入。
randomSet.insert(1);

// 返回 false ，表示集合中不存在 2 。
randomSet.remove(2);

// 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
randomSet.insert(2);

// getRandom 应随机返回 1 或 2 。
randomSet.getRandom();

// 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
randomSet.remove(1);

// 2 已在集合中，所以返回 false 。
randomSet.insert(2);

// 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
randomSet.getRandom();
'''

import random


class RandomizedSet:

    def __init__(self):
        self.cache = {}
        self.nums = []
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.cache:
            return False
        else:
            self.cache[val] = len(self.nums)
            self.nums.append(val)
            self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.cache:
            self.nums[self.cache[val]] = self.nums[self.size - 1]
            self.cache[self.nums[self.size - 1]] = self.cache[val]
            self.size -= 1
            self.nums.pop()
            self.cache.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        rand_int = random.randint(0, self.size - 1)
        return self.nums[rand_int]


# 优化版本
class RandomizedSet:

    def __init__(self):
        self.cache = {}
        self.nums = []
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.cache:
            return False
        self.cache[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.cache:
            return False
        # 将要删除的元素交换到数组末位，然后删除
        index = self.cache[val]
        last = self.nums[-1]
        # 将数组中对应索引位置更新为原来数组中的最后一个元素
        self.nums[index] = last
        # 更新hash中的val对应的数组索引
        self.cache[last] = index
        self.nums.pop()
        self.cache.pop(val)
        return True

    def getRandom(self) -> int:
        rand_int = random.randint(0, len(self.nums) - 1)
        return self.nums[rand_int]
