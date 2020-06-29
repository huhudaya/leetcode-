'''
集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。

给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

示例 1:

输入: nums = [1,2,2,4]
输出: [2,3]
注意:

给定数组的长度范围是 [2, 10000]。
给定的数组是无序的。
'''
'''
其实很容易解决这个问题，先遍历一次数组，用一个哈希表记录每个数字出现的次数，然后遍历一次[1..N]，看看那个元素重复出现，那个元素没有出现，就 OK 了。

但问题是，这个常规解法需要一个哈希表，也就是 O(N) 的空间复杂度。
你看题目给的条件那么巧，在[1..N]的几个数字中恰好有一个重复，一个缺失，事出反常必有妖，对吧。

O(N) 的时间复杂度遍历数组是无法避免的，所以我们可以想想办法如何降低空间复杂度，是否可以在 O(1) 的空间复杂度之下找到重复和确实的元素呢？


这个问题的特点是，每个元素和数组索引有一定的对应关系。

我们现在自己改造下问题，暂且将nums中的元素变为[0..N-1]，这样每个元素就和一个数组索引完全对应了，这样方便理解一些。

如果说nums中不存在重复元素和缺失元素，那么每个元素就和唯一一个索引值对应，对吧？

现在的问题是，有一个元素重复了，同时导致一个元素缺失了，这会产生什么现象呢？
会导致有两个元素对应到了同一个索引，而且会有一个索引没有元素对应过去。

那么，如果我能够通过某些方法，找到这个重复对应的索引，不就是找到了那个重复元素么？
找到那个没有元素对应的索引，不就是找到了那个缺失的元素了么？

那么，如何不使用额外空间判断某个索引有多少个元素对应呢？这就是这个问题的精妙之处了：

通过将每个索引对应的元素变成负数，以表示这个索引被对应过一次了：
'''
'''
vector<int> findErrorNums(vector<int>& nums) {
    int n = nums.size();
    int dup = -1;
    for (int i = 0; i < n; i++) {
        // 索引应该从 0 开始
        int index = abs(nums[i]) - 1;
        if (nums[index] < 0)
            dup = abs(nums[i]);
        else
            nums[index] *= -1;
    }

    int missing = -1;
    for (int i = 0; i < n; i++)
        if (nums[i] > 0)
            // 将索引转换成元素
            missing = i + 1;

    return {dup, missing};
}
'''
# https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247485050&idx=1&sn=dac757454b2df9a1291f1e8027f56c1b&chksm=9bd7f872aca07164da3e1138df630d63b41e4f071f71194069bcedeef866c1b91650a77be3d2&scene=21#wechat_redirect
from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # 绝对值的方法
        n = len(nums)
        dup = -1
        for num in nums:
            # nums[index] 小于 0 则说明重复访问
            if nums[abs(num) - 1] < 0:
                dup = abs(num)
            else:
                nums[abs(num) - 1] *= -1
        missing = -1
        for i in range(n):
            # nums[i] 大于 0 则说明没有访问
            if nums[i] > 0:
                missing = i + 1
        return [dup, missing]
