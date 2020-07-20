'''
一个数据先递增再递减，找出数组不重复的个数，比如 [1, 3, 9, 1]，结果为3，不能使用额外空间，复杂度o(n)
'''
'''
作者：星__尘
链接：https://www.nowcoder.com/discuss/428158?source_id=profile_create&channel=2002
来源：牛客网

public class Solution {
    public int diffnum(int[] nums){
        int n = nums.length;
        if(n == 0 || nums == null){
            return 0;
        }
        int left = 0;
        int right = n - 1;
        int sum = 0;
        while(left <= right){
            if(nums[left] == nums[right]){
                sum++;
                int temp = nums[left];
                while(left <= right && nums[right] == temp)
                    right--;
                while(left <= right && nums[left] == temp)
                    left++;
            }
            else if(nums[left] < nums[right]){
                sum++;
                int temp = nums[left];
                while(left <= right && nums[left] == temp)
                    left++;
            }
            else{
                sum++;
                int temp = nums[right];
                while(left <= right && nums[right] == temp)
                    right--;
            }
        }
        return sum;
    }
}
'''