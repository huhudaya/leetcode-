''''
2.将正整数n拆分成k份，每份不为空，不考虑顺序，求划分的种类。
样例：
n = 7, k = 3;
输出：
4
{1,1,5; 1,2,4; 1,3,3; 2,2,3}
分析：
（1）分的时候至少有一个1，相当于dp[n][k] = dp[n - 1][k - 1]
（2）分的时候没有1，dp[n][k] = dp[n - k][k]
=》 dp[n][k] = dp[n - 1][k - 1] + dp[n - k][k]
'''
'''
import java.util.Scanner;
 
public class Main {
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext()){
            int n = scanner.nextInt();
            int k = scanner.nextInt();
            int [][] arr = new int [n + 1][k + 1];
            arr[0][0] = 1;
 
            for (int i = 1; i <= n; i++){
                for (int j = 1; j <= k; j++){
                    if(i >= j){
                        arr[i][j]=arr[i-j][j]+arr[i-1][j-1];
                    }
                }
            }
            System.out.println(arr[n][k]);
        }
        scanner.close();
    }
}
'''