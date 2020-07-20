'''
41. 缺失的第一个正数
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
说明:

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。
'''
# 暴力解法 时间空间复杂度都是O(N)
'''
import java.util.HashSet;
import java.util.Set;

public class Solution {

    public int firstMissingPositive(int[] nums) {
        int len = nums.length;

        Set<Integer> hashSet = new HashSet<>();
        for (int num : nums) {
            hashSet.add(num);
        }

        for (int i = 1; i <= len ; i++) {
            if (!hashSet.contains(i)){
                return i;
            }
        }

        return len + 1;
    }
}
'''
# 排序
'''
import java.util.Arrays;

public class Solution {

    public int firstMissingPositive(int[] nums) {
        int len = nums.length;
        Arrays.sort(nums);

        for (int i = 1; i <= len; i++) {
            int res = binarySearch(nums, i);
            if (res == -1) {
                return i;
            }
        }
        return len + 1;
    }

    private int binarySearch(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int mid = (left + right) >>> 1;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }
}
'''
# 抽屉法
# 注意一点 找缺失的第一个正数，应该从1开始找
# 最小正数，从 1 开始找。
# 一种很特殊的情况是：数组 [1, 2, 3, 4, 5] 一共有 5 个数，
# 最多搜索数组的长度这么多次，一定能得到答案。
# [3, 4, -1, 1]
from typing import List

'''
由于题目要求我们“只能使用常数级别的空间”，而要找的数一定在 [1, N + 1] 左闭右闭（这里 N 是数组的长度）这个区间里。
因此，我们可以就把原始的数组当做哈希表来使用。
事实上，哈希表其实本身也是一个数组；
我们要找的数就在 [1, N + 1] 里，最后 N + 1 这个元素我们不用找。
因为在前面的 N 个元素都找不到的情况下，我们才返回 N + 1；
那么，我们可以采取这样的思路：
就把 1 这个数放到下标为 0 的位置，
2 这个数放到下标为 1 的位置，按照这种思路整理一遍数组。
然后我们再遍历一次数组，第 1 个遇到的它的值不等于下标的那个数，就是我们要找的缺失的第一个正数。
这个思想就相当于我们自己编写哈希函数，这个哈希函数的规则特别简单，那就是数值为 i 的数映射到下标为 i - 1 的位置。
'''


class Solution:
    # 要找的数在[1, N]
    # 3 应该放在索引为 2 的地方
    # 4 应该放在索引为 3 的地方
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            # 先判断这个数字是不是在适合的索引区间，比如在[1,len(nums)]，然后判断这个数字是不是放在了正确的地方
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                # self.__swap(nums, i, nums[i] - 1)
                # 下面这种交换是错误的交换！！！！！一定要注意，先交换到nums[nums[i] - 1]
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(size):
            if i + 1 != nums[i]:
                return i + 1
        return size + 1

    def __swap(self, nums, index1, index2):
        nums[index1], nums[index2] = nums[index2], nums[index1]


print(Solution().firstMissingPositive([3, 4, -1, 1]))

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 抽屉的思想
        size = len(nums)
        for i in range(size):
            # num[i] >= 1,就一定要找到属于自己的位置 而且我们只考虑在1和size之间的范围
            while 1 <= nums[i] <= size and nums[nums[i] - 1] != nums[i]:
                # 下面这种交换是错误的交换！！！！！一定要注意，先交换到nums[nums[i] - 1]
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        # 遍历，找到第一个不满足的位置的索引即为缺失的第一个正数
        for i in range(size):
            if i + 1 != nums[i]:
                return i + 1
        return size + 1


# 方法二：
# 原地hash
'''
实际上，对于一个长度为 N 的数组，其中没有出现的最小正整数只能在 [1, N+1]中。
这是因为如果 [1, N] 都出现了，那么答案是 N+1，否则答案是 [1, N][1,N] 中没有出现的最小正整数。

我们将数组中所有小于等于 0 的数修改为 N+1；

我们遍历数组中的每一个数 xx，它可能已经被打了标记，因此原本对应的数为 |x|∣x∣，其中 |\,|∣∣ 为绝对值符号。如果 |x| \in [1, N]∣x∣∈[1,N]，那么我们给数组中的第 |x| - 1∣x∣−1 个位置的数添加一个负号。注意如果它已经有负号，不需要重复添加；

在遍历完成之后，如果数组中的每一个数都是负数，那么答案是 N+1，否则答案是第一个正数的位置加 1。
'''


# 重点是将所有小于等于0的数字变成n+1,这样这个数组中的数就都是大于1了，这样就可以是用绝对值算法，即用负号作为标记是否有这个数的存在


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 原地hash
        n = len(nums)
        # 小于等于0的数置为n+1
        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = n + 1
        for i, num in enumerate(nums):
            # 如果要替换的位置已经存在了，说明重复了
            if 1 <= abs(nums[i]) <= n and nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
        print(nums)
        for i, num in enumerate(nums):
            if num > 0:
                return i + 1
        return n + 1
