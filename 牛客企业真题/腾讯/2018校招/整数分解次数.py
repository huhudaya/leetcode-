'''
题目
如下示例：
1：共0种分解方法；
2：共0种分解方法；
3：3=2+1 共1种分解方法；
4：4=3+1=2+1+1 共2种分解方法；
5：5=4+1=3+2=3+1+1=2+2+1=2+1+1+1 共5种分解方法
6：6=5+1=4+2=4+1+1=3+2+1=3+1+1+1=2+2+1+1=2+1+1+1+1 共7种分解方法
以此类推，求一任意整数num有几种分解方法？
输入一个数字（1到90），输出该整数的分解方法个数
如：
输入：2——输出：0
输入：3——输出：1
输入：5——输出：5
注意：整数不能分解为两个一样的数字，比如2 != 1+1
'''
# https://www.cnblogs.com/xuehaoyue/p/6660315.html
# Java
'''
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()){
            int num = sc.nextInt();
            int result = 0;

            int[][] arr = new int[num+1][];
            for(int i = 3; i <= num; i++){
                int columnNum = (int)Math.floor((i-1)/2d);
                arr[i] = new int[columnNum];
                for(int j = 0; j < columnNum; j++){
                    arr[i][j] = 1;
                    int num2 = j + 1;
                    int num1 = i - num2;
                    if(num1 > 2 * num2){//只有这种情况才分解
                        if(num1 % 2 == 0){//num1是偶数，计算分解情况时+1
                            arr[i][j]++;
                        }
                        //计算数1的分解情况
                        for (int k = j; k < arr[num1].length; k++){
                            arr[i][j] += arr[num1][k];
                        }

                    }
                }

            }
//            输出整个二维数组的情况
//            for(int i = 3; i <= num; i++){
//                for(int j = 0; j < arr[i].length;j++){
//                    System.out.println("arr["+i+"]["+j+"] is: "+arr[i][j]);
//                }
//            }
            if(num == 1 || num == 2) result = 0;
            else{
                for(int i = 0; i < arr[num].length;i++){
                    result += arr[num][i];
                }
            }
            System.out.println(result);
        }
    }
}
'''
