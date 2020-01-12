# 42. 接雨水.py
'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

链接：https://leetcode-cn.com/problems/trapping-rain-water
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        #双指针优化版本
        n = len(height)
        if n < 1:
            return 0
        ans = 0
        left = 0
        right = n-1
        l_max = height[0]
        r_max = height[n-1]
        #每次循环更新一次，所以这里必须<=
        while left <= right:
            l_max = max(height[left],l_max)
            r_max = max(height[right],r_max)
            #谁小移动谁，相当于当前指针所在位置已经计算过了
            if l_max < r_max:
                ans += l_max - height[left]
                left += 1
            else:
                ans += r_max - height[right]
                right -= 1  
        return ans
'''
# 接雨水
# 暴力法
def trap(heigh):
    length = len(heigh)
    ans = 0
    # 边走边算
    # 从第二个到倒数第二个之间计算
    for i in range(1,length-1):
        l_max,r_max = heigh[0],heigh[length-1]
        # 找到当前元素右边最高的柱子
        for j in range(i,length):
            r_max = max(heigh[j],r_max)
        # 找到当前元素左边最高柱子
        for j in range(i,0,-1):
            l_max = max(heigh[j],l_max)
        # 计算当前元素能接的最大水量，同时累加到ans结果中
        ans += min(l_max,r_max) - heigh[i]
    return ans


# 备忘录优化
# 准备两个备忘录，减少重复计算
'''
    # 我们开两个数组r_max和l_max充当备忘录
    # l_max[i]表示位置 i 左边最高的柱子高度
    # r_max[i]表示位置 i 右边最高的柱子高度
'''
def mempTrap(heigh):
    if len(heigh) < 1:
        return 0
    length = length(heigh)
    ans = 0
    # 准备两个备忘录
    l_max,r_max = [ 0 for i in range(length)],[0 for i in range(length)]
    # 当前元素左边最大值
    l_max[0] = heigh[0]
    # 当前元素右边最大值
    r_max[-1] = heigh[-1]
    # 计算从i到左右两边的最大值
    for i in range(1,length):
        r_max = max(heigh[i],r_max[i-1])
    for i in range(length-1,-1,-1):
        l_max = max(heigh[i],l_max[i+1])
    # 计算答案,第一个和最后一个位置不用计算
    for i in range(1,length-1):
        ans += min(l_max[i]-r_max[i])-heigh[i]
    return ans


# 双指针
'''
    # 边走边算
    # l_max是height[0..left]中最高柱子的高度，
    # r_max是height[right..end]的最高柱子的高度
    # 最后双指针一定会相遇，所以移动一次计算一次
'''
def twoPreTrap(heigh):
    if len(heigh) < 1:
        return 0
    length = len(heigh)
    ans = 0
    left = 0
    right = length-1
    l_max = heigh[0]
    r_max = heigh[length-1]
    #必须保证left到达right，因为每次判断一步
    while left <= right:
        # 每次循环更新一次
        l_max = max(l_max,heigh[left])
        r_max = max(r_max,heigh[right])
        # 如果l_max < r_max,即只和l_max相关，就和r_max没有关系了，谁小移动谁
        if l_max < r_max:
            ans += l_max - heigh[left]
            left += 1
        else:
            ans += r_max - heigh[right]
            right -= 1
    return ans

print(twoPreTrap([1,6,1,5]))
'''