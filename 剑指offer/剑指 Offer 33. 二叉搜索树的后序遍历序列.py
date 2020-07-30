'''

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：
输入: [1,6,3,2,5]
输出: false

示例 2：
输入: [1,3,2,6,5]
输出: true
提示：
数组长度 <= 1000
'''
'''
BST的后序序列的合法序列是:
后序遍历的特点是最后一个元素是根节点
对于一个序列S，最后一个元素是x （也就是根），如果去掉最后一个元素的序列为T
那么T满足：T可以分成两段，前一段（左子树）小于x，后一段（右子树）大于x
且这两段（子树）都是合法的后序序列。完美的递归定义 : ) 。
'''


class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j:
                return True
            p = i
            # 核心思路是找见第一个大于等于最后一个元素的索引！！！！！！
            while postorder[p] < postorder[j]:
                p += 1
            m = p
            while postorder[p] > postorder[j]:
                p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)


'''
class Solution {
    bool judge(vector<int>& a, int l, int r){
        if(l >= r) return true;
        int i = r;
        while(i > l && a[i - 1] > a[r]) --i;
        for(int j = i - 1; j >= l; --j) if(a[j] > a[r]) return false;
        return judge(a, l, i - 1) && (judge(a, i, r - 1));
    }
public:
    bool VerifySquenceOfBST(vector<int> a) {
        if(!a.size()) return false;
        return judge(a, 0, a.size() - 1);
    }
};
'''

# 单调栈 重要思想，倒着遍历
# 重点思想就是当弹出栈的时候，更新一下当前的root节点，同时节点不能大于root节点的值
'''
时间复杂度 O(N) ： 遍历 postorderpostorder 所有节点，各节点均入栈 / 出栈一次，使用 O(N) 时间。
空间复杂度 O(N) ： 最差情况下，单调栈 stackstack 存储所有节点，使用 O(N) 额外空间。
'''

# 后序遍历倒序： [ 根节点 | 右子树 | 左子树 ] 。
# 类似 先序遍历的镜像 ，即先序遍历为 “根、左、右” 的顺序
# 而后序遍历的倒序为 “根、右、左” 顺序。
from typing import List
import sys


# 核心思路就是维护一个min栈，逆序遍历整个数组
# 因为是后序遍历，所以当逆序遍历的时候，数组中的第一个节点是根节点，然后右子树的节点都比根节点的值要大
# 初始化： 单调栈 stackstack ，父节点值 root = +\infinroot=+∞ （初始值为正无穷大，可把树的根节点看为此无穷大节点的左孩子）；
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        # 单调栈
        stack = []
        root = sys.maxsize
        # 逆序遍历整个数组
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root:
                return False
            # 维护单调的min栈
            while stack and postorder[i] < stack[-1]:
                # 这里更新root的值
                root = stack.pop()
            stack.append(postorder[i])
        return True


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:

        def helper(nums):
            if len(nums) <= 1:
                return True
            # 最后一个数为根节点
            root = nums[-1]
            for i in range(len(nums)):
                if nums[i] > root:
                    break
            for j in range(i, len(nums) - 1):
                if nums[j] < root:
                    return False
            return helper(nums[:i]) and helper(nums[i:-1])

        if not postorder:
            return True
        return helper(postorder)
