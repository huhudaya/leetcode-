'''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。
说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''


# 快慢指针
class Solution:
    def removeDuplicates(self, nums) -> int:
        # 利用快慢指针
        slow = 0
        fast = 1
        length = len(nums)
        if length < 2:
            return length
        # for i in range(length - 1):
        #     if nums[fast] != nums[slow]:
        #         slow += 1
        #         nums[slow] = nums[fast]
        #     fast += 1
        # fast 走到头就停止
        for fast in range(1, length):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1


class Solution:
    def removeDuplicates(self, nums) -> int:
        # 定义为写指针
        slow = 0
        K = 1
        for num in nums:
            if slow < K or num != nums[slow - K]:
                nums[slow] = num
                slow += 1
        return slow
