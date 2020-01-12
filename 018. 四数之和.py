# 18. 四数之和.py
'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
链接：https://leetcode-cn.com/problems/4sum
'''

# 简约版
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        from itertools import combinations as com
        dic, l = collections.defaultdict(list), [*com(range(len(nums)), 2)]
        for a, b in l: dic[target - nums[a] - nums[b]].append((a, b))
        r = [(*ab, c, d) for c, d in l for ab in dic[nums[c] + nums[d]]]
        return [*set(tuple(sorted(nums[i] for i in t)) for t in r if len(set(t)) == 4)]
思想类似于 2SUM，先得到任意两个数字的和记入字典，然后再获得其余任意俩个数字，看看是否匹配。2个 2SUM 相当于 4SUM。时间复杂度为 O(N^2)
1.用 combination 获得 nums 中任意两个不同索引的组合
2.用字典记录任意两个数字的和，dic =｛除了这两个数字之外还差多少：这俩个数字在 nums 中的索引｝
3.用 r 记录所有满足条件的索引序列，注意此时可能含有重复的索引
4.利用 len + set 保证 a，b，c，d 各不相等，用 set 删除重复的结果

作者：QQqun902025048
链接：https://leetcode-cn.com/problems/4sum/solution/5-xing-python-on2-by-qqqun902025048/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# 双指针
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4: return []
        nums.sort()
        res = []
        for i in range(n-3):
            # 防止重复 数组进入 res
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 当数组最小值和都大于target 跳出
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # 当数组最大值和都小于target,说明i这个数还是太小,遍历下一个
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
            # 固定两个数 i 和 j
            for j in range(i+1,n-2):
                # 防止重复 数组进入 res
                if j - i > 1 and nums[j] == nums[j-1]:
                    continue
                # 同理
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                # 同理
                if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                    continue
                # 双指针
                left = j + 1
                right = n - 1
                while left < right:
                    tmp = nums[i] + nums[j] + nums[left] + nums[right]
                    if tmp == target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif tmp > target:
                        right -= 1
                    else:
                        left += 1
        return res
# 简洁
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=set()
        
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):#固定两个数
                left=j+1#左指针
                right=len(nums)-1#右指针
                while(right>left):
                    temp=nums[i]+nums[j]+nums[left]+nums[right]
                    if temp==target:
                        ans.add((nums[i],nums[j],nums[left],nums[right]))
                        left+=1
                        right-=1
                    if temp>target:right-=1#太大了，右指针左移
                    if temp<target:left+=1#反之
        #去重
        rec=[]
        for i in ans:
            rec.append(list(i))
        return rec