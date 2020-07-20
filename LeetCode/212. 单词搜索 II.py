'''

给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例:

输入:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]
说明:
你可以假设所有输入都由小写字母 a-z 组成。

提示:
你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。
'''

'''
根据题意，此 55 张牌是顺子的 充分条件 如下：

除大小王外，所有牌 无重复 ；
设此 55 张牌中最大的牌为 maxmax ，最小的牌为 minmin （大小王除外），则需满足：
max - min < 5
max−min<5

因而，可将问题转化为：此 55 张牌是否满足以上两个条件？

'''

# 方法一： 集合 Set + 遍历
# 遍历五张牌，遇到大小王（即 00 ）直接跳过。
# 判别重复： 利用 Set 实现遍历判重， Set 的查找方法的时间复杂度为 O(1) ；
# 获取最大 / 最小的牌： 借助辅助变量 mama 和 mimi ，遍历统计即可。
# 时间复杂度 O(N) = O(5) = O(1)O(N)=O(5)=O(1) ： 其中 NN 为 numsnums 长度，本题中 N \equiv 5N≡5 ；遍历数组使用 O(N)O(N) 时间。
# 空间复杂度 O(N) = O(5) = O(1)O(N)=O(5)=O(1) ： 用于判重的辅助 Set 使用 O(N) 额外空间。

from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0:
                continue  # 跳过大小王
            ma = max(ma, num)  # 最大牌
            mi = min(mi, num)  # 最小牌
            if num in repeat:
                return False  # 若有重复，提前返回 false
            repeat.add(num)  # 添加牌至 Set
        return ma - mi < 5  # 最大牌 - 最小牌 < 5 则可构成顺子


# 方法二：排序 + 遍历
# 先对数组执行排序。
# 判别重复： 排序数组中的相同元素位置相邻，因此可通过遍历数组，判断 nums[i] = nums[i + 1]nums[i]=nums[i+1] 是否成立来判重。
# 获取最大 / 最小的牌： 排序后，数组末位元素 nums[4]nums[4] 为最大牌；元素 nums[joker]nums[joker] 为最小牌，其中 jokerjoker 为大小王的数量。
# 复杂度分析：
# 时间复杂度 O(N \log N) = O(5 \log 5) = O(1)O(NlogN)=O(5log5)=O(1) ： 其中 NN为 nums 长度，本题中 N \equiv 5N≡5 ；数组排序使用 O(N \log N)O(NlogN) 时间。
# 空间复杂度 O(1)O(1) ： 变量 jokerjoker 使用 O(1)O(1) 大小的额外空间。

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        joker = 0
        nums.sort()  # 数组排序
        for i in range(4):
            if nums[i] == 0:
                joker += 1  # 统计大小王数量
            elif nums[i] == nums[i + 1]:
                return False  # 若有重复，提前返回 false
        return nums[4] - nums[joker] < 5  # 最大牌 - 最小牌 < 5 则可构成顺子
