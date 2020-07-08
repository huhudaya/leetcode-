'''
为了找到自己满意的工作，牛牛收集了每种工作的难度和报酬。牛牛选工作的标准是在难度不超过自身能力值的情况下，牛牛选择报酬最高的工作。在牛牛选定了自己的工作后，牛牛的小伙伴们来找牛牛帮忙选工作，牛牛依然使用自己的标准来帮助小伙伴们。牛牛的小伙伴太多了，于是他只好把这个任务交给了你。

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含两个正整数，分别表示工作的数量N(N<=100000)和小伙伴的数量M(M<=100000)。
接下来的N行每行包含两个正整数，分别表示该项工作的难度Di(Di<=1000000000)和报酬Pi(Pi<=1000000000)。
接下来的一行包含M个正整数，分别表示M个小伙伴的能力值Ai(Ai<=1000000000)。
保证不存在两项工作的报酬相同。

输出描述:
对于每个小伙伴，在单独的一行输出一个正整数表示他能得到的最高报酬。一个工作可以被多个人选择。

输入例子1:
3 3------>N,M
1 100
10 1000
1000000000 1001
9 10 1000000000

输出例子1:
100
1000
1001
'''
# Java
'''
public class MainCorrect {

    public static void main(String[] args) {
        //划重点！！！此题坑点：输入中间有空行，所以用BuffferedReader会更麻烦，所以选择用Scanner
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        //保存所有工作的键值对，即<工作能力，报酬>，而且也保存每个小伙伴的能力值键值对，其报酬为0
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        //保存所有工作的能力值以及要计算的每个小伙伴的能力值
        int[] ai = new int[m + n];
        for(int i = 0; i < n; i++) {
            int di = sc.nextInt();
            ai[i] = di;
            int pi = sc.nextInt();
            map.put(di, pi);
        }
        //保存要计算的每个小伙伴的能力值
        int[] bi = new int[m];
        for(int i = 0; i < m; i++) {
            ai[i + n] = sc.nextInt();
            bi[i] = ai[i + n];
            if(!map.containsKey(ai[i + n])) {
                map.put(ai[i + n], 0);
            }
        }
        //对能力值进行排序
        Arrays.sort(ai);
        //保存到目前的能力值为止，所能获得的最大报酬，有种dp的味道
        int ma = 0;
        for(int i = 0; i < m + n; i++) {
            //每次都更新当前能力值所对应的最大报酬，由于ma是保存的<=当前能力值所能获得的最大报酬，所以可行
            ma = Math.max(ma, map.get(ai[i])); //因为已经排好序了，相当于和前一个最大值进行比较
            map.put(ai[i], ma);
        }
        //遍历每个小伙伴的能力值，从map中获取到其最大报酬（在上面的for循环中已经更新到了）
        for(int i = 0; i < m; i++) {
            System.out.println(map.get(bi[i]));
        }
    }

}
'''

