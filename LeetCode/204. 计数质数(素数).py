# 204. 计数质数(素数).py
'''
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 
'''
# # 高效找素数
# 素数的定义很简单，如果一个数如果只能被 1 和它本身整除，那么这个数就是素数。

# 不要觉得素数的定义简单，恐怕没多少人真的能把素数相关的算法写得高效。本文就主要聊这样一个函数：

'''
int countPrimes(int n) {
    boolean[] isPrim = new boolean[n];
    Arrays.fill(isPrim, true);
    for (int i = 2; i * i < n; i++) 
        if (isPrim[i]) 
            for (int j = i * i; j < n; j += i) 
                isPrim[j] = false;

    int count = 0;
    for (int i = 2; i < n; i++)
        if (isPrim[i]) count++;

    return count;
}
该算法的时间复杂度比较难算，显然时间跟这个嵌套 for 循环有关，其操作数应该是：

   n/2 + n/3 + n/5 + n/7 + …= n × (1/2 + 1/3 + 1/5 + 1/7…)

括号中是素数的倒数和。其最终结果是 O(N * loglogN)，有兴趣的读者可以查一下该算法的时间复杂度证明。
'''

# 暴力法
'''
int countPrimes(int n) {
    int count = 0;
    for (int i = 2; i < n; i++)
        if (isPrim(i)) count++;
    return count;
}
// 判断整数 n 是否是素数
boolean isPrime(int n) {
    for (int i = 2; i < n; i++)
        if (n % i == 0)
            // 有其他整除因子
            return false;
    return true;
}
'''


class Solution:
    # Sieve of Eratosthenes算法
    def countPrimes(self, n: int) -> int:
        # 维护一个dp数组，注意是从小到大
        # 核心思路，素数的倍数一定不是素数，又因为非素数可以被比他小的素数*int表示
        # 所以这里只判断dp数组中从小到大的素数的倍数
        # 又因为比如说x,则x之前的数字都已经乘过了，所以直接从x**2开始计算 数学归纳法
        # 实际上，比x小的数字，不论是素数还是非素数，他们倍数都会被定义为false，所以直接从x**2开始即可
        isPrime = [True for i in range(n + 1)]
        i = 2
        # 最外层的优化
        while i * i < n:
            if isPrime[i]:
                j = i * i
                # 里面的优化
                while j < n:
                    isPrime[j] = False
                    j += i
            i += 1
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        return count

    def countPrimes(self, n):
        """
        求n以内的所有质数，不包括n本身（纯python代码）
        """
        # 最小的质数是 2
        if n < 2:
            return 0

        # 首先构造 0 到 n-1 的自然数列表，每个元素的下标对应每个自然数，元素值用于标记该元素下标是否为质数
        # 这样一来不用开辟内存用来存放大量的数字
        isPrime = [1] * n
        # 0 和 1 不是质数
        isPrime[0] = isPrime[1] = 0

        # 根据算术基本定理，任何一个合数，即非质数，都可以以唯一形式被写成质数的乘积，即分解质因数。
        # 埃式筛法：找出 2 到 根号n 的范围内的所有质数，将列表中所有它的倍数位设为0
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                # 指定位置切片赋值，从它的平方开始，因为小于平方的倍数已经被之前的质数倍数排除了
                isPrime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)

        # 现在每个质数位的值为1，其余合数位的值为0，返回质数个数
        return sum(isPrime)
# Java
'''
int countPrimes(int n) {
    boolean[] isPrim = new boolean[n];
    Arrays.fill(isPrim, true);
    for (int i = 2; i * i < n; i++) 
        if (isPrim[i]) 
            for (int j = i * i; j < n; j += i) 
                isPrim[j] = false;
    int count = 0;
    for (int i = 2; i < n; i++)
        if (isPrim[i]) count++;
    return count;
}
'''


class Solution:
    def countPrimes(self, n: int) -> int:
        dp = [1 for i in range(n)]
        i = 2
        while i * i < n:
            # 如果是素数就进入循环
            if dp[i] == 1:
                j = i
                while i * j < n:
                    dp[i * j] = 0
                    j += 1
            i += 1
        count = 0
        for i in range(2, n):
            if dp[i]:
                count += 1
        return count
Solution().countPrimes(10)


