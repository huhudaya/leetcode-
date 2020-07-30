# 027. 移除元素.py
'''
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:

给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,1,2,2,3,0,4,2], val = 2,

函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素。
说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
int len = removeElement(nums, val);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

链接：https://leetcode-cn.com/problems/remove-element
'''
# 快慢指针
'''
public int removeElement(int[] nums, int val) {
    int i = 0;
    for (int j = 0; j < nums.length; j++) {
        if (nums[j] != val) {
            nums[i] = nums[j];
            i++;
        }
    }
    return i;
}
时间复杂度：O(n)
假设数组总共有 n 个元素，i 和 j 至少遍历 2n 步。

空间复杂度：O(1)。
'''

#
'''
时间复杂度：O(n)，i 和 n 最多遍历 n 步。
不用一直赋值操作，效率更高
在这个方法中，赋值操作的次数等于要删除的元素的数量。因此，如果要移除的元素很少，效率会更高。

空间复杂度：O(1)

public int removeElement(int[] nums, int val) {
    int i = 0;
    int n = nums.length;
    while (i < n) {
        if (nums[i] == val) {
        	//将最后一位换到要删除的数组这里，然后判断
            nums[i] = nums[n - 1];
            // reduce array size by one
            n--;
        } else {
            i++;
        }
    }
    return n;
}
'''

# 优化
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 双指针
        left = 0
        n = len(nums)
        while left < n:
            if nums[left] == val:
                nums[left] = nums[n - 1]
                n -= 1
            else:
                left += 1
        return n


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 双指针
        n = len(nums)
        slow = 0
        for i in range(n):
            if nums[i] != val:
                nums[slow] = nums[i]
                slow += 1
        return slow


'''
public int removeElement(int[] nums, int val) {
    int i = 0;
    for (int j = 0; j < nums.length; j++) {
        if (nums[j] != val) {
            nums[i] = nums[j];
            i++;
        }
    }
    return i;
}
'''