# 超时，两层for循环
'''
public class Main {

    //用一个类来记录工作能力和报酬的对应关系，其实可以用map实现的
    static class Job implements Comparable<Job>{
        int di, pi;
        public Job(int di, int pi) {
            this.di = di;
            this.pi = pi;
        }
        //按工作能力值进行排序
        public int compareTo(Job job) {
            return this.di - job.di;
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        Job[] jobs = new Job[n];
        for(int i = 0; i < n; i++) {
            int di = sc.nextInt();
            int pi = sc.nextInt();
            jobs[i] = new Job(di, pi);
        }
        //对工作能力进行排序
        Arrays.sort(jobs);
        int[] ai = new int[m];
        for(int i = 0; i < m; i++) {
            ai[i] = sc.nextInt();
        }
        //逐一计算每个小伙伴，在其工作能力之内所能获得的最大报酬
        for(int i = 0; i < m; i++) {
            int j = 0;
            int cnt = 0;
            while(j < n && jobs[j].di <= ai[i]) {
                if(cnt < jobs[j].pi) {
                    cnt = jobs[j].pi;
                }
                j++;
            }
            System.out.println(cnt);
        }
    }

}
'''
# 二分
'''
解题思路：
自定义一个类Work来描述工作
所有的Work存入works数组中，根据工作的难度对works从小到大排序
定义一个dp数组，dp[i]表示难度小于等于works[i]的最大报酬。
对于输入的能力值，使用二分查找，扫描works数组，找到works数组中小于等于指定能力值，且下标最大的Work。
记该Work的下标为index
dp[index]就是结果
        // dp[i]:记录难度小于等于works[i].difficulty的最大报酬
        dp[0] = works[0].reward;
        for (int i = 1; i < works.length; i++) {
            dp[i] = dp[i - 1] > works[i].reward ? dp[i - 1] : works[i].reward;
        }
'''
# Java
'''
import java.util.Scanner;
import java.util.Arrays;
import java.util.Comparator;
class Work {
    int difficulty;
    int reward;
 
    public Work(int difficulty, int reward) {
        super();
        this.difficulty = difficulty;
        this.reward = reward;
    }
 
}
 
public class Main {
 
    public static void main(String[] args) {
        findwork();
    }
 
    public static void findwork() {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();// 工作数量
        int m = in.nextInt();// 人数
 
        Work[] works = new Work[n];// 存储n份工作
        int[] dp = new int[n];// dp[n]:难度小于等于works[n].difficulty的工作的最高报酬
        // 读入n份工作
        for (int i = 0; i < n; i++) {
            int difficulty = in.nextInt();
            int reward = in.nextInt();
            Work work = new Work(difficulty, reward);
            works[i] = work;
        }
        // 根据工作的难度，对n份工作从小到大排序
        Arrays.sort(works, new Comparator<Work>() {
 
            @Override
            public int compare(Work o1, Work o2) {
                return o1.difficulty - o2.difficulty;
            }
        });
        // dp[i]:记录难度小于等于works[i].difficulty的最大报酬
        dp[0] = works[0].reward;
        for (int i = 1; i < works.length; i++) {
            dp[i] = dp[i - 1] > works[i].reward ? dp[i - 1] : works[i].reward;
        }
 
        for (int i = 0; i < m; i++) {
            int capability = in.nextInt();
            // 能力值小于所有的工作的难度
            if (capability < works[0].difficulty) {
                System.out.println(0);
                continue;
            }
            // 能力值大于等于所有的工作的难度
            if (capability >= works[n - 1].difficulty) {
                System.out.println(dp[n - 1]);
                continue;
            }
            // 二分查找,找到第一个小于capability的work
            int low = 0;
            int high = n - 1;
            while (low <= high) {
                int middle = (low + high) / 2;
 
                // works[middle]是符合能力值，且难度最大的工作
                if (works[middle].difficulty <= capability && works[middle + 1].difficulty > capability) {
                    System.out.println(dp[middle]);
                    break;
                }
                // 找到难度等于能力值，且下标最大的工作
                if (works[middle].difficulty == capability) {
                    // 找到最后一个符合capability的工作
                    int index = middle;
                    while (index + 1 < n && works[index + 1].difficulty == capability) {
                        index++;
                    }
                    System.out.println(dp[middle]);
                    break;
                } else if (capability > works[middle].difficulty) {
                    low = middle + 1;
                } else if (capability < works[middle].difficulty) {
                    high = middle - 1;
                }
            }
        }
    }  
}
'''

# 自己的版本
import sys

n, m = list(map(int, input().strip().split()))
di = []
map = dict()
for i in range(n):
    line = sys.stdin.readline()
    d, p = [int(i) for i in line.strip().split()]
    di.append(d)
    map[d] = p
cap = [int(i) for i in input().strip().split()]
# cap = [9, 10, 1000000000]
for i in cap:
    di.append(i)
    if i not in map:
        map[i] = 0
di.sort()
# dp
dp = [0 for i in range(m + n)]
dp[0] = map[di[0]]
for i in range(1, m + n):
    dp[i] = max(map[di[i]], dp[i - 1])
    map[di[i]] = dp[i]
for i in cap:
    print(map[i])

import sys


def main():
    lines = sys.stdin.readlines()
    lines = [l.strip().split() for l in lines if l.strip()]
    n, m = int(lines[0][0]), int(lines[0][1])
    res = [0] * (n + m)
    abilities = list(map(int, lines[-1]))
    maps = dict()
    for index, l in enumerate(lines[1:-1]):
        d, s = int(l[0]), int(l[1])
        maps[d] = s
        res[index] = d
    for index, ability in enumerate(abilities):
        res[index + n] = ability
        if ability not in maps:
            maps[ability] = 0
    res.sort()
    maxSalary = 0
    for index in range(n + m):
        maxSalary = max(maxSalary, maps[res[index]])
        maps[res[index]] = maxSalary
    for index in range(m):
        print(maps[abilities[index]])


if __name__ == '__main__':
    main()
