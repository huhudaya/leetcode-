'''
给定一个无重复元素的数组 candidates 和一个目标数 target
找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''
'''
public class combinationSum_39 {

    public static void main(String[] args) {
        combinationSum(new int[]{2,3,6,7},7);
        System.out.println(res);

    }
    public static List<List<Integer>> res =  new LinkedList<>();

    public static List<List<Integer>> combinationSum(int[] candidates, int target) {
        LinkedList<Integer> track = new LinkedList<>();
        Arrays.sort(candidates);
        backtrack(candidates, 0, target, track);
        return res;
    }

    private static void backtrack(int[] candidates, int start, int target, LinkedList<Integer> track) {
        if (target < 0) return;
        if (target == 0){
            res.add(new LinkedList<>(track));
            return;
        }
        for(int i = start;i < candidates.length;i++){
            if(target < candidates[i]) break;
            track.add(candidates[i]);
            backtrack(candidates,i,target-candidates[i],track);
            track.removeLast();
        }
    }
}
'''


# 注意 题意， candidates是无重复的数组！！！！
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 回溯法模板
        res = []
        # 这里需要排序 便于剪枝
        candidates.sort()
        n = len(candidates)
        self.__dfs(candidates, 0, res, target, [], n)
        return res

    def __dfs(self, candidates, start, res, target, path, size):
        if target == 0:
            res.append(path[:])
            return
        for i in range(start, size):
            # 剪枝
            if target < candidates[i]:
                break
            # 路径添加
            path.append(candidates[i])
            # 递归 i 表示这里可以利用当前元素以及当前元素之后的元素
            self.__dfs(candidates, i, res, target - candidates[i], path, size)
            # 路径移除
            path.pop()

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        import functools
        @functools.lru_cache(None)
        def helper(amount):
            if amount == 0:
                return 0
            return min(helper(amount - c) if amount - c >= 0 else float("inf") for c in coins) + 1
        res = helper(amount)
        return res if res != float("inf") else -1