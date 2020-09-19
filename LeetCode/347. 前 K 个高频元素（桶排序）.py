'''
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]
说明：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
'''

# 求前 k 大，用小根堆，求前 k 小，用大根堆。

# 排序
# O(Nlog(N))
# 建立堆，堆中添加一个元素的复杂度是 O(log(k))，要进行 N 次复杂度是 O(N)。
# counter方法复杂度为O（N），建堆和输出结果是O（NlogK）
# Klog(K) 空间复杂度为O(N)
from typing import List
import collections


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #  count是map， map.get(key)得到value， value表示的是统计元素出现的个数， 这里是实现一个自定义比较器
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)


# 堆排序 Java
'''
class Solution {
  public List<Integer> topKFrequent(int[] nums, int k) {
    // build hash map : character and how often it appears
    HashMap<Integer, Integer> count = new HashMap();
    for (int n: nums) {
      count.put(n, count.getOrDefault(n, 0) + 1);
    }

    // init heap 'the less frequent element first'
    PriorityQueue<Integer> heap =
            // 小根堆
            new PriorityQueue<Integer>((n1, n2) -> count.get(n1) - count.get(n2));

    // keep k top frequent elements in the heap
    for (int n: count.keySet()) {
      heap.add(n);
      if (heap.size() > k)
        heap.poll();
    }

    // build output list
    List<Integer> top_k = new LinkedList();
    while (!heap.isEmpty())
      top_k.add(heap.poll());
    Collections.reverse(top_k);
    return top_k;
  }
}
'''

# 桶排序
# 时间复杂度O(N),空间复杂度O(N)
'''
//基于桶排序求解「前 K 个高频元素」
class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        List<Integer> res = new ArrayList();
        // 使用字典，统计每个元素出现的次数，元素为键，元素出现的次数为值
        HashMap<Integer,Integer> map = new HashMap();
        for(int num : nums){
            if (map.containsKey(num)) {
               map.put(num, map.get(num) + 1);
             } else {
                map.put(num, 1);
             }
        }
        
        //桶排序
        //将频率作为数组下标，对于出现频率不同的数字集合，存入对应的数组下标
        List<Integer>[] list = new List[nums.length+1];
        for(int key : map.keySet()){
            // 获取出现的次数作为下标
            int i = map.get(key);
            if(list[i] == null){
               list[i] = new ArrayList();
            } 
            list[i].add(key);
        }
        
        // 倒序遍历数组获取出现顺序从大到小的排列
        for(int i = list.length - 1;i >= 0 && res.size() < k;i--){
            if(list[i] == null) continue;
            res.addAll(list[i]);
        }
        return res;
    }
}
'''



'''
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> count = new HashMap();
        for (int num: nums){
            count.put(num, count.getOrDefault(num, 0) + 1);
        }
        // 小根堆 按value建堆
        PriorityQueue<Integer> heap = new PriorityQueue<>((o1, o2) -> count.get(o1) - count.get(o2));
        for (int num: count.keySet()){
            heap.add(num);
            if (heap.size() > k) heap.poll();
        }
        // 输出
        int[] topK = new int[k];
        for (int i = 0; i < k; i ++){
            topK[i] = heap.poll();
        }
        return topK;
    }
}
'''


# 桶排序
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if nums is None:
            return
        n = len(nums)
        # 使用桶排序
        bucket = [[] for _ in range(n + 1)]
        res = []
        cnt = 0
        hash = collections.Counter(nums)
        for key, val in hash.items():
            # value作为索引，将key作为value
            bucket[val].append(key)
        # 倒着遍历bucket
        for num in bucket[::-1]:
            if cnt == k:
                return res
            if num:
                res.extend(num)
                cnt += len(num)
        return res


# 堆 排序
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if not nums or len(nums) == 1:
            return nums
        freq_dict = collections.Counter(nums)
        # print(freq_dict)
        priority_queue = []
        # 扫描freq，维护当前出现频率最高的k个元素，优先队列（堆）中存放元组（频率，元素）
        for element, freq in freq_dict.items():
            # print element, freq
            if len(priority_queue) == k:
                # print priority_queue
                if freq > priority_queue[0][0]:  # 新加入的元素频率比堆中最小频率要大
                    heapq.heappop(priority_queue)  # 弹出堆顶元素
                    heapq.heappush(priority_queue, (freq, element))
            else:
                heapq.heappush(priority_queue, (freq, element))
                # print priority_queue
            # print(priority_queue)

        return [item[1] for item in priority_queue]


import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 求最大的k个数用小根堆
        # 先构建一个hash映射表
        hash = Counter(nums)
        res = []
        print(hash)
        for key, val in hash.items():
            if len(res) < k:
                # 注意，这里添加到堆的时候需要逆序
                heapq.heappush(res, (val, key))
            # 如果当前元素比堆顶的值大，则替换进堆中
            elif val > res[0][0]:
                heapq.heapreplace(res, (val, key))
        ans = []
        for i in res:
            ans.append(i[1])
        return ans


Solution().topKFrequent([4, 1, -1, 2, -1, 2, 3], 2)
