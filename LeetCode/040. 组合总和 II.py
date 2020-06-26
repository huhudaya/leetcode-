'''
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
'''
# 注意和39题的区别，candidates中的数是有重复的，并且必须制定candidates中的数据只能使用一次，不能重复用
'''
为了使得解集不包含重复的组合。
我们想一想，如何去掉一个数组中重复的元素
除了使用哈希表以外
我们还可以先对数组升序排序
重复的元素一定不是排好序以后的第 1 个元素和相同元素的第 1 个元素
根据这个思想，我们先对数组升序排序是有必要的。
候选数组有序，对于在递归树中发现重复分支，进而“剪枝”也是有效的。

核心思路就是剪枝，什么时候剪枝？
当后一个分支和前一个分支value一样的时候，前一个搜索范围肯定更大
所以得到的结果一定是重复的，所以这时候需要剪掉
'''
# 避免重复
'''
这个避免重复当思想是在是太重要了。
这个方法最重要的作用是，可以让同一层级，不出现相同的元素。即
                  1
                 / \
                2   2  这种情况不会发生 但是却允许了不同层级之间的重复即：
               /     \
              5       5
                例2
                  1
                 /
                2      这种情况确是允许的
               /
              2  
                
为何会有这种神奇的效果呢？
首先 cur-1 == cur 是用于判定当前元素是否和之前元素相同的语句。这个语句就能砍掉例1。
可是问题来了，如果把所有当前与之前一个元素相同的都砍掉，那么例二的情况也会消失。 
因为当第二个2出现的时候，他就和前一个2相同了。
                
那么如何保留例2呢？
那么就用cur > begin 来避免这种情况，你发现例1中的两个2是处在同一个层级上的，
例2的两个2是处在不同层级上的。
在一个for循环中，所有被遍历到的数都是属于一个层级的。我们要让一个层级中，
必须出现且只出现一个2，那么就放过第一个出现重复的2，但不放过后面出现的2。
第一个出现的2的特点就是 cur == begin. 第二个出现的2 特点是cur > begin.
'''

from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 这类问题先排序，然后要考虑剪枝
        candidates.sort()
        n = len(candidates)
        res = []
        self.__dfs(candidates, target, 0, res, [], n)
        return res

    def __dfs(self, candidates, target, start, res, path, size):
        # 终止条件
        if target == 0:
            res.append(path[:])
            return
        # 递归
        for i in range(start, size):
            # 大剪枝
            if target < candidates[i]:
                break
            # 小剪枝 这里的判断条件 candidates[i] == candidates[i - 1] 是为了防止出现 2，2 变换位置之后是两个结果，其实就是一个结果
            if start < i and candidates[i] == candidates[i - 1]:
                continue
            # 路径选择
            path.append(candidates[i])
            # 递归 从当前元素之后，不包括当前元素 所以是 i+1
            self.__dfs(candidates, target - candidates[i], i + 1, res, path, size)
            # 撤销选择
            path.pop()
Solution().combinationSum2([1,1],2)