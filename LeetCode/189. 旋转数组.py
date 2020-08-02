'''
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。
'''
'''
三次反转
对于[1,2,3,4,5,6,7][1,2,3,4,5,6,7]，
根据k=k%n，将数组分为两段：

第一段，对应数组下标范围[0,n-k-1][0,n−k−1]段，即[1,2,3,4][1,2,3,4]
第二段，对应数组下标范围[n-k,n-1][n−k,n−1]，即[5,6,7][5,6,7]
分为三步：

反转第一段，[4,3,2,1,5,6,7]
反转第二段，[4,3,2,1,7,6,5]
反转整体，[5,6,7,1,2,3,4]
完成！

复杂度分析
时间复杂度：O(N)
空间复杂度：O(1)
'''

# 三次反转 三次旋转
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def swap(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        n = len(nums)
        k = k % n
        swap(0, n - k - 1)
        swap(n - k, n - 1)
        swap(0, n - 1)
        return nums



# java
'''
class Solution {
    public void rotate(int[] nums, int k) {
       int len  = nums.length;
       k = k % len;
       int count = 0;         // 记录交换位置的次数，n个同学一共需要换n次
        for(int start = 0; count < len; start++) {
            int cur = start;       // 从0位置开始换位子
            int pre = nums[cur];   
            do{
                int next = (cur + k) % len;
                int temp = nums[next];    // 来到角落...
                nums[next] = pre;
                pre = temp;
                cur = next;
                count++;
            }while(start != cur)  ;     // 循环暂停，回到起始位置，角落无人
             
        }   
    }  
}
'''