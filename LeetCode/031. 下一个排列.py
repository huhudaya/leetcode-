# 31. 下一个排列.py
'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

链接：https://leetcode-cn.com/problems/next-permutation
'''
# java
'''
public class Solution {
    public void nextPermutation(int[] nums) {
        int i = nums.length - 2;
        while (i >= 0 && nums[i + 1] <= nums[i]) {
            i--;
        }
        if (i >= 0) {
            int j = nums.length - 1;
            while (j >= 0 && nums[j] <= nums[i]) {
                j--;
            }
            swap(nums, i, j);
        }
        reverse(nums, i + 1);
    }

    private void reverse(int[] nums, int start) {
        int i = start, j = nums.length - 1;
        while (i < j) {
            swap(nums, i, j);
            i++;
            j--;
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
链接：https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-by-leetcode/
'''
'''
注意画图理解
1.从右侧遍历先找到右边第一个连续的数字a[i],a[i-1] 他们满足a[i] > a[i-1],此时i右边的数字都已经是降序了
2.这个时候需要对包括i的所有右侧进行重新排序，这个时候就相当于找到一个新的排头兵，这个排头兵应该是i从右侧遍历比i大的第一个数
3.其实就相当于找到i右边从右侧开始遍历的第一个比i大的数作为新的排头兵，交换两个位置，然后反转index为i的右侧部分即可
2.交换这两个数，然后反转i右侧的部分即可
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_index = -1
        n = len(nums)
        # reverse函数 反转i到j之间的元素
        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        # 从后往前遍历 找到first_index
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                first_index = i
                break
        # 如果遍历完都没有找见这个index，就直接反转全部元素
        if first_index == -1:
            reverse(nums, 0, n-1)
            return
        second_index = -1
        # 再次从后往前遍历整个元素，找见第一个比first_index的元素，然后交换两个元素
        for i in range(n - 1, first_index, -1):
            if nums[first_index] < nums[i]:
                second_index = i
                break
        nums[first_index], nums[second_index] = nums[second_index], nums[first_index]
        # 最后记得反转first_index之后的元素
        reverse(nums, first_index + 1, n - 1)