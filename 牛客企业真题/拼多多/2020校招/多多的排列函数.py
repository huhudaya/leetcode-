'''
数列 {An} 为N的一种排列。
例如N=3，可能的排列共6种：
1
2
3
4
5
6
1, 2, 3
1, 3, 2
2, 1, 3
2, 3, 1
3, 1, 2
3, 2, 1
定义函数F:
    F(1) = 1
    F(x) = |X - F(x-1)|
其中|X|表示X的绝对值。

现在多多鸡想知道，在所有可能的数列 {An} 中，F(N)的最小值和最大值分别是多少。

输入描述:
第一行输入1个整数T，表示测试用例的组数。
( 1 <= T <= 10 )
第二行开始，共T行，每行包含1个整数N，表示数列 {An} 的元素个数。
( 1 <= N <= 100,000 )

输出描述:
共T行，每行2个整数，分别表示F(N)最小值和最大值

输入例子1:
2
2
3

输出例子1:
1 1
0 2

例子说明1:
对于N=3：
- 当{An}为3，2，1时可以得到F(N)的最小值0
- 当{An}为2，1，3时可以得到F(N)的最大值2
'''

# 4个一组
def getmin(n):
    if n % 4 == 0 or n % 4 == 3:
        return 0
    else:
        return 1

def getmax(n):
    return n - getmin(n - 1)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(getmin(n), getmax(n))

'''
题目一开始没读懂，意思是：在{An}的所有排列中，能让F(N)取得的最大最小值为多少。

每四个数 例如 5，6，7，8，我们把它们两两一组 |||8-6|-7|-5|=0，最小值是0；猜测最小值的变化也是4个一组

看到min只有2种取值。0，1，最大值自然就是N-getmin(N-1)
'''
# java
'''
import java.util.Scanner;
  
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int nums = sc.nextInt();
        for (int i = 0; i<nums; i++){
            int N = sc.nextInt();
            maxandmin(N);
        }
    }
  
    public static void maxandmin(int N){
        if (N==1||N==2){
            System.out.println("1 1");
            return;
        }
        //之后每4个一组 0011
        int min = getmin(N);
        int max = N-getmin(N-1);
        System.out.println(min + " " + max);
    }
  
    public static int getmin(int N){
        int temp = (N-2)%4;
        if (temp==1 || temp==2){
            return 0;
        }
        else return 1;
    }
  
}
'''
# 找规律
# 首先F(X)肯定>=0 那么最小值肯定>=0
# 如果每四个为一组 如5 6 7 8 那么最小值不就是8-6-(7-5)=0
# 很明显是4个数可以为一组，这样的话我们可以取使得x的最后四位一定为0
# Fx的最小值=F(x%4)的最小值
# 即如果x为5 那么1 2 3 4 5 由于2 3 4 5最小值为0则F5最小值=F1
# 所以我们只要求F1 F2 F3的最小值即可
# 示例的X=1 2 3时 F(x)min分别为 1 1 0
# 很重要的一点！说F(X)的最小值不是0就是1
# 然后 F(x)=|F(x-1)-A[x]| 要想fx最大，F(x-1)肯定要最小或者最大
# F（x) max不就是在|A(x)-F(x-1)min |和|A(x)-F(x-1)max |取大值吗
# 看到min只有2种取值：0，1，最大值自然就是N-getmin(N-1)
n = int(input())
def get_min(N):
    tmp = N % 4
    if tmp == 1 or tmp == 2:
        return 1
    else:
        return 0
for i in range(n):
    num = int(input())
    min_num = get_min(num)
    max_num = num - get_min(num - 1)
    print(min_num, max_num)