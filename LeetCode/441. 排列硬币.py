'''
你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。

给定一个数字 n，找出可形成完整阶梯行的总行数。

n 是一个非负整数，并且在32位有符号整型的范围内。

示例 1:

n = 5

硬币可排列成以下几行:
¤
¤ ¤
¤ ¤

因为第三行不完整，所以返回2.
示例 2:

n = 8

硬币可排列成以下几行:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

因为第四行不完整，所以返回3.
'''

# java
'''
根据数学公式，k(k+1)/2 = n，可以得到其正数解为：k = sqrt(2n+1/4) - 1/2。然后求整即可。
唯一的问题是，这里2n+1/4有可能会超出sqrt函数的参数范围。
于是，我们可以变换一下， k = sqrt(2) * sqrt(n+1/8) - 1/2，这样求平方根就不会超限了。
于是，我们就有了这么一行代码
class Solution {
    public int arrangeCoins(int n) {
        return (int)(Math.sqrt(2) * Math.sqrt(n + 0.125) - 0.5);
    }
}
'''
'''
/**
     * 数学求解法 O(1) 不含求根预算
     *
     * @param n
     * @return
     */
    public static int arrangeCoins(int n) {
        return (int) (-1 + Math.sqrt(1 + 8 * (long) n)) / 2;
    }

    /**
     * 迭代求解法 O(n)
     *
     * @param n
     * @return
     */
    public static int arrangeCoins2(int n) {
        int i = 1;
        while (n >= i) {
            n -= i;
            i++;
        }
        return i - 1;
    }

    /**
     * 二分查找，O(log(n / 2 + 1))
     *
     * @param n
     * @return
     */
 public int arrangeCoins(int n) {
        int low = 0, high = n;
        while (low <= high) {
            long mid = (high - low) / 2 + low;
            long cost = ((mid + 1) * mid) / 2;
            if (cost == n) {
                return (int)mid;
            } else if (cost > n) {
                high = (int)mid - 1;
            } else {
                low = (int)mid + 1;
            }
        }
        return high;
    }
'''


# 自己的版本
# 求小于等于n的lastposition
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # 二分
        left = 0
        right = n
        while left + 1 < right:
            mid = left + (right - left) // 2
            if mid * (mid + 1) // 2 <= n:
                left = mid
            else:
                right = mid
        if right * (right + 1) // 2 <= n:
            return right
        else:
            return left
