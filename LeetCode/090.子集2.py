'''
90. 子集 II
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

# 这里简单讲一下90题和47题的区别，同样都是重复的元素，同样都需要排序
# 不同的是90题没有使用used数组！而47题使用了used数组来标记是否遍历过，为了防止出现'112'这种情况，需要注意边界条件
# 子集是用到了range(start,size), 全排列是用到了used数组用来去重而且用到了depth用来记录深度


# 特别注意，设计到重复的问题，必须先排序！！！！
# 这里的 i 是指回溯树中同一层中的其他节点，start指层数
'''
start i
1 2 3 4
2 3 4
3 4
4
'''

from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size == 0:
            return []
        res = []
        # 解决重复问题，要先排序
        nums.sort()
        self._dfs(nums, size, [], res, 0)
        return res

    def _dfs(self, nums, size, path, res, start):
        # 递归结束条件,因为要求子集，所以每次遍历之前都先将路径添加到res中
        res.append(path[:])
        for i in range(start, size):
            # 剪枝 注意必须start < i ,否则就多剪了，这里表示在不是第一条分支上出现这种情况就剪枝
            if start < i and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            # 从当前元素之后遍历
            self._dfs(nums, size, path, res, i + 1)
            path.pop()
print(Solution().subsetsWithDup([1,1,0]))


# java
"""
public List<List<Integer>> subsetsWithDup(int[] nums) {
    List<List<Integer>> ans = new ArrayList<>();
    Arrays.sort(nums); //排序
    getAns(nums, 0, new ArrayList<>(), ans);
    return ans;
}

private void getAns(int[] nums, int start, ArrayList<Integer> temp, List<List<Integer>> ans) {
    ans.add(new ArrayList<>(temp));
    for (int i = start; i < nums.length; i++) {
        //和上个数字相等就跳过
        if (i > start && nums[i] == nums[i - 1]) {
            continue;
        }
        temp.add(nums[i]);
        getAns(nums, i + 1, temp, ans);
        temp.remove(temp.size() - 1);
    }
}
"""
'''
func subsetsWithDup(nums []int) (result [][]int) {
	var dfs func(temp []int, idx int)
	n := len(nums)
	sort.Ints(nums)
	dfs = func(temp []int, idx int) {
		result = append(result, append([]int(nil), temp...))
		for i := idx; i < n; i++ {
			if i > idx && nums[i] == nums[i-1] {
				continue
			}
			temp = append(temp, nums[i])
			dfs(temp, i+1)
			temp = temp[:len(temp)-1]
		}
	}
	dfs([]int{}, 0)
	return
}
'''