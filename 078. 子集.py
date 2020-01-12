'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

'''
位运算
集合的每个元素，都有可以选或不选，用二进制和位运算，可以很好的表示。

Java
    public static List<List<Integer>> binaryBit(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        for (int i = 0; i < (1 << nums.length); i++) {
            List<Integer> sub = new ArrayList<Integer>();
            for (int j = 0; j < nums.length; j++)
                if (((i >> j) & 1) == 1) sub.add(nums[j]);
            res.add(sub);
        }
        return res;
    }

逐个枚举，空集的幂集只有空集，每增加一个元素，让之前幂集中的每个集合，追加这个元素，就是新增的子集。

Java
    /**
     * 循环枚举
     */
    public static List<List<Integer>> enumerate(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        res.add(new ArrayList<Integer>());
        for (Integer n : nums) {
            int size = res.size();
            for (int i = 0; i < size; i++) {
                List<Integer> newSub = new ArrayList<Integer>(res.get(i));
                newSub.add(n);
                res.add(newSub);
            }
        }
        return res;
    }

    /**
     * 递归枚举
     */
    public static void recursion(int[] nums, int i, List<List<Integer>> res) {
        if (i >= nums.length) return;
        int size = res.size();
        for (int j = 0; j < size; j++) {
            List<Integer> newSub = new ArrayList<Integer>(res.get(j));
            newSub.add(nums[i]);
            res.add(newSub);
        }
        recursion(nums, i + 1, res);
    }

思路：
集合中每个元素的选和不选，构成了一个满二叉状态树，比如，左子树是不选，右子树是选，从根节点、到叶子节点的所有路径，构成了所有子集。可以有前序、中序、后序的不同写法，结果的顺序不一样。本质上，其实是比较完整的中序遍历。
    /**
     * DFS，前序遍历
     */
    public static void preOrder(int[] nums, int i, ArrayList<Integer> subset, List<List<Integer>> res) {
        if (i >= nums.length) return;
        // 到了新的状态，记录新的路径，要重新拷贝一份
        subset = new ArrayList<Integer>(subset);

        // 这里
        res.add(subset);
        preOrder(nums, i + 1, subset, res);
        subset.add(nums[i]);
        preOrder(nums, i + 1, subset, res);
    }

    /**
     * DFS，中序遍历
     */
    public static void inOrder(int[] nums, int i, ArrayList<Integer> subset, List<List<Integer>> res) {
        if (i >= nums.length) return;
        subset = new ArrayList<Integer>(subset);

        inOrder(nums, i + 1, subset, res);
        subset.add(nums[i]);
        // 这里
        res.add(subset);
        inOrder(nums, i + 1, subset, res);
    }

    /**
     * DFS，后序遍历
     */
    public static void postOrder(int[] nums, int i, ArrayList<Integer> subset, List<List<Integer>> res) {
        if (i >= nums.length) return;
        subset = new ArrayList<Integer>(subset);

        postOrder(nums, i + 1, subset, res);
        subset.add(nums[i]);
        postOrder(nums, i + 1, subset, res);
        // 这里
        res.add(subset);
    }
回溯:
    public static void backtrack(int[] nums, int i, List<Integer> sub, List<List<Integer>> res) {
        for (int j = i; j < nums.length; j++) {
            if (j > i && nums[j] == nums[j - 1]) continue;
            sub.add(nums[j]);
            res.add(new ArrayList<Integer>(sub));
            backtrack(nums, j + 1, sub, res);
            sub.remove(sub.size() - 1);
        }
    }
'''


'''-----------------------------容易理解版本
# 回溯法一:在回溯的过程中记录结点
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size == 0:
            return []

        res = []
        self.__dfs(nums, 0, [], res)
        return res

    def __dfs(self, nums, start, path, res):
        # 每次遍历的时候都添加到res中
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            # 因为 nums 不包含重复元素，并且每一个元素只能使用一次
            # 所以下一次搜索从 i + 1 开始
            self.__dfs(nums, i + 1, path, res)
            path.pop()


参考代码 2：在回溯的过程中记录深度。
PythonJava
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size == 0
                    return []    
        res = []
        for i in range(size + 1):
            self.__dfs(nums, i, 0, [], res)
        return res

    def __dfs(self, nums, depth, begin, path, res):
        # 深度等于 path 长度的时候递归终止
        if len(path) == depth:
            res.append(path[:])
            return

        # 按顺序来的，所以不用设置 used 数组
        for i in range(begin, len(nums)):
            path.append(nums[i])
            print(path)
            self.__dfs(nums, depth, i + 1, path, res)
            path.pop()
'''



# 回溯法：
'''
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/**
 * @author liweiwei1419
 * @date 2019/10/30 5:26 下午
 */
public class Solution8 {

         public List<List<Integerm>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        int len = nums.length;
        if (len == 0) {
            return res;
        }
        Stack<Integer> stack = new Stack<>();
        dfs(nums, 0, len, stack, res);
        return res;
    }

    private void dfs(int[] nums, int index, int len,
                     Stack<Integer> stack, List<List<Integer>> res) {
        if (index == len) {
            res.add(new ArrayList<>(stack));
            return;
        }
        // 当前数可选，也可以不选

        // 不选，直接进入下一层
        dfs(nums, index + 1, len, stack, res);

        // 选了，进入下一层
        stack.add(nums[index]);
        dfs(nums, index + 1, len, stack, res);
        stack.pop();
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        Solution8 solution7 = new Solution8();
        List<List<Integer>> subsets = solution7.subsets(nums);
        System.out.println(subsets);
    }
}

'''
class Solution:
    def subsets(self, nums):        
        if not nums:
            return []
        res = []
        n = len(nums)
        def helper(idx, temp_list):
            res.append(temp_list)
            for i in range(idx, n):
                helper(i + 1, temp_list + [nums[i]])
        helper(0, [])
        return res

