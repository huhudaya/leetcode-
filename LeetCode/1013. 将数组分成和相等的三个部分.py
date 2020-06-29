'''

给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。

形式上，如果可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。



示例 1：

输出：[0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
示例 2：

输入：[0,2,1,-6,6,7,9,-1,2,0,1]
输出：false
示例 3：

输入：[3,3,6,5,-2,2,5,1,-9,4]
输出：true
解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4


提示：

3 <= A.length <= 50000
-10^4 <= A[i] <= 10^4
'''
# 官方解
from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 != 0:
            return False
        target = s // 3
        n, i, cur = len(A), 0, 0
        while i < n:
            cur += A[i]
            if cur == target:
                break
            i += 1
        if cur != target:
            return False
        j = i + 1
        while j + 1 < n:  # 需要满足最后一个数组非空
            cur += A[j]
            if cur == target * 2:
                return True
            j += 1
        return False


'''
双指针
数组元素的总和 sum 不是3的倍数，直接返回false
使用双指针left，right, 从数组两头开始一起找，节约时间
当 left + 1 < right 的约束下，可以找到数组两头的和都是 sum/3,那么中间剩下的元素和就一定也是sum/3
（left + 1 < right的约束就是要中间有剩下的元素，使用left < right的约束，数组可能可以恰好被划分成两部分，中间没有元素）
'''
'''
class Solution {
    public boolean canThreePartsEqualSum(int[] A) {
        int sum = 0;
        for(int i : A){
            sum += i;
        }
        if(sum%3 != 0){
            // 总和不是3的倍数，直接返回false
            return false;
        }

        // 使用双指针,从数组两头开始一起找，节约时间
        int left = 0;
        int leftSum = A[left];
        int right = A.length - 1;
        int rightSum = A[right];

        // 使用left + 1 < right 的原因，防止只能将数组分成两个部分
        // 例如：[1,-1,1,-1]，使用left < right作为判断条件就会出错
        while(left + 1 < right){
            if(leftSum == sum/3 && rightSum == sum/3){
                // 左右两边都等于 sum/3 ，中间也一定等于
                return true;
            }
            if(leftSum != sum/3){
                // left = 0赋予了初值，应该先left++，在leftSum += A[left];
                leftSum += A[++left];
            }
            if(rightSum != sum/3){
                // right = A.length - 1 赋予了初值，应该先right--，在rightSum += A[right];
                rightSum += A[--right];
            }
        }
        return false;  
    }
}
'''

# 直接找
'''
class Solution {
    public boolean canThreePartsEqualSum(int[] A) {
        int sum = 0;
        for(int i: A){
            sum += i;
        }
        if(sum%3 != 0){
            // 总和不是3的倍数，直接返回false
            return false;
        }
        int s = 0;
        int flag = 0;
        for(int i:A){
            s += i;
            if(s == sum/3){
                flag++;
                s = 0;
            }
        }
        // flag不一定等于3，例如[1,-1,1,-1,1,-1,1,-1]
        return flag >= 3;
    }
}
'''

'''
答疑
疑问一：

评论区好多人对 count == 3 有疑问， count == 3 之后还没有遍历完数组，怎么就能判断为 true 了？

解答：

首先 count == 3 就说明找到了三个和为 sum / 3 的子数组，那剩下元素的和就只能为 0 了，把它们合并到最后一个子数组就 OK 啦。

疑问二：

那 count == 2 不就可以返回 true 了吗？ 因为已经找到了两个和为 sum / 3 的子数组，那剩下的不就是第三个了嘛！

解答：

其实不是这样的，因为找到了两个子数组后可能恰好到达了数组末尾，此时就不符合要求了，例如: [1, -1, 1, -1] .
'''


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        amount = sum(A)
        if amount % 3 != 0:
            return False
        res = amount // 3
        temp, count = 0, 0
        for i in A:
            # 还有剩余元素，已经和为target的有两组了，所以一定可以返回true
            if count == 2:
                return True
            temp += i
            if temp == res:
                count += 1
                temp = 0
        return False
