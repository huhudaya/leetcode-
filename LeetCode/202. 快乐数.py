'''
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：
对于一个正整数
每一次将该数替换为它每个位置上的数字的平方和
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。

 

示例：

输入：19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''


# 快慢指针，判圈法
# 时间复杂度O(logN)
class Solution:
    def isHappy(self, n: int) -> bool:
        # 核心思路是判定是否有环！
        def helper(num):
            res = 0
            for i in str(num):
                res += int(i) ** 2
            return res

        # 快慢指针
        slow = n
        fast = helper(n)
        # 核心思路是检测是否有环
        while fast != 1 and fast != slow:
            slow = helper(slow)
            fast = helper(helper(fast))
        return fast == 1


# 时间复杂度O(N)
# 空间复杂度O(lonN)
class Solution:
    def isHappy(self, n: int) -> bool:
        # 初始化 visited
        visited = set()
        # 当 n != 1，并且没见过 n 时进行判断
        while n != 1 and n not in visited:
            # 把 n 放入 visited
            visited.add(n)
            # 计算下一轮的数字
            nxt = 0
            # 计算 n 的各位数字平方和
            while n != 0:
                nxt += (n % 10) ** 2
                n //= 10
            # 把下一轮的数字设定为 n
            n = nxt
        # 判断 n 的最终结果是否为 1
        return n == 1


# set
class Solution:
    def isHappy(self, n: int) -> bool:
        # 判定是否有环
        seen = set()

        def cal_num(n):
            res = 0
            while n != 0:
                res += (n % 10) ** 2
                n //= 10
            return res

        while n != 1 and n not in seen:
            seen.add(n)
            n = cal_num(n)
        return n == 1
