'''
1.将正整数n无序拆分成最大数为m的拆分方案个数，要求所有拆分方案不重复。
样例：
n = 5, m = 5,对应的拆分方案如下：
5 = 5
5 = 4 + 1
5 = 3 + 2
5 = 3 + 1 + 1
5 = 2 + 2 + 1
5 = 2 + 1 + 1 + 1
5 = 1 + 1 + 1 + 1 + 1
分析：
（1）当n=1，无论m为多少，只有{1}一种划分
（2）当m=1，无论n为多少，只有{1,1,1…}一种划分
（3）当n<m，f（n，m）=f（n，n）
（4）当n=m，如果划分中有n，则只有{n}一种划分；当划分中没有n，则f（n，n）=f（n，n-1）
f（n，n）= 1 + f（n，n - 1）
（5）当n>m，如果划分中有m，则{m，{x1，x2，…} = n - m}，f（n，m）=f（n - m， m）；当划分中没有m，f（n，m）=f（n，m - 1）
f（n，m） = f（n - m， m）+ f（n，m - 1）
'''

'''
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext()){
            int n = scanner.nextInt();
            int m = scanner.nextInt();
            int temp = integerhuafen(n, m);
            System.out.print(temp);
        }      
    }
    public static int integerhuafen(int n, int m) {
         
        int dp[][] = new int[n + 1][m + 1];    
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= m; j++ ){
                if(i == 1 || j == 1){
                    dp[i][j] = 1;
                }else if (i == j) {
                    dp[i][j] = 1 + dp[i][j - 1];
                }else if (i < j) {
                    dp[i][j] = dp[i][i];
                }else {
                    dp[i][j] = dp[i - j][j] + dp[i][j - 1];
                }
            }
        }
        return dp[n][m];       
    }
}
'''