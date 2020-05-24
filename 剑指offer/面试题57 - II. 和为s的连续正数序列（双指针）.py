'''
面试题57 - II. 和为s的连续正数序列
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数)

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
示例 1：
输入：target = 9
输出：[[2,3,4],[4,5]]

示例 2：
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]

限制：
1 <= target <= 10^5
'''
from typing import List


class Solution:
    from math import sqrt
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        size = target // 2 + 1
        nums = [i for i in range(1, size + 1)]
        print(nums)
        # left其实为写指针
        left = 0
        sum = 0
        res = []
        # 双指针，right为读指针
        for right in range(size):
            # 大于等于left移动，小于target的话right移动
            sum += nums[right]
            while sum > target:
                sum -= nums[left]
                left += 1
            if sum == target:
                res.append(nums[left:right + 1])
                sum -= nums[left]
                left += 1

        return res


print(Solution().findContinuousSequence(15))


def findContinuousSequence(self, target: int) -> List[List[int]]:
    i = 1  # 滑动窗口的左边界
    j = 1  # 滑动窗口的右边界
    sum = 0  # 滑动窗口中数字的和
    res = []

    while i <= target // 2:
        if sum < target:
            # 右边界向右移动
            sum += j
            j += 1
        elif sum > target:
            # 左边界向右移动
            sum -= i
            i += 1
        else:
            # 记录结果
            arr = list(range(i, j))
            res.append(arr)
            # 左边界向右移动
            sum -= i
            i += 1

    return res


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 初始化窗口指针和输出列表
        i, j, res = 1, 2, []

        # 滑动窗口的右边界不能超过target的中值
        while j <= target // 2 + 1:
            # 计算当前窗口内数字之和
            cur_sum = sum(list(range(i, j + 1)))
            # 若和小于目标，右指针向右移动，扩大窗口
            if cur_sum < target:
                j += 1
            # 若和大于目标，左指针向右移动，减小窗口
            elif cur_sum > target:
                i += 1
            # 相等就把指针形成的窗口添加进输出列表中
            # 别忘了，这里还要继续扩大寻找下一个可能的窗口哦
            else:
                res.append(list(range(i, j + 1)))
                # 这里用j+=1，i+=1，i+=2都可以的
                j += 1

        return res


# 求根法
class Solution:
    def findContinuousSequence(self, target: int):
        # 创建输出列表
        res = []

        # y不能超过target的中值,即y<=target//2 + 1,range函数左开右闭,所以这里是+2
        for y in range(1, target // 2 + 2):
            # 应用我们的求根公式
            x = (1 / 4 + y ** 2 + y - 2 * target) ** (1 / 2) + 0.5
            # 我们要确保x不能是复数，且x必须是整数
            if type(x) != complex and x - int(x) == 0:
                res.append(list(range(int(x), y + 1)))

        return res


# 间隔法
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 我们的间隔从1开始
        i, res = 1, []

        # 根据上面的条件1，限定i的大小，即间隔的范围
        while i * (i + 1) / 2 < target:
            # 根据条件2，如果x不为整数则扩大间隔
            if not (target - i * (i + 1) / 2) % (i + 1):
                # 如果两个条件都满足，代入公式求出x即可，地板除//会把数改成float形式，用int()改回来
                x = int((target - i * (i + 1) / 2) // (i + 1))
                # 反推出y，将列表填入输出列表即可
                res.append(list(range(x, x + i + 1)))
            # 当前间隔判断完毕，检查下一个间隔
            i += 1

        # 由于间隔是从小到大，意味着[x,y]列表是从大到小的顺序放入输出列表res的，所以反转之
        return res[::-1]
