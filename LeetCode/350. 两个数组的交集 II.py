'''
给定两个数组，编写一个函数来计算它们的交集。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
 

说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。
进阶：

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
'''
from typing import List
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_hash = Counter(nums1)
        nums2_hash = Counter(nums2)
        res = []
        for k, v in nums1_hash.items():
            if k in nums2_hash:
                res.extend(min(nums2_hash[k], v) * [k])
        return res

# java
'''
class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        HashMap<Integer,Integer> map = new HashMap<>();
        //1.统计nums1中各个元素的出现次数
        for (int i = 0; i < nums1.length; i++) {
            //当Map集合中有这个key时，就使用这个key值，如果没有就使用默认值defaultValue
            int count = map.getOrDefault(nums1[i], 0)+1;
            map.put(nums1[i],count);
        }
        //2. 遍历nums2查找存在map中的元素同时更新map的key的次数
        int[] result = new int[nums1.length];//既然是两数组的交集，那么长度一定小于等于任意一个数组
        int index = 0;
        for (int target : nums2) {
            int count = map.getOrDefault(target, 0);
            //证明元素target存在于map，就说明nums2中的target是和nums1有交集的元素
            if (count > 0){
                result[index++] = target;//添加到结果集中
                count --;
                map.put(target, count);//更新map
            }
        }
       //将指定的数组指定的范围复制到一个新的数组中
        return Arrays.copyOfRange(result,0,index);
    }
}
'''