'''
洗牌在生活中十分常见，现在需要写一个程序模拟洗牌的过程。
现在需要洗2n张牌，从上到下依次是第1张，第2张，第3张一直到第2n张。
首先，我们把这2n张牌分成两堆，左手拿着第1张到第n张（上半堆），右手拿着第n+1张到第2n张（下半堆）。
接着就开始洗牌的过程，先放下右手的最后一张牌，再放下左手的最后一张牌，接着放下右手的倒数第二张牌，再放下左手的倒数第二张牌，直到最后放下左手的第一张牌。接着把牌合并起来就可以了。
例如有6张牌，最开始牌的序列是1,2,3,4,5,6。首先分成两组，左手拿着1,2,3；右手拿着4,5,6。
在洗牌过程中按顺序放下了6,3,5,2,4,1。把这六张牌再次合成一组牌之后，我们按照从上往下的顺序看这组牌，就变成了序列1,4,2,5,3,6。 现在给出一个原始牌组，请输出这副牌洗牌k次之后从上往下的序列。

输入描述:
第一行一个数T(T ≤ 100)，表示数据组数。对于每组数据，第一行两个数n,k(1 ≤ n,k ≤ 100)，接下来一行有2n个数a1,a2,…,a2n(1 ≤ ai ≤ 1000000000)。表示原始牌组从上到下的序列。

输出描述:
对于每组数据，输出一行，最终的序列。数字之间用空格隔开，不要在行末输出多余的空格。

输入例子:
3

3 1

1 2 3 4 5 6

3 2

1 2 3 4 5 6

2 2

1 1 1 1

输出例子:
1 4 2 5 3 6

1 5 4 3 2 6

1 1 1 1
'''

# 方法一
'''
import java.util.ArrayList;
import java.util.Scanner;

/**
 * 解法一：模拟洗牌法
 * 例如有6张牌，最开始牌的序列是1,2,3,4,5,6。首先分成两组，左手拿着1,2,3；右手拿着4,5,6。
 * 新建一个ArrayList,先加入1，然后4，接着依次加入 2 ， 5 ， 3 ， 6
 * 于是1,4,2,5,3,6，这就完成了一次洗牌的过程
 * k次洗牌，就把上述过程重复k次。
 * 优点： 直观易懂，模拟题中的洗牌过程。
 * 缺点： 大量运用arrayList 和数组的数字转移，且for循环次数过多，繁琐
 */
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int i = 0; i < T; i ++) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int[] arr = new int[2 * n];
            for (int j = 0; j < 2 * n; j ++) {
                arr[j] = sc.nextInt();
            }
            for (int times = 0; times < k; times ++) {
                ShuffleOnce(arr, arr.length);
            }
            for (int a = 0; a < n * 2 - 1; a ++) {
                System.out.print(arr[a] + " ");
            }
            System.out.println(arr[n * 2 - 1]);
        }
    }

    private static void ShuffleOnce(int[] arr, int n) {
        ArrayList<Integer> list = new ArrayList<>(n);
        for (int i = 0; i < n / 2; i ++) {
            list.add(arr[i]);
            list.add(arr[i + n / 2]);
        }
        for (int i = 0; i < n; i ++) {
            arr[i] = list.get(i);
        }
    }
}

'''

# 解法二：预测位置法
'''
import java.util.ArrayList;
import java.util.Scanner;

/**
 * 解法二：预测位置法
 * 每次读取一个数之后，算出他经过k次洗牌后的位置，只用一个长度为2n数组用来输出
 * 根据当前数的位置，可以算出经过一次洗牌后的位置
 * 如果当前数小于等于n（即在左手），则他下次出现的位置是 1 + (当前位置 - 1) * 2 也就是 2*当前位置-1
 * 如果当前位置大于n（即在右手）,则他下次出现的位置是 2*（当前位置 - n）
 */
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt(); //T组数据
        while (T -- > 0) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int[] arr = new int[2 * n];
            for (int i = 1; i <= 2 * n; i ++) { //数据从1开始，取到2n
                int index = i; //因为下面的while循环要多次改变i值，所以用index去替代i
               for (int j = 0; j < k; j ++){//翻转k次
                    if (index <= n) {
                        index = 2 * index - 1;
                    } else {
                        index = (index - n) * 2;
                    }
                }
                arr[index - 1] = sc.nextInt(); //放入数组
            }
            //输出
            int i;
            for (i = 0; i < 2 * n - 1; i ++) {
                System.out.print(arr[i] + " ");
            }
            System.out.println(arr[i]);
        }

    }
}
'''