# 496. 下一个更大元素 I.py
'''
给定两个没有重复元素的数组 nums1 和 nums2
其中nums1 是 nums2 的子集。
找到 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。

示例 1:

输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释: 注意必须是右边
    对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
    对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
    对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
示例 2:

输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]
解释:
    对于num1中的数字2，第二个数组中的下一个较大数字是3。
    对于num1中的数字4，第二个数组中没有下一个更大的数字，因此输出 -1。
注意:

nums1和nums2中所有元素是唯一的。
nums1和nums2 的数组大小都不超过1000

'''

'''
这道题的暴力解法很好想到，就是对每个元素后面都进行扫描，找到第一个更大的元素就行了。但是暴力解法的时间复杂度是 O(n^2)。

这个问题可以这样抽象思考：把数组的元素想象成并列站立的人
元素大小想象成人的身高。这些人面对你站成一列
如何求元素「2」的 Next Greater Number 呢？
很简单，如果能够看到元素「2」，那么他后面可见的第一个人就是「2」的 Next Greater Number
因为比「2」小的元素身高不够，都被「2」挡住了，第一个露出来的就是答案。
'''
# 模板
'''
倒着遍历  使用这种方法的好处是不用使用dict这种hahsMap的结构了，更省内存!
vector<int> nextGreaterElement(vector<int>& nums) {
    vector<int> ans(nums.size()); // 存放答案的数组
    stack<int> s;
    for (int i = nums.size() - 1; i >= 0; i--) { // 倒着往栈里放
        while (!s.empty() && s.top() <= nums[i]) { // 判定个子高矮
            s.pop(); // 矮个起开，反正也被挡着了。。。
        }
        ans[i] = s.empty() ? -1 : s.top(); // 这个元素身后的第一个高个
        s.push(nums[i]); // 进队，接受之后的身高判定吧！
    }
    return ans;
}
顺着遍历
public class Solution {
    public int[] nextGreaterElement(int[] findNums, int[] nums) {
        Stack < Integer > stack = new Stack < > ();
        HashMap < Integer, Integer > map = new HashMap < > ();
        int[] res = new int[findNums.length];
        for (int i = 0; i < nums.length; i++) {
            //其实也相当于维护了一个max栈，即栈底是max
            while (!stack.empty() && nums[i] > stack.peek())
                map.put(stack.pop(), nums[i]);
            stack.push(nums[i]);
        }
        # 区别于下面的那种方法，这种方法在最后的时候需要弹出栈中所有的值，然后放入map并且置value是-1
        while (!stack.empty())
            map.put(stack.pop(), -1);
        for (int i = 0; i < findNums.length; i++) {
            res[i] = map.get(findNums[i]);
        }
        return res;
    }
}
'''
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, hashmap = list(), dict()
        for i in nums2:
            # 其实相当于维护一个双端队列qmax，只不过在弹出值得时候加到hahsMap中 max栈
            while len(stack) != 0 and stack[-1] < i:
                hashmap[stack.pop()] = i
            stack.append(i)
        # 因为无重复数据
        return [hashmap.get(i, -1) for i in nums1]


'''
这就是单调队列解决问题的模板。for 循环要从后往前扫描元素
因为我们借助的是栈的结构，倒着入栈
其实是正着出栈。while 循环是把两个“高个”元素之间的元素排除，因为他们的存在没有意义
前面挡着个“更高”的元素，所以他们不可能被作为后续进来的元素的 Next Great Number 了。

这个算法的时间复杂度不是那么直观
如果你看到 for 循环嵌套 while 循环，可能认为这个算法的复杂度也是 O(n^2)
但是实际上这个算法的复杂度只有 O(n)。

分析它的时间复杂度
要从整体来看：总共有 n 个元素，每个元素都被 push 入栈了一次，而最多会被 pop 一次
没有任何冗余操作。所以总的计算规模是和元素规模 n 成正比的，也就是 O(n) 的复杂度
这道题一个思路：
'''
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 使用单调栈
        # 倒着遍历，为啥要倒着遍历，倒着遍历的好处是什么？
        # 我们当然可以顺着遍历，而且代码可读性更好，更容易理解，
        # 之所以选择倒着遍历是由于这样可以不使用hashmap，而只使用一个数组即可存放记录，节省空间
        m = len(nums1)
        n = len(nums2)
        res = {}
        stack = []
        ans = []
        for i in range(n - 1, -1, -1):
            # 维护一个 max 栈
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
                # res[i] =  stack[-1] if len(stack) != 0 else -1
            # res[i] = stack[-1] if stack else -1
            res[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])
        for i in range(m):
            ans.append(res.get(nums1[i]))
        return ans
