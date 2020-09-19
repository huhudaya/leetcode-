'''
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数
并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
'''
from typing import List
from itertools import combinations as com


class Solution:
    # 简约版本
    def combinationSum31(self, k: int, n: int) -> List[List[int]]:
        tmp = list(map(list, list(com(range(1, 10), k))))
        res = []
        for i in tmp:
            if sum(i) == n:
                res.append(i)
        return res

    # 优化版
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [i for i in range(1, 10)]
        size = 9
        res = []

        def dfs(target, path, start):
            if len(path) == k:
                if target == 0:
                    res.append(path[:])
                return
            # len(path)越大,size - (k - len(path)) + 2越大
            # 剪枝
            for i in range(start, size - (k - len(path)) + 2):
                # 下面这两行写不写无所谓
                # if target < i:
                #     break
                path.append(i)
                dfs(target - i, path, i + 1)
                path.pop()

        dfs(n, [], 1)
        return res

    # 未优化版
    def combinationSum32(self, k: int, n: int) -> List[List[int]]:
        candidates = [i for i in range(1, 10)]
        size = 9
        res = []

        def dfs(target, path, start):
            if len(path) == k and target == 0:
                res.append(path[:])
                return
            for i in range(start, size + 1):
                path.append(i)
                dfs(target - i, path, i + 1)
                path.pop()

        dfs(n, [], 1)
        return res



# java
'''
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class Solution {

    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> res = new ArrayList<>();

        // 根据官方对 Stack 的使用建议，这里将 Deque 对象当做 stack 使用
        // 注意只使用关于栈的接口
        Deque<Integer> path = new ArrayDeque<>();
        dfs(k, n, 1, path, res);
        return res;
    }

    /**
     * @param k       剩下要找 k 个数
     * @param residue 剩余多少
     * @param start   下一轮搜索的起始元素是多少
     * @param path    深度优先遍历的路径参数（状态变量）
     * @param res     保存结果集的列表
     */
    private void dfs(int k, int residue, int start, Deque<Integer> path, List<List<Integer>> res) {
        // 这一步判断可以放到上一层，减少递归深度
        if (residue < 0) {
            return;
        }

        if (k == 0) {
            if (residue == 0) {
                res.add(new ArrayList<>(path));
                return;
            }
            return;
        }

        for (int i = start; i <= 9; i++) {
            path.addLast(i);
            dfs(k - 1, residue - i, i + 1, path, res);
            path.removeLast();
        }
    }
}
'''

# java优化版本
'''
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class Solution {

    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> res = new ArrayList<>();

        // 一开始做一些特殊判断
        if (k <= 0 || n <= 0 || k >= n) {
            return res;
        }

        // 寻找 n 的上限：[9, 8, ... , (9 - k + 1)]，它们的和为 (19 - k) * k / 2
        // 比上限还大，就不用搜索了：
        if (n > (19 - k) * k / 2) {
            return res;
        }

        // 根据官方对 Stack 的使用建议，这里将 Deque 对象当做 stack 使用
        // 注意只使用关于栈的接口
        Deque<Integer> path = new ArrayDeque<>();
        dfs(k, n, 1, path, res);
        return res;
    }

    /**
     * @param k       剩下要找 k 个数
     * @param residue 剩余多少
     * @param start   下一轮搜索的起始元素是多少
     * @param path    深度优先遍历的路径参数（状态变量）
     * @param res     保存结果集的列表
     */
    private void dfs(int k, int residue, int start, Deque<Integer> path, List<List<Integer>> res) {
        // 剪枝：[start, 9] 这个区间里的数都不够 k 个，不用继续往下搜索
        if (10 - start < k) {
            return;
        }
        if (k == 0) {
            if (residue == 0) {
                res.add(new ArrayList<>(path));
                return;
            }
        }

        // 枚举起点值 [..., 7, 8, 9]
        // 找 3 个数，起点最多到 7
        // 找 2 个数，起点最多到 8
        // 规律是，起点上界 + k = 10，故起点上界 = 10 - k
        for (int i = start; i <= 10 - k; i++) {

//            if ((2 * i + k - 1) * k / 2 > residue) {
//                break;
//            }

            // 剪枝
            if (residue - i < 0) {
                break;
            }
            path.addLast(i);
            dfs(k - 1, residue - i, i + 1, path, res);
            path.removeLast();
        }
    }
}
'''