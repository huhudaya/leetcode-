'''
作者：星__尘
链接：https://www.nowcoder.com/discuss/428158?source_id=profile_create&channel=2002
来源：牛客网

如果不是排序数组，可以使用hashset来保存数字的平方，重复就存不进去，那么最后就可以直接返回set的大小size即可。
时间空间复杂度都是O（n)。
双指针遍历：这里是排序数组，既然有重复，肯定是有负数，0,1这些数字。
平方后两头大，中间小，可以用首尾指针共同向中间扫描，扫描时去掉重复元素，同时用一个sum来记录有多少个不同数字。
时间复杂度O(N)，空间复杂度O(1)。

'''

# Java
'''
作者：星__尘
链接：https://www.nowcoder.com/discuss/428158?source_id=profile_create&channel=2002
来源：牛客网
public class Solution {
    public int diffSquareNum(int nums[]) {
        int n = nums.length;
        if(n == 0 || nums == null){
            return 0;
        }
        int sum = 0;
        int left = 0;
        int right = n - 1;
        while(left <= right){
            if(nums[left] + nums[right] == 0){
                sum++;
                int temp = nums[left];
                //这里开始去掉后面重复的数字
                while(left <= right && nums[left] == temp)
                    left++;
                while(left <= right && nums[right] == -temp)
                    right--;
            }
            else if(nums[left] + nums[right] < 0){
                sum++;
                int temp = nums[left];
                // 说明left对应的值需要再大一点
                while(left <= right && nums[left] == temp)
                    left++;
            }
            else {
                sum++;
                int temp = nums[right];
                // 说明right对应的值需要小一点
                while(left <= right && nums[right] == temp)
                    right--;
            }
        }
        return sum;
    }
}
'''