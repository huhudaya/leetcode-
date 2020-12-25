'''
给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。

请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。

示例 1：

输入：nums = [2,5,1,3,4,7], n = 3
输出：[2,3,5,4,1,7]
解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，所以答案为 [2,3,5,4,1,7]
示例 2：

输入：nums = [1,2,3,4,4,3,2,1], n = 4
输出：[1,4,2,3,3,2,4,1]
示例 3：

输入：nums = [1,1,2,2], n = 2
输出：[1,2,1,2]
 

提示：

1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3
'''

# 注意到题目的限制，每个元素的值都是正数！
# 观察可知一个性质：getDesireIdx = lambda i: i * 2 if i < n else (i - n) * 2 + 1
'''
1.通过in-place swap的方法做到O(1)空间O(n)时间。
2.每个"nums[i]"都有一个“目标”index。例如对于8个数的nums, "nums[0]"想去"0", "nums[4]"想去"1", "nums[1]"想去"2", "nums[5]"想去"3", "nums[2]"想去"4"...
3.in-place把nums[i] swap到它想去的index，把swap走的数标记为负数，并把swap回来的数继续"原地"swap出去
  直到swap回来的数的目标index就是“i”自己，然后才增加"i"并继续过下一个“i”。
4.遇到nums[i]是负数就说明nums[i]已经在之前的swap中到达了目前位置，因此跳过。
5.所有的i都过好后nums就是正确的顺序，别忘了最后再过一遍把所有的负数变回正数。
6.由于每个nums[i]只会被标记1次负数，因此时间复杂度是O(n)
'''

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        getDesIndex = lambda i: i * 2 if i < n else (i - n) * 2 + 1
        for i in range(2 * n):
            j = i
            # 这里的while循环就是为了将num[i]换到应该在的位置上
            while nums[i] >= 0:
                j = getDesIndex(j)
                # 负数代表着已经换到了应该的位置上
                nums[i], nums[j] = nums[j], -nums[i]
        for i in range(2 * n):
            nums[i] = -nums[i]
        return nums


# Java
'''
public int[] shuffle(int[] nums, int n) {
        int [] ret = new int[2 * n];
        for(int i=0; i<n; i++){
            ret[i * 2] = nums[i];
            ret[i * 2 + 1] = nums[n + i];
        }
        return ret;
}
'''

# go
'''
func shuffle(nums []int, n int) []int {
    var(
        index_x = 1
        temp = 0
    )
    for k := 0; k < n; k++ {
        for i := n + k; i > index_x; i-- {
            temp = nums[i]
            nums[i] = nums[i-1]
            nums[i-1] = temp
        }
        index_x += 2
    }
    return nums
}
'''

# java
'''
    public int[] shuffle(int[] nums, int n) {
        Function<Integer, Integer> fun = i -> i < n ? 2 * i : (i - n) * 2 + 1;
        for (int i = 0; i < 2 * n; i++) {
            int j = i;
            while (nums[i] >= 0) {
                j = fun.apply(j);
                int tmp = nums[i]; nums[i] = nums[j]; nums[j] = -tmp;
            }
        }
        for (int i = 0; i < 2 * n; i++) {
            nums[i] = -nums[i];
        }
        return nums;
    }
'''