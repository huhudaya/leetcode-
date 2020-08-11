/**

我们提供一个类：
class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}

两个不同的线程将会共用一个 FooBar 实例。其中一个线程将会调用 foo() 方法，另一个线程将会调用 bar() 方法。
请设计修改程序，以确保 "foobar" 被输出 n 次。
示例 1:
输入: n = 1
输出: "foobar"
解释: 这里有两个线程被异步启动。其中一个调用 foo() 方法, 另一个调用 bar() 方法，"foobar" 将被输出一次。
示例 2:
输入: n = 2
输出: "foobarfoobar"
解释: "foobar" 将被输出两次。
**/

//方案一：Semaphore 信号量
class FooBar {
    private int n;

    public FooBar(int n) {
        this.n = n;
    }
    // 哪一个需要先打印，就将哪个semaphore的值置为1
    Semaphore foo = new Semaphore(1);
    Semaphore bar = new Semaphore(0);

    public void foo(Runnable printFoo) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            foo.acquire();
            printFoo.run();
            bar.release();
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            bar.acquire();
            printBar.run();
            foo.release();
        }
    }
}
//方案二：Lock（公平锁）
class FooBar {
    private int n;

    public FooBar(int n) {
        this.n = n;
    }

    Lock lock = new ReentrantLock(true);
    volatile boolean permitFoo = true;

    public void foo(Runnable printFoo) throws InterruptedException {
        for (int i = 0; i < n; ) {
            lock.lock();
            try {
            	if(permitFoo) {
                    // printFoo.run() outputs "foo". Do not change or remove this line.
            	    printFoo.run();
                    i++;
                    permitFoo = false;
            	}
            }finally {
            	lock.unlock();
            }
        }
    }
    public void bar(Runnable printBar) throws InterruptedException {
        for (int i = 0; i < n; ) {
            lock.lock();
            try {
            	if(!permitFoo) {
            	    // printFoo.run() outputs "foo". Do not change or remove this line.
            	    printBar.run();
            	    i++;
            	    permitFoo = true;
            	}
            }finally {
            	lock.unlock();
            }
        }
    }
}

// 方法三：使用一个CountDownLatch和一个CyclicBarrier解决

import java.util.concurrent.CountDownLatch;
import java.util.concurrent.CyclicBarrier;
class FooBar {
    private int n;
    private CountDownLatch a;
    private CyclicBarrier barrier;// 使用CyclicBarrier保证任务按组执行
    public FooBar(int n) {
        this.n = n;
        a = new CountDownLatch(1);
        barrier = new CyclicBarrier(2);// 保证每组内有两个任务
    }

    public void foo(Runnable printFoo) throws InterruptedException {

        try {
            for (int i = 0; i < n; i++) {
                printFoo.run();
                a.countDown();// printFoo方法完成调用countDown
                barrier.await();// 等待printBar方法执行完成
            }
        } catch(Exception e) {}
    }

    public void bar(Runnable printBar) throws InterruptedException {

        try {
            for (int i = 0; i < n; i++) {
                a.await();// 等待printFoo方法先执行
                printBar.run();
                a = new CountDownLatch(1); // 保证下一次依旧等待printFoo方法先执行
                barrier.await();// 等待printFoo方法执行完成 当barrier减少到0的时候，才会继续执行
            }
        } catch(Exception e) {}
    }
}

// 方法四：使用condition实现精确唤醒
class FooBar {
    private ReentrantLock lock = new ReentrantLock();
    private Condition fooCondition = lock.newCondition();
    private Condition barCondition = lock.newCondition();
    private int count = 1;
    private int n;

    public FooBar(int n) {
        this.n = n;
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            lock.lock();
            if(count != 1) {
                fooCondition.await();
            }
            // printFoo.run() outputs "foo". Do not change or remove this line.
        	printFoo.run();
            barCondition.signal();
            count=2;
            lock.unlock();
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            lock.lock();
            if(count != 2) {
                barCondition.await();
            }
            // printBar.run() outputs "bar". Do not change or remove this line.
        	printBar.run();
            fooCondition.signal();
            count=1;
            lock.unlock();
        }
    }
}

// 方法五：使用synchronize
class FooBar {
        private int n;
	    private volatile boolean isFoo;

	    public FooBar(int n) {
	        this.n = n;
	    }

	    public synchronized void foo(Runnable printFoo) throws InterruptedException {

	        for (int i = 0; i < n; i++) {
	            // printFoo.run() outputs "foo". Do not change or remove this line.
	            printFoo.run();
	            isFoo = true;
	            this.notify();
	            if (i < n - 1) {
	                this.wait();
	            }
	            //            }
	        }
	    }

	    public synchronized void bar(Runnable printBar) throws InterruptedException {
	        if (!isFoo) {
	            this.wait();
	        }
	        for (int i = 0; i < n; i++) {
	            //            synchronized (lock) {
	            // printBar.run() outputs "bar". Do not change or remove this line.
	            printBar.run();
	            this.notify();
                // 必须先唤醒在阻塞当前线程
                if (i < n - 1) {
	                this.wait();
	            }
	            //            }
	        }
	    }
}