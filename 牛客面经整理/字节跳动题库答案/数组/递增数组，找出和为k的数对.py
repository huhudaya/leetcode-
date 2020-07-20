'''
作者：星__尘
链接：https://www.nowcoder.com/discuss/428158?source_id=profile_create&channel=2002
来源：牛客网

输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
双指针遍历：用头尾两个指针，分别开始遍历，两个数字和大于k时，右指针向前移动，小于k时左指针向后移动。


public class Solution{
    public ArrayList findPair(int[] nums,int k){
        int n = nums.length;
        int i = 0;
        int j = n - 1;
        ArrayList<Integer> list = new ArrayList<>();
        while(i < j){
            if(nums[i] + nums[j] < k){
                i++;
            }else if(num[i] + nums[j] > k){
                j--;
            }else{
                list.add(nums[i]);
                list.add(nums[j]);
            }
        }
        return list;
    }
}
'''
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 因为已经排好序，直接双指针
        n = len(nums)
        left = 0
        right = n - 1
        res = []
        # 最大值都比target小，剪枝
        right_max = nums[right] + nums[right - 1]
        if right_max < target:
            return res
        while left < right:
            tmp = nums[left] + nums[right]
            if tmp == target:
                return [nums[left], nums[right]]
            elif tmp < target:
                left += 1
            else:
                right -= 1
        return res