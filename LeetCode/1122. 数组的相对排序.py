'''

给你两个数组，arr1 和 arr2，

arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。
未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。



示例：

输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]


提示：

arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
arr2 中的元素 arr2[i] 各不相同
arr2 中的每个元素 arr2[i] 都出现在 arr1 中
'''

from typing import List


# 对元组的排序
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n = len(arr2)
        def mycmp(x: int):
            # return (0, rank[x]) if x in rank else (1, x)
            # 表示一定需要调整
            return rank[x] - n if x in rank else x

        rank = {x: i for i, x in enumerate(arr2)}
        arr1.sort(key=mycmp)
        return arr1

'''
func relativeSortArray(arr1 []int, arr2 []int) []int {
    rank := map[int]int{}
    for i, v := range arr2 {
        rank[v] = i - len(arr2)
    }
    sort.Slice(arr1, func(i, j int) bool {
        x, y := arr1[i], arr1[j]
        if r, has := rank[x]; has {
            x = r
        }
        if r, has := rank[y]; has {
            y = r
        }
        return x < y
    })
    return arr1
}
'''



# 计数排序
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        upper = max(arr1)
        frequency = [0] * (upper + 1)
        for x in arr1:
            frequency[x] += 1

        ans = list()
        for x in arr2:
            ans.extend([x] * frequency[x])
            frequency[x] = 0
        for x in range(upper + 1):
            if frequency[x] > 0:
                ans.extend([x] * frequency[x])
        return ans


# java
'''
class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        Map<Integer,Integer> map = new HashMap<Integer, Integer>();
        // map 存储arr2中元素以及其对应的下标位置
        for(int i=0; i<arr2.length; i++){
            map.put(arr2[i],i);
        }
        Integer[] temp = new Integer[arr1.length];
        //将int[] arr1 转成 Integer[] temp,
        for(int i=0; i<arr1.length; i++){
            temp[i] = arr1[i];
        }
        //按自定义方式排序
        Arrays.sort(temp, new Comparator<Integer>(){
            @Override
            public int compare(Integer a, Integer b){
                //若a和b都在arr2中，按map中存储的下标位置从小到大排序
                if(map.containsKey(a) && map.containsKey(b)){
                    return map.get(a)-map.get(b);
                }else if(map.containsKey(a)){ //若只有a出现在arr2中，a排在前面
                    return -1;
                }else if(map.containsKey(b)){ //若只有b出现在arr2中，b排在前面
                    return 1;
                }else{ //若a和b都不在arr2中，按其值从小到大排列
                    return a-b;
                }
            }
        });
        //将Integer类型转回基本数据类型int
        for(int i=0; i<arr1.length; i++){
            arr1[i] = temp[i];
        }
        return arr1;
    }
}
'''

# 计数排序 golang
'''
func relativeSortArray(arr1 []int, arr2 []int) []int {
    upper := 0
    for _, v := range arr1 {
        if v > upper {
            upper = v
        }
    }
    frequency := make([]int, upper+1)
    for _, v := range arr1 {
        frequency[v]++
    }

    ans := make([]int, 0, len(arr1))
    for _, v := range arr2 {
        for ; frequency[v] > 0; frequency[v]-- {
            ans = append(ans, v)
        }
    }
    for v, freq := range frequency {
        for ; freq > 0; freq-- {
            ans = append(ans, v)
        }
    }
    return ans
}
'''



