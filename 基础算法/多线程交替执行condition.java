import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class test{

    public static void main(String[] args) {
        Resource resource = new Resource();
        new Thread(()->
        {
            for (int i = 0; i < 10; i++) {
                resource.print5();
            }
        },"A").start();

        new Thread(() -> {
            for (int i = 0; i < 10; i ++){
                resource.print10();
            }
        }, "B").start();
        new Thread(() -> {
            for (int i = 0; i < 10; i ++){
                resource.print15();
            }
        }, "C").start();
    }

}

class Resource{
    private int number = 1;
    private Lock lock = new ReentrantLock();

    private Condition condition1 = lock.newCondition();
    private Condition condition2 = lock.newCondition();
    private Condition condition3 = lock.newCondition();


    public void print5(){
        lock.lock();
        try {
            while (number != 1) {
                condition1.await();
            }
            number = 2;
            condition2.signal();
            for (int i = 0; i < 5; i ++){
                System.out.println(Thread.currentThread().getName() + "\t" + i);
            }

        } catch (Exception e){
            e.printStackTrace();
        }finally {
            lock.unlock();
        }
    }


    public void print10(){
    }
    public void print15(){
    }

}