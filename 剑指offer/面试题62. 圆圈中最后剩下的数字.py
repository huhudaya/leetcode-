'''
0,1,,n-1这n个数字排成一个圆圈，从数字0开始
每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈
从数字0开始每次删除第3个数字
则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
示例 1：

输入: n = 5, m = 3
输出: 3
示例 2：

输入: n = 10, m = 17
输出: 2
'''

# 约瑟夫环
# Python 默认的递归深度不够，需要手动设置
# 时间和空间复杂度都是O(N)
'''
题目中的要求可以表述为：给定一个长度为 n 的序列，每次向后数 m 个元素并删除，那么最终留下的是第几个元素？
这个问题很难快速给出答案。但是同时也要看到，这个问题似乎有拆分为较小子问题的潜质：
如果我们知道对于一个长度 n - 1 的序列，留下的是第几个元素，那么我们就可以由此计算出长度为 n 的序列的答案。

算法
我们将上述问题建模为函数 f(n, m)，该函数的返回值为最终留下的元素的序号。
首先，长度为 n 的序列会先删除第 m % n 个元素，然后剩下一个长度为 n - 1 的序列。
那么，我们可以递归地求解 f(n - 1, m)，就可以知道对于剩下的 n - 1 个元素，最终会留下第几个元素，我们设答案为 x = f(n - 1, m)。
由于我们删除了第 m % n 个元素，将序列的长度变为 n - 1。当我们知道了 f(n - 1, m) 对应的答案 x 之后
我们也就可以知道，长度为 n 的序列最后一个删除的元素，应当是从 m % n 开始数的第 x 个元素
因此有 f(n, m) = (m % n + x) % n = (m + x) % n。
'''


# 注意 是每次删除一个人，第一次有8个人的时候，第一轮过去杀死一个还有7个人

# 递推 f(8,3) = (f(7, 3) + 3) % 8
#     f(n,m) = (f(n - 1 + m) % n)
import sys
sys.setrecursionlimit(100000)
def f(n, m):
    if n == 0:
        return 0
    x = f(n - 1, m)
    return (m + x) % n

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        return f(n, m)


# 数学法 时间O(N),空间O(1)
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        f = 0
        for i in range(2, n + 1):
            f = (m + f) % i
        return f



from collections import deque
# 队列模拟
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        simqueue = deque()
        for i in range(n):
            simqueue.append(i)
        while len(simqueue) > 1:
            for i in range(n):
                simqueue.append(simqueue.popleft())
            # 循环结束后kill一个人
            simqueue.popleft()
        alive = simqueue.popleft()
        return alive

'''
既然约塞夫问题就是用人来举例的，那我们也给每个人一个编号（索引值），每个人用字母代替
下面这个例子是N=8 m=3的例子
我们定义F(n,m)表示最后剩下那个人的索引号，因此我们只关系最后剩下来这个人的索引号的变化情况即可

从8个人开始，每次杀掉一个人，去掉被杀的人，然后把杀掉那个人之后的第一个人作为开头重新编号

第一次C被杀掉，人数变成7，D作为开头，（最终活下来的G的编号从6变成3）
第二次F被杀掉，人数变成6，G作为开头，（最终活下来的G的编号从3变成0）
第三次A被杀掉，人数变成5，B作为开头，（最终活下来的G的编号从0变成3）
以此类推，当只剩一个人时，他的编号必定为0！（重点！）

现在我们知道了G的索引号的变化过程，那么我们反推一下
从N = 7 到N = 8 的过程

如何才能将N = 7 的排列变回到N = 8 呢？

我们先把被杀掉的C补充回来，然后右移m个人，发现溢出了，再把溢出的补充在最前面

神奇了 经过这个操作就恢复了N = 8 的排列了！
'''
'''
class Solution {
public:
    int lastRemaining(int n, int m) {
        int pos = 0; // 最终活下来那个人的初始位置
        for(int i = 2; i <= n; i++){
            pos = (pos + m) % i;  // 每次循环右移
        }
        return pos;
    }
};
'''
# java链表模拟
'''
class Solution {
    public int lastRemaining(int n, int m) {
        ArrayList<Integer> list = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            list.add(i);
        }
        int idx = 0;
        while (n > 1) {
            idx = (idx + m - 1) % n;
            list.remove(idx);
            n--;
        }
        return list.get(0);
    }
}
'''
'''
首先，记f(n)为游戏结束后最后一个数字的index
那么关键在于找到f(n,start=0)和f(n-1,start=0)的关系
显然，第一次扔出去的元素是(m-1)%n，记作k
那么根据游戏规则f(n,start=0)=f(n-1,start = k+1)。
接下来我们可以看到f(n-1,start = k+1) = (f(n-1,start=0)+k+1)%n。
有了这个中间桥梁，可知f(n,start=0) = (f(n-1,start=0)+k+1)%n = (f(n-1,start=0)+m)%n。
然后从f(1)=0推广过去即可。

这类问题凭空很难找到规律，建议记住f(n) = (f(n-1)+m)%n的大概形式，再去推导会比较有方向。
数学归纳法都是扯淡，都是有了公式强行去归纳，要是不知道递推公式怎么能从n=1,n=2,n=3找到取模规律

'''
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        res = 0
        for i in range(2,n+1):
            res = (res+m)%i
        return(res)
