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
# 最小正数，从 1 开始找。一种很特殊的情况是：数组 [1, 2, 3, 4, 5] 一共有 5 个数，最多搜索数组的长度这么多次，一定能得到答案。
from typing import List
class Solution:
    # 3 应该放在索引为 2 的地方
    # 4 应该放在索引为 3 的地方
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            # 先判断这个数字是不是索引，然后判断这个数字是不是放在了正确的地方
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                # self.__swap(nums, i, nums[i] - 1)
                nums[nums[i] - 1],nums[i] = nums[i],nums[nums[i] - 1]
        for i in range(size):
            if i + 1 != nums[i]:
                return i + 1
        return size + 1
    def __swap(self, nums, index1, index2):
        nums[index1], nums[index2] = nums[index2], nums[index1]
print(Solution().firstMissingPositive([3,4,-1,1]))