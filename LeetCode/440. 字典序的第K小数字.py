'''
给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。

注意：1 ≤ k ≤ n ≤ 109。

示例 :

输入:
n: 13   k: 2

输出:
10

解释:
字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
'''

'''
我们求字典序第k个就是上图前序遍历访问的第k节点！
但是不需要用前序遍历，如果我们能通过数学方法求出节点1和节点2之间需要走几步，减少很多没必要的移动。

其实只需要按层节点个数计算即可，图中节点1和节点2在第二层，因为n = 13，节点1可以移动到节点2（同一层）所以在第二层需要移动1步。

第三层，移动个数就是 (13 - 10 + 1) = 4 （min（13 + 1， 20） - 10）

所以节点1到节点2需要移动 1 + 4 = 5 步

当移动步数小于等于k，说明需要向右节点移动，图中就是节点1移动到节点2。

当移动步数大于k，说明目标值在节点1和节点2之间，我们要向下移动！即从节点1移动到节点10。
'''


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def cal_steps(n, n1, n2):
            step = 0
            while n1 <= n:
                step += min(n2, n + 1) - n1
                n1 *= 10
                n2 *= 10
            return step

        cur = 1
        # k -= 1

        while k > 0:
            # 求同一层移动一个节点所需要的步数
            steps = cal_steps(n, cur, cur + 1)
            # 如果移动次数<=k，则需要水平移动一次
            if steps <= k:
                k -= steps
                cur += 1
            # 否则需要下沉
            else:
                k -= 1
                cur *= 10

        return cur - 1


# 自己的版本
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # 计算水平移动的时候需要移动的步数
        def cal_step(n, n1, n2):
            step = 0
            while n1 <= n:
                step += min(n2, n + 1) - n1
                n1 *= 10
                n2 *= 10
            return step

        cur = 1
        # 因为k多走了一步，所以这里需要提前减1
        k -= 0
        while k > 0:
            # 计算水平移动的时候需要的步数
            step = cal_step(n, cur, cur + 1)
            # 需要水平移动
            if step <= k:  # 在另外的子树中
                k -= step
                # 这里cur每次都+1，最后会多加一个1
                cur += 1
            # 需要下沉
            else:  # 在当前子树中
                k -= 1
                cur *= 10
        return cur


print(Solution().findKthNumber(100, 90))
