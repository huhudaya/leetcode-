'''
给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。
现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数
要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
说明: 请尽可能地优化你算法的时间和空间复杂度。

示例 1:

输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]
示例 2:

输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]
示例 3:

输入:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
输出:
[9, 8, 9]
'''

# 单调栈 min栈
class Solution:
    def maxNumber(self, nums1, nums2, k):

        def pick_max(nums, k):
            stack = []
            drop = len(nums) - k
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(A, B):
            ans = []
            while A or B:
                bigger = A if A > B else B
                ans.append(bigger[0])
                bigger.pop(0)
            return ans

        return max(merge(pick_max(nums1, i), pick_max(nums2, k-i)) for i in range(k+1) if i <= len(nums1) and k-i <= len(nums2))

#自己的版本
from typing import List
from collections import deque
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m = len(nums1)
        n = len(nums2)
        def pick_max(nums, k):
            stack = []
            n = len(nums)
            cnt = n - k
            for num in nums:
                # 维护一个max单调栈
                while cnt and stack and stack[-1] < num:
                    stack.pop()
                    cnt -= 1
                stack.append(num)
            return deque(stack[:k])
        def merge(nums1, nums2):
            res = []
            while nums1 or nums2:
                if nums1 > nums2:
                    res.append(nums1.popleft())
                else:
                    res.append(nums2.popleft())
            return res

        res = []
        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                res = max(res, merge(pick_max(nums1, i), pick_max(nums2, k - i)))
        return res
Solution().maxNumber([6,7],[6,0,4],5)



# java
'''
class Solution {
    /**
     * 最大数来源于 nums1长度为s的子序列 和num2长度为k - s的子序列
     * 反证法可得 最大数来源于 nums1长度为s的最大子序列 和num2长度为k - s的最大子序列
     * 按最大值合并两个子序列， 即为结果
     * 时间复杂度 ： O(k * max(n, k) )
     */
    public int[] maxNumber(int[] nums1, int[] nums2, int k) {
        int[] ans = new int[k];
        if(nums1.length + nums2.length < k) return ans;
        for(int s = Math.max(k - nums2.length, 0); s <= Math.min(nums1.length , k); s++){
            List<Integer> l1 = getKLargestNumber(nums1, s);   //O(n1)
            List<Integer> l2 = getKLargestNumber(nums2, k - s);  //O(n2)
            int[] merge = merge(l1, l2);    //O(k)
            if(isBigger(merge, ans)) ans = merge;  //O(k)
        }
        return ans;
    }

    //获取长度为k的最大子序列
    public List<Integer> getKLargestNumber(int[] nums, int k){
        int n = nums.length;
        int popCnt = n - k;
        List<Integer> res = new ArrayList<>();
        if(k == 0)  return res;
        for(int i = 0; i < n; i++){
            while(!res.isEmpty() && res.get(res.size() - 1) < nums[i] && popCnt > 0){
                res.remove(res.size() - 1);
                popCnt--;
            }
            if(res.size() < k) res.add(nums[i]);
            else popCnt--;  //注意， 这里容易漏了， 如果没有添加到数组， pop--
        }
        return res;
    }

    //合并两个有序子序列， 成为一个最大值
    public int[] merge(List<Integer> l1, List<Integer> l2){
        int[] res = new int[l1.size() + l2.size()];
        int l = 0, r = 0, idx = 0;
        // StringBuilder sb1 = new StringBuilder();
        // StringBuilder sb2 = new StringBuilder();
        // for(int i = l; i < l1.size(); i++) sb1.append(l1.get(i));
        // for(int i = r; i < l2.size(); i++) sb2.append(l2.get(i));
        // String a = sb1.toString();
        // String b = sb2.toString();
        
        String a = String.join('', l1);
        String b = String.join('', l2);
        while (l < l1.size() || r < l2.size()){
            if(l >= l1.size()) res[idx++] = l2.get(r++);
            else if(r >= l2.size()) res[idx++] = l1.get(l++);
            else if(a.substring(l, l1.size()).compareTo(b.substring(r, l2.size())) >= 0){
                res[idx++] = l1.get(l++);
            }else{
                res[idx++] = l2.get(r++);
            }
        }
        return res;
    }

    //前面的数是否大于后面的数
    public boolean isBigger(int[] list, int[] ans){
        if(ans.length == 0) return true;
        for(int i = 0; i < list.length; i++){
            if(list[i] > ans[i]) return true;
            else if(list[i] < ans[i]) return false;
        }
        return false;
    }
}
'''


'''
class Solution {
    public int[] maxNumber(int[] nums1, int[] nums2, int k) {
        if(nums1.length + nums2.length<k) return new int[0];
        int[] res=new int[k];
        for(int i = 0; i <= Math.min(nums1.length, k); ++i)
        {
            if(k - i > nums2.length) continue;
            int[] arr1=new int[i];
            int[] arr2=new int[k-i];
            Deque<Integer> dq1 = new ArrayDeque<>();
            Deque<Integer> dq2 = new ArrayDeque<>();
            for(int j = 0; j < nums1.length; ++j)
            {
                if(dq1.isEmpty() || dq1.peek() >= nums1[j]) {
                    dq1.push(nums1[j]);
                    continue;
                }
                while(nums1.length - 1 - j + dq1.size() >= i && !dq1.isEmpty() && dq1.peek() < nums1[j]) dq1.pop();
                dq1.push(nums1[j]);
            }
            for(int j = 0; j < i; ++j) arr1[j]=dq1.removeLast();
            for(int j = 0; j < nums2.length; ++j)
            {
                if(dq2.isEmpty() || dq2.peek() >= nums2[j]) {
                    dq2.push(nums2[j]);
                    continue;
                }
                while(nums2.length - 1 - j + dq2.size() >= k-i && !dq2.isEmpty() && dq2.peek() < nums2[j]) dq2.pop();
                dq2.push(nums2[j]);
            }
            for(int j = 0; j < k - i; ++j) arr2[j] = dq2.removeLast();
            int[] temp = merge(arr1, arr2);
            for(int j = 0; j < k; ++j) 
            {
                if(res[j] < temp[j]) {
                    res = temp;
                    break;
                }
                else if(res[j] > temp[j]) break;
            }
        }
        return res;
    }

    private int[] merge(int[] arr1, int[] arr2) {
        if(arr1.length==0) return arr2;
        if(arr2.length==0) return arr1;
        int[] res=new int[arr1.length + arr2.length];
        int i1=0,i2=0;
        for(int i = 0; i < res.length; ++i)
        {
            if(compare(Arrays.copyOfRange(arr1, i1, arr1.length), Arrays.copyOfRange(arr2, i2, arr2.length))){
                res[i] = arr1[i1++];
            }
            else{
                res[i] = arr2[i2++];
            }
        }
        return res;
    }

      private boolean compare(int[] nums1, int[] nums2){
        int n = Math.min(nums1.length, nums2.length);
        for(int i = 0; i < n; i++){
            if(nums1[i] > nums2[i]) return true;
            else if(nums1[i] < nums2[i]) return false;
            else continue;
        }
        return nums1.length > nums2.length;
    }
}
'''