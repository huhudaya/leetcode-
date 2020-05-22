# 503. 下一个更大元素 II
'''
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。
数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。
如果不存在，则输出 -1。

示例 1:

输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数；
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
类比于SQL中的时间窗口操作，timestamp/n，相当于是每隔n为一个区间

首先，计算机的内存都是线性的，没有真正意义上的环形数组，但是我们可以模拟出环形数组的效果，一般是通过 % 运算符求模（余数），获得环形特效：

int[] arr = {1,2,3,4,5};
int n = arr.length, index = 0;
while (true) {
    print(arr[index % n]);
    index++;
}
回到 Next Greater Number 的问题，增加了环形属性后，问题的难点在于：这个 Next 的意义不仅仅是当前元素的右边了，有可能出现在当前元素的左边（如上例）。

明确问题，问题就已经解决了一半了。我们可以考虑这样的思路：将原始数组 “翻倍”，就是在后面再接一个原始数组，这样的话，按照之前“比身高”的流程，每个元素不仅可以比较自己右边的元素，而且也可以和左边的元素比较了。



怎么实现呢？你当然可以把这个双倍长度的数组构造出来，然后套用算法模板。但是，我们可以不用构造新数组，而是利用循环数组的技巧来模拟。

直接看代码吧：


# 优化版本，加了一个if判断节省时间
因为是倒着遍历的，所以相当于
21243
     21243     <--倒着，先从3开始，通过while i%n来进行循环数组的操作
由于倒着遍历，当遍历到上面一组的尾部3的时候，这个时候就满足我们的循环数组的需求，即求3的后面一个的最大值即4，所以从题意上来看，我们只需要当i<n的时候进行赋值，不用每一个都赋值
C++
vector<int> nextGreaterElements(vector<int>& nums) {
    int n = nums.size();
    vector<int> res(n); // 存放结果
    stack<int> s;
    // 假装这个数组长度翻倍了
    for (int i = 2 * n - 1; i >= 0; i--) {
        while (!s.empty() && s.top() <= nums[i % n])
            s.pop();
        # 加if判断，节省时间
        if(i < n){
            res[i] = s.empty() ? -1 : s.top();
        }
        s.push(nums[i % n]);
    }
    return res;
}

vector<int> nextGreaterElements(vector<int>& nums) {
    int n = nums.size();
    vector<int> res(n); // 存放结果
    stack<int> s;
    // 假装这个数组长度翻倍了
    for (int i = 2 * n - 1; i >= 0; i--) {
        while (!s.empty() && s.top() <= nums[i % n])
            s.pop();
        res[i % n] = s.empty() ? -1 : s.top();
        s.push(nums[i % n]);
    }
    return res;
}

至此，你已经掌握了单调栈的设计方法及代码模板，学会了解决 Next Greater Number，并能够处理循环数组了。
'''
'''
方法一：单调栈
我们可以使用单调栈来解决这个问题。

我们首先把第一个元素 A[1] 放入栈，随后对于第二个元素 A[2]，如果 A[2] > A[1]，那么我们就找到了 A[1] 的下一个更大元素 A[2]，此时就可以把 A[1] 出栈并把 A[2] 入栈；如果 A[2] <= A[1]，我们就仅把 A[2] 入栈。对于第三个元素 A[3]，此时栈中有若干个元素，那么所有比 A[3] 小的元素都找到了下一个更大元素（即 A[3]），因此可以出栈，在这之后，我们将 A[3] 入栈，以此类推。

可以发现，我们维护了一个单调栈，栈中的元素从栈顶到栈底是单调不降的。当我们遇到一个新的元素 A[i] 时，我们判断栈顶元素是否小于 A[i]，如果是，那么栈顶元素的下一个更大元素即为 A[i]，我们将栈顶元素出栈。重复这一操作，直到栈为空或者栈顶元素大于 A[i]。此时我们将 A[i] 入栈，保持栈的单调性，并对接下来的 A[i + 1], A[i + 2] ... 执行同样的操作。

由于这道题的数组是循环数组，因此我们需要将每个元素都入栈两次。这样可能会有元素出栈找过一次，即得到了超过一个“下一个更大元素”，我们只需要保留第一个出栈的结果即可。

下面的动画中给出了一个例子，注意动画中是从右往左加入元素，其原理和上述是类似的。

地址:
https://leetcode-cn.com/problems/next-greater-element-ii/solution/xia-yi-ge-geng-da-yuan-su-ii-by-leetcode/
public class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int[] res = new int[nums.length];
        Stack<Integer> stack = new Stack<>();
        for (int i = 2 * nums.length - 1; i >= 0; --i) {
            while (!stack.empty() && nums[stack.peek()] <= nums[i % nums.length]) {
                stack.pop();
            }
            res[i % nums.length] = stack.empty() ? -1 : nums[stack.peek()];
            stack.push(i % nums.length);
        }
        return res;
    }
}
'''
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        res = [-1] * n

        for i in range(n * 2 - 1, -1, -1):
            while (stack and nums[stack[-1]] <= nums[i % n]):
                stack.pop()
            # 加速
            # if i < n:
            #     res[i % n] = -1 if stack == [] else nums[stack[-1]]
            # stack.append(i % n)
            res[i % n] = -1 if stack == [] else nums[stack[-1]]
            stack.append(i % n)

        return res


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 循环数组，使用i%n表示数组索引，不用复制两个一样的数组
        # 还是单调栈的思路，其实也是双端队列维护qmax的思想，具体可以参考LeetCode生成窗口最大值数组
        n = len(nums)
        res = [0 for i in range(n)]
        stack = []
        # 倒着遍历
        for i in range(n * 2 - 1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            if i < n:
                res[i] = stack[-1] if stack else -1
            stack.append(nums[i % n])
        return res
