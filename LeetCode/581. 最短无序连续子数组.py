'''
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

示例 1:

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
说明 :

输入的数组长度范围在 [1, 10,000]。
输入的数组可能包含重复元素 ，所以升序的意思是<=
'''
from typing import List
# 排序
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        while left <= right and nums[left] == sort_nums[left]:
            left += 1
        while left <= right and nums[right] == sort_nums[right]:
            right -= 1
        return right - left + 1

# 双指针
'''
分别从最左和最有开始，找到两边的逆序对，并停下来；
此时数组分为三部分：
[0,left) //有序
[left,right] //无序
(right,len-1] //有序
然后，在中间[left,right]这一段，找到最大值和最小值。
最后，从start=left-1和end=right+1开始，分别向两边拓展，拓展规则如下：
如果 nums[start] > min, 则start--;
如果 nums[end] < max, 则end++;
执行完以上步骤后，start和end之间（不包括start和end），就是需要排序的最小子数组。
'''
# 主要思路是找见最后逆序的位置，比如[1,3,2,2,2]
# java
'''
class Solution {
    public int findUnsortedSubarray(int[] nums) {
        //初始化双指针
        int left = 0, right = nums.length - 1;
        while (left < nums.length - 1 && nums[left] <= nums[left + 1]) left++;//持续右移
        while (right > 0 && nums[right] >= nums[right - 1]) right--;//持续左移
        //如果出现这种情况，表示数组本身就是有序的，不需要排序
        if (left >= right) return 0;
        //开始寻找中间一段最大值和最小值
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        for (int i = left; i <= right; i++) {
            min = Math.min(min, nums[i]);
            max = Math.max(max, nums[i]);
        }
        //准备向两边扩散
        int start = left - 1, end = right + 1;
        while (start >= 0 && nums[start] > min) start--;//向左扩散
        while (end < nums.length && nums[end] < max) end++;//向右扩散
        //整个数组的最小值和最大值都在中间一段，所以整个数组都要排序
        if (start <= -1 && end >= nums.length){
            return nums.length;
        }
        //只有最大值在中间一段
        if (start <= -1) return end;
        //只有最小值在中间一段
        if (end >= nums.length) return nums.length - start - 1;
        //最大值和最小值都不在中间一段，换句话说，最大值和最小值已分别在左右两段有序的部分
        return end - start - 1;
    }
}
'''
# go
'''
func findUnsortedSubarray(nums []int) int {
	ret := 0
	left, right := -1, -1
	min, max := math.MaxInt64, math.MinInt64
	for i := 0; i < len(nums); i++ {
		//如果是递增数组，nums[i]>=max(nums[0,...,i-1])
		if nums[i] >= max {
			max = nums[i]
		} else {
			//持续更新最右
			right = i
		}
	}
	for i := len(nums) - 1; i >= 0; i-- {
		//如果是递增数组，nums[i]<=min(nums[i,...,len])
		if nums[i] <= min {
			min = nums[i]
		} else {
			//持续更新最左
			left = i
		}
	}
	if right > left {
		ret = right - left + 1
	}
	return ret
}
'''
'''
func findUnsortedSubarray(nums []int) int {
	l, r := 0, len(nums)-1
	for l < len(nums)-1 && nums[l] <= nums[l+1] { // 排好序的左边界
		l++
	}
	for r > 0 && nums[r] >= nums[r-1] { // 排好序的有右边界
		r--
	}
	if l >= r { // 表明是顺序的
		return 0
	}
	down, up := getBorder(nums, l, r) // 获取乱序子数组上下边界
	// 在排好序的左右数组中，对l和r的区域进行扩大
	for l > 0 {
		if nums[l-1] > down {
			l--
		} else {
			break
		}
	}
	for r < len(nums)-1 {
		if nums[r+1] < up {
			r++
		} else {
			break
		}
	}
	return r - l + 1
}

func getBorder(nums []int, l, r int) (int, int) {
	max, min := nums[l], nums[l]
	for i := l; i <= r; i++ {
		if nums[i] > max {
			max = nums[i]
		}
		if nums[i] < min {
			min = nums[i]
		}
	}
	return min, max
}
'''

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1
        # print(left, right)
        # 此时有序
        if left >= right:
            return 0
        min_num = min(nums[left:right + 1])
        max_num = max(nums[left:right + 1])
        start = left - 1
        end = right + 1
        # 向两边扩散找到最远边界
        while start >= 0 and nums[start] > min_num:
            start -= 1
        while end < n and nums[end] < max_num:
            end += 1
        return end - start - 1