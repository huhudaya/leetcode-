
// 方法一，使用CAS
class Foo {

  private AtomicInteger firstJobDone = new AtomicInteger(0);
  private AtomicInteger secondJobDone = new AtomicInteger(0);

  public Foo() {}

  public void first(Runnable printFirst) throws InterruptedException {
    // printFirst.run() outputs "first".
    printFirst.run();
    // mark the first job as done, by increasing its count.
    firstJobDone.incrementAndGet();
  }

  public void second(Runnable printSecond) throws InterruptedException {
    while (firstJobDone.get() != 1) {
      // waiting for the first job to be done.
    }
    // printSecond.run() outputs "second".
    printSecond.run();
    // mark the second as done, by increasing its count.
    secondJobDone.incrementAndGet();
  }

  public void third(Runnable printThird) throws InterruptedException {
    while (secondJobDone.get() != 1) {
      // waiting for the second job to be done.
    }
    // printThird.run() outputs "third".
    printThird.run();
  }
}
//方法二，使用synchronized
// 多线程编程的三要素，判断 干活 通知，高内聚情况下，线程操作资源类
public class Foo {
    //控制变量
    private int flag = 0;
    //定义Object对象为锁
    private Object lock = new Object();
    public Foo() {
    }
    public void first(Runnable printFirst) throws InterruptedException {
        //sync已经是一个原子性操作
        synchronized (lock){
            //如果flag不为0则让first线程等待，while循环控制first线程如果不满住条件就一直在while代码块中，防止出现中途跳入，执行下面的代码，其余线程while循环同理
            while( flag != 0){
                //wait的时候已经释放了锁
                lock.wait();
            }
            // printFirst.run() outputs "first". Do not change or remove this line.
            printFirst.run();
            //定义成员变量为 1
            flag = 1;
            //唤醒其余所有的线程
            lock.notifyAll();
        }
    }
    public void second(Runnable printSecond) throws InterruptedException {
        synchronized (lock){
            //如果成员变量不为1则让二号等待
            while (flag != 1){
                lock.wait();
            }
            // printSecond.run() outputs "second". Do not change or remove this line.
            printSecond.run();
            //如果成员变量为 1 ，则代表first线程刚执行完，所以执行second，并且改变成员变量为 2
            flag = 2;
            //唤醒其余所有的线程
            lock.notifyAll();
        }
    }
    public void third(Runnable printThird) throws InterruptedException {
        synchronized (lock){
            //如果flag不等于2 则一直处于等待的状态
            while (flag != 2){
                lock.wait();
            }
            // printThird.run() outputs "third". Do not change or remove this line.
            //如果成员变量为 2 ，则代表second线程刚执行完，所以执行third，并且改变成员变量为 0
            printThird.run();
            flag = 0;
            lock.notifyAll();
        }
    }
}
//使用countdownlatch
public class Foo {
    //声明两个 CountDownLatch变量
    private CountDownLatch countDownLatch01;
    private CountDownLatch countDownLatch02;

    public Foo() {
        //初始化每个CountDownLatch的值为1，表示有一个线程执行完后，执行等待的线程
        countDownLatch01 = new CountDownLatch(1);
        countDownLatch02 = new CountDownLatch(1);
    }
    public void first(Runnable printFirst) throws InterruptedException {
            //当前只有first线程没有任何的阻碍，其余两个线程都处于等待阶段
            // printFirst.run() outputs "first". Do not change or remove this line.
            printFirst.run();
            //直到CountDownLatch01里面计数为0才执行因调用该countDownCatch01.await()而等待的线程
            countDownLatch01.countDown();
    }
    public void second(Runnable printSecond) throws InterruptedException {
            //只有countDownLatch01为0才能通过，否则会一直阻塞
            countDownLatch01.await();
            // printSecond.run() outputs "second". Do not change or remove this line.
            printSecond.run();
            //直到CountDownLatch02里面计数为0才执行因调用该countDownCatch02.await()而等待的线程
            countDownLatch02.countDown();
    }
    public void third(Runnable printThird) throws InterruptedException {
            //只有countDownLatch02为0才能通过，否则会一直阻塞
            countDownLatch02.await();
            // printThird.run() outputs "third". Do not change or remove this line.
            printThird.run();
    }
}

//使用Semaphore变量
public class Foo03 {
    //声明两个 Semaphore变量
    private Semaphore spa,spb;
    public Foo03() {
        //初始化Semaphore为0的原因：如果这个Semaphore为零，如果另一线程调用(acquire)这个Semaphore就会产生阻塞，便可以控制second和third线程的执行
        spa = new Semaphore(0);
        spb = new Semaphore(0);
    }
    public void first(Runnable printFirst) throws InterruptedException {
            // printFirst.run() outputs "first". Do not change or remove this line.
            printFirst.run();
            //只有等first线程释放Semaphore后使Semaphore值为1,另外一个线程才可以调用（acquire）
            spa.release();
    }
    public void second(Runnable printSecond) throws InterruptedException {
            //只有spa为1才能执行acquire，如果为0就会产生阻塞
            spa.acquire();
            // printSecond.run() outputs "second". Do not change or remove this line.
            printSecond.run();
            spb.release();
    }
    public void third(Runnable printThird) throws InterruptedException {
            //只有spb为1才能通过，如果为0就会阻塞
            spb.acquire();
            // printThird.run() outputs "third". Do not change or remove this line.
            printThird.run();
    }
}


 private static void FooTest01() throws InterruptedException{
        Foo foo = new Foo();
        Thread thread1 = new Thread(() -> {
            try {
                foo.first(() -> {
                    System.out.println("one");

                });
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        Thread thread2 = new Thread(() -> {
            try {
                foo.second(() -> {
                    System.out.println("two");
                });
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        Thread thread3 = new Thread(() -> {
            try {
                foo.third(() -> {
                    System.out.println("third");
                });
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        thread1.start();
        thread2.start();
        thread3.start();
    }
    public static void main(String[] args) throws InterruptedException{
        FooTest01();
    }