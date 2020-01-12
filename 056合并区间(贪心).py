# 56. 合并区间.py
'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
public int[][] merge(int[][] intervals) {
    LinkedList<int[]> res = new LinkedList<>();
    if (intervals == null || intervals.length == 0) {
        return res.toArray(new int[0][]);
    }

    Arrays.sort(intervals, new Comparator<int[]>() {
        @Override
        public int compare(int[] o1, int[] o2) {
            return o1[0] - o2[0];
        }
    });

    for (int i = 0; i < intervals.length; i++) {
        if (res.isEmpty() || res.getLast()[1] < intervals[i][0]) {
            res.add(intervals[i]);
        } else {
            res.getLast()[1] = Math.max(res.getLast()[1], intervals[i][1]);
        }
    }

    //为什么放0，0长度？可以看下源码就知道了
    return res.toArray(new int[0][0]);
}
'''
'''
时间复杂度：O(nlogn)

除去 sort 的开销，我们只需要一次线性扫描，所以主要的时间开销是排序的 O(nlgn)O(nlgn)

空间复杂度：O(1) or O(N)

如果我们可以原地排序 intervals ，就不需要额外的存储空间；否则，我们就需要一个线性大小的空间去存储 intervals 的备份，来完成排序过程。

'''
class Solution:
    def merge(self, intervals):
        res = []
        intervals.sort()
        for i in intervals:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(i[1],res[-1][1])
        return res
a = [[1,3],[6,9]]
print(a)