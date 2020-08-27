'''

给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。

示例:

nums = [1, 2, 3]
target = 4

所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

请注意，顺序不同的序列被视作不同的组合。

因此输出为 7。
进阶：
如果给定的数组中含有负数会怎么样？
问题会产生什么变化？
我们需要在题目中添加什么限制来允许负数的出现？

致谢：
特别感谢 @pbrother 添加此问题并创建所有测试用例。
'''

'''
如果是组合背包
    1.数组中的元素可以重复出现，但是考虑顺序(即顺序不同组合不同)
        此时nums放在内循环，target放在外循环，正序遍历，
        因为这样dp的每个状态更新时都不用考虑前面的状态是否选择了第i个num。
    2.数组中的元素可以重复出现，但是不考虑顺序(顺序不同组合相同)
        nums放在外循环，target在内循环。且内循环正序。
    组合背包的问题一般是求组合个数。
'''
from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        # 顺序不同，组合不同，所以将nums放在内部循环
        for i in range(1, target + 1):
            for j in range(n):
                if nums[j] <= i:
                    dp[i] += dp[i - nums[j]]
        return dp[target]
    def combinationSum_test(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        # 顺序不同，组合不同，所以将nums放在内部循环
        for j in range(n):
            for i in range(1, target + 1):
                if nums[j] <= i:
                    dp[i] += dp[i - nums[j]]
        return dp[target]
print(Solution().combinationSum4([1,2,3],5))
