'''
链接：https://www.nowcoder.com/questionTerminal/a22dd98b3d224f2bb89142f8acc2fe57?answerType=1&f=discussion
来源：牛客网

平面内有n个矩形, 第i个矩形的左下角坐标为(x1[i], y1[i]), 右上角坐标为(x2[i], y2[i])。

如果两个或者多个矩形有公共区域则认为它们是相互重叠的(不考虑边界和角落)。

请你计算出平面内重叠矩形数量最多的地方,有多少个矩形相互重叠。


输入描述:
输入包括五行。
第一行包括一个整数n(2 <= n <= 50), 表示矩形的个数。
第二行包括n个整数x1[i](-10^9 <= x1[i] <= 10^9),表示左下角的横坐标。
第三行包括n个整数y1[i](-10^9 <= y1[i] <= 10^9),表示左下角的纵坐标。
第四行包括n个整数x2[i](-10^9 <= x2[i] <= 10^9),表示右上角的横坐标。
第五行包括n个整数y2[i](-10^9 <= y2[i] <= 10^9),表示右上角的纵坐标。


输出描述:
输出一个正整数, 表示最多的地方有多少个矩形相互重叠,如果矩形都不互相重叠,输出1。
示例1
输入
2
0 90
0 90
100 200
100 200
输出
2
'''

"""
重叠的区域角横坐标x必然是【x1，x2】中某个值
重叠的区域角横坐标y必然是【y1，y2】中某个值
遍历所有坐标点（x,y），由于重叠不考虑边界和角落
    在 x_range, y_range = x ± δ, y ± δ （δ< 1)
    x1[i] < x_range < x2[i] and y1[i] < y_range < y2[i] 范围内计算重叠个数
    或者 x1[i] < x <= x2[i] and y1[i] < y <= y2[i] ，等号的位置等同于上式的±号。
取所有坐标点最大的重叠个数即为所求
"""
import sys

if __name__ == "__main__":
    # sys.stdin = open('input.txt', 'r')
    n = int(input().strip())
    x1 = list(map(int, input().strip().split()))
    y1 = list(map(int, input().strip().split()))
    x2 = list(map(int, input().strip().split()))
    y2 = list(map(int, input().strip().split()))
    ans = 1
    for x in x1 + x2:  # x1+x2为一个列表
        for y in y1 + y2:  # y1+y2为一个列表
            x_range, y_range = x - 0.1, y - 0.1
            cnt = 0
            for i in range(n):
                if x1[i] < x_range < x2[i] and y1[i] < y_range < y2[i]:
                    # if x1[i] < x <= x2[i] and y1[i] < y <= y2[i]:
                    cnt += 1
            ans = max(ans, cnt)
    print(ans)

'''
链接：https://www.nowcoder.com/questionTerminal/a22dd98b3d224f2bb89142f8acc2fe57?f=discussion
注意判断重叠矩形数量最多的地方：遍历所有可能包含的点,看一下有多少矩形包含它
注：重叠数量最多的地方肯定是一块矩形区域

误区：A和B交，B和C交，但是A不和C交 --- B同时和A,C交, 但是重叠区域只为1
'''
import sys

lines = sys.stdin.readlines()
n = int(lines[0])
x1 = list(map(int, lines[1].split()))  # 左下角x
y1 = list(map(int, lines[2].split()))  # 左下角y
x2 = list(map(int, lines[3].split()))  # 右上角x
y2 = list(map(int, lines[4].split()))  # 右上角y
# 遍历所有点的组合（包含了矩形所有角以及交点），看一下有多少矩形包含它
res = 1
for x in x1 + x2:
    for y in y1 + y2:
        cnt = 0
        for i in range(n):  # 判断左下角这个点包含在多少个矩形中！
            if x > x1[i] and y > y1[i] and x <= x2[i] and y <= y2[i]:
                cnt += 1
        res = max(res, cnt)
print(res)

# Java
'''
最外两层遍历线段延长后的交点，最里层统计相交次数


链接：https://www.nowcoder.com/questionTerminal/a22dd98b3d224f2bb89142f8acc2fe57?f=discussion
想要知道某个重合区域在多少个矩形内，可以转化为计算这个重合区域的左下角在多少个矩形内。
外面两层循环遍历了所有重合区域可能的左下角，最里层循环计算这个左下角在多少个矩形内。
这个算法可以保证一定能算出正确结果，但也算了很多额外的情况，有点像充分条件的意思。
'''
'''
链接：https://www.nowcoder.com/questionTerminal/a22dd98b3d224f2bb89142f8acc2fe57?f=discussion
来源：牛客网

/*
无论何种情况，重叠区域也是四条边组成。
而且是取自与n的矩形中的四条。
所以遍历边的交点即可。
*/
import java.util.*;
 
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] x1 = new int[n];
        int[] y1 = new int[n];
        int[] x2 = new int[n];
        int[] y2 = new int[n];
        int xmin = Integer.MAX_VALUE;
        int xmax = Integer.MIN_VALUE;
        int ymin = Integer.MAX_VALUE;
        int ymax = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) 
            x1[i] = in.nextInt();
        for (int i = 0; i < n; i++) 
            y1[i] = in.nextInt();
        for (int i = 0; i < n; i++)
            x2[i] = in.nextInt();
        for (int i = 0; i < n; i++)
            y2[i] = in.nextInt();
        int ans = 0;
        int cnt = 0;
        for (int x : x1)
            for (int y : y1) {
                for (int i = 0; i < n; i++) {
                    if (x >= x1[i] && x < x2[i] && y >= y1[i] && y < y2[i])
                        cnt++;
                }
                if (cnt > ans)
                    ans = cnt;
                cnt = 0;
            }
        System.out.println(ans);
    }
}
'''

import sys

# 注意，这里是readlines不是readline,是读取多行
lines = sys.stdin.readlines()
n = int(lines[0])
x1 = list(map(int, lines[1].split()))  # 左下角x
y1 = list(map(int, lines[2].split()))  # 左下角y
x2 = list(map(int, lines[3].split()))  # 右上角x
y2 = list(map(int, lines[4].split()))  # 右上角y
res = 1  # 最少都有一个
# 确定一个左下角和右上角作为重叠区域，看这个重叠区域在多少个矩形之中
for x in x1 + x2:
    for y in y1 + y2:
        cnt = 0
        for i in range(n):
            if x > x1[i] and y > y1[i] and x <= x2[i] and y <= y2[i]:
                cnt += 1
            res = max(res, cnt)
print(res)

import sys

lines = sys.stdin.readlines()
n = int(lines[0])
x1 = list(map(int, lines[1].split()))  # 左下角x
y1 = list(map(int, lines[2].split()))  # 左下角y
x2 = list(map(int, lines[3].split()))  # 右上角x
y2 = list(map(int, lines[4].split()))  # 右上角y
res = 1  # 最少都有一个
# 确定一个左下角和右上角作为重叠区域，看这个重叠区域在多少个矩形之中
for x in x1:
    for y in y1:
        cnt = 0
        for i in range(n):
            if x >= x1[i] and x < x2[i] and y >= y1[i] and y < y2[i]:
                cnt += 1
            res = max(res, cnt)
print(res)
