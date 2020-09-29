'''
设计一个支持在平均 时间复杂度 O(1) 下， 执行以下操作的数据结构。

注意: 允许出现重复元素。

insert(val)：向集合中插入元素 val。
remove(val)：当 val 存在时，从集合中移除一个 val。
getRandom：从现有集合中随机获取一个元素。每个元素被返回的概率应该与其在集合中的数量呈线性相关。
示例:

// 初始化一个空的集合。
RandomizedCollection collection = new RandomizedCollection();

// 向集合中插入 1 。返回 true 表示集合不包含 1 。
collection.insert(1);

// 向集合中插入另一个 1 。返回 false 表示集合包含 1 。集合现在包含 [1,1] 。
collection.insert(1);

// 向集合中插入 2 ，返回 true 。集合现在包含 [1,1,2] 。
collection.insert(2);

// getRandom 应当有 2/3 的概率返回 1 ，1/3 的概率返回 2 。
collection.getRandom();

// 从集合中删除 1 ，返回 true 。集合现在包含 [1,2] 。
collection.remove(1);

// getRandom 应有相同概率返回 1 和 2 。
collection.getRandom();
'''
from collections import defaultdict
from random import choice


class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.size = 0
        # 使用一个hashmap + set的数据结构，set中保存的是对应元素的数组下标，数组下标一定是唯一的
        self.cache = defaultdict(set)

    def insert(self, val: int) -> bool:
        # cache中需要记录对应的数组索引
        self.cache[val].add(len(self.nums))
        self.nums.append(val)
        return len(self.cache[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.cache[val]:
            return False
        last = self.nums[-1]
        # 对应数组中的索引
        remove = self.cache[val].pop()
        self.nums[remove] = last
        # 更新hash中last元素对应的数组下标
        self.cache[last].add(remove)
        # 删除hash中last元素对应的数组下标
        self.cache[last].discard(len(self.nums) - 1)
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.nums)
