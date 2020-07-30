'''
现在有两种线程，氧 oxygen 和氢 hydrogen，你的目标是组织这两种线程来产生水分子。

存在一个屏障（barrier）使得每个线程必须等候直到一个完整水分子能够被产生出来。

氢和氧线程会被分别给予 releaseHydrogen 和 releaseOxygen 方法来允许它们突破屏障。

这些线程应该三三成组突破屏障并能立即组合产生一个水分子。

你必须保证产生一个水分子所需线程的结合必须发生在下一个水分子产生之前。

换句话说:

如果一个氧线程到达屏障时没有氢线程到达，它必须等候直到两个氢线程到达。
如果一个氢线程到达屏障时没有其它线程到达，它必须等候直到一个氧线程和另一个氢线程到达。
书写满足这些限制条件的氢、氧线程同步代码。

 

示例 1:

输入: "HOH"
输出: "HHO"
解释: "HOH" 和 "OHH" 依然都是有效解。
示例 2:

输入: "OOHHHH"
输出: "HHOHHO"
解释: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" 和 "OHHOHH" 依然都是有效解。
 

提示：

输入字符串的总长将会是 3n, 1 ≤ n ≤ 50；
输入字符串中的 “H” 总数将会是 2n 。
输入字符串中的 “O” 总数将会是 n 。
'''
// 暴力法 这样只会产生HHOHHO这样的序列，没法并行产生HOH这种
import java.util.concurrent.Semaphore;
import java.util.concurrent.CountDownLatch;

class H2O {

    private Semaphore h = new Semaphore(2);
    private Semaphore o = new Semaphore(0);

    public H2O() {
    }

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
		h.acquire();
        // releaseHydrogen.run() outputs "H". Do not change or remove this line.
        releaseHydrogen.run();
        o.release();
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        o.acquire(2); // acquire之后，对应的semaphore会又变成0
        // releaseOxygen.run() outputs "O". Do not change or remove this line.
		releaseOxygen.run();
        h.release(2);
    }
}
// semaphore优化版本

import java.util.concurrent.*;

class H2O {

    private Semaphore s1,s2,s3,s4;

    public H2O() {
        s1 = new Semaphore(2); // H线程信号量
        s2 = new Semaphore(1); // O线程信号量

        s3 = new Semaphore(0); // 反应条件信号量
        s4 = new Semaphore(0); // 反应条件信号量
    }

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
        s1.acquire(); // 保证只有2个H线程进入执行
        s3.release(); // 释放H原子到达信号
        s4.acquire(); // 等待O原子到达
        releaseHydrogen.run();
        s1.release(); // 相当于唤醒1个H线程
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        s2.acquire(); // 保证只有1个O线程进入执行
        s4.release(2); // 释放O原子到达信号，因为有2个H线程等待所以释放2个
        s3.acquire(2); // 等待H原子到达，2个原因同上
        releaseOxygen.run();
        s2.release(); // 相当于唤醒1个O线程
    }
}
// semaphore + cyclicbarrier
class H2O {

    // 使用cyclicbarrier以及semaphore
    public H2O() {
        // 初始化sempO和sempH
        sempH = new Semaphore(2);
        sempO = new Semaphore(1);
    }
    private Semaphore sempO;
    private Semaphore sempH;
    private CyclicBarrier barrier = new CyclicBarrier(3, ()->{
        sempH.release(2);
        sempO.release();
    });
    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {

        // releaseHydrogen.run() outputs "H". Do not change or remove this line.
        sempH.acquire();
        releaseHydrogen.run();
        try {
            barrier.await();
        } catch (BrokenBarrierException e) {
            e.printStackTrace();
        }
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {

        // releaseOxygen.run() outputs "O". Do not change or remove this line.
        sempO.acquire();
        releaseOxygen.run();
        // 当barrier减少到1的时候，会执行cyclicbarrier中的run方法
        try{
            barrier.await();
        } catch (BrokenBarrierException e) {
            e.printStackTrace();
        }
    }
}