# 81. 搜索旋转排序数组 II.py
'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:

输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false
进阶:

这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
'''
'''
解题思路：
本题是需要使用二分查找，怎么分是关键，举个例子：

第一类
10111 和 11101 这种。此种情况下 nums[start] == nums[mid]，分不清到底是前面有序还是后面有序，此时 start++ 即可。相当于去掉一个重复的干扰项。

第二类
22 33 44 55 66 77 11 这种，也就是 nums[start] < nums[mid]。此例子中就是 2 < 5；
这种情况下，前半部分有序。因此如果 nums[start] <=target<nums[mid]，则在前半部分找，否则去后半部分找。

第三类
66 77 11 22 33 44 55 这种，也就是 nums[start] > nums[mid]。此例子中就是 6 > 2；
这种情况下，后半部分有序。因此如果 nums[mid] <target<=nums[end]。则在后半部分找，否则去前半部分找。
'''

# java
'''
public boolean search(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return false;
        }
        int start = 0;
        int end = nums.length - 1;
        int mid;
        while (start <= end) {
            mid = start + (end - start) / 2;
            if (nums[mid] == target) {
                return true;
            }
            if (nums[start] == nums[mid]) {
                start++;
                continue;
            }
            //前半部分有序
            if (nums[start] < nums[mid]) {
                //target在前半部分
                if (nums[mid] > target && nums[start] <= target) {
                    end = mid - 1;
                } else {  //否则，去后半部分找
                    start = mid + 1;
                }
            } else {
                //后半部分有序
                //target在后半部分
                if (nums[mid] < target && nums[end] >= target) {
                    start = mid + 1;
                } else {  //否则，去后半部分找
                    end = mid - 1;
                }
            }
        }
        //一直没找到，返回false
        return false;

    }
'''


class Solution:
    def search(self, nums, target: int) -> bool:

        left = 0
        right = len(nums) - 1
        while left <= right:
            # print(left, right)
            mid = left + (right - left) // 2
            # 等于目标值
            if nums[mid] == target:
                return True

            if nums[mid] == nums[left] == nums[right]:
                left += 1
                right -= 1
            # 在前部分
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


# 自己的版本
class Solution:
    def search(self, nums, target: int) -> bool:
        left = 0
        right = len(nums) - 1
        # 牢记LeetCode中一定有[]的存在，所以一定要判断一下
        if not nums:
            return False
        while left + 1 < right:
            mid = left + ((right - left) >> 1)
            # mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[right] == nums[mid]:
                left += 1
                right -= 1
            # 后面的部分
            # elif nums[mid] <= nums[right]:
            #     if nums[mid] <= target <= nums[right]:
            #         left = mid
            #     else:
            #         right = mid
            # else:
            #     if nums[left] <= target <= nums[mid]:
            #         right = mid
            #     else:
            #         left = mid

            elif nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid
        if nums[left] == target or nums[right] == target:
            return True
        else:
            return False

print(Solution().search([1, 3, 1, 1, 2],3))
# 注意 13112这种情况是不会发生的，因为原数组是排好序的，按某一个点进行旋转，显然11213不满足升序条件