'''
排排坐，分糖果。

我们买了一些糖果 candies，打算把它们分给排好队的 n = num_people 个小朋友。

给第一个小朋友 1 颗糖果，第二个小朋友 2 颗，依此类推，直到给最后一个小朋友 n 颗糖果。

然后，我们再回到队伍的起点，给第一个小朋友 n + 1 颗糖果，第二个小朋友 n + 2 颗，依此类推，直到给最后一个小朋友 2 * n 颗糖果。

重复上述过程（每次都比上一次多给出一颗糖果，当到达队伍终点后再次从队伍起点开始），直到我们分完所有的糖果。注意，就算我们手中的剩下糖果数不够（不比前一次发出的糖果多），这些糖果也会全部发给当前的小朋友。

返回一个长度为 num_people、元素之和为 candies 的数组，以表示糖果的最终分发情况（即 ans[i] 表示第 i 个小朋友分到的糖果数）。

 

示例 1：

输入：candies = 7, num_people = 4
输出：[1,2,3,1]
解释：
第一次，ans[0] += 1，数组变为 [1,0,0,0]。
第二次，ans[1] += 2，数组变为 [1,2,0,0]。
第三次，ans[2] += 3，数组变为 [1,2,3,0]。
第四次，ans[3] += 1（因为此时只剩下 1 颗糖果），最终数组变为 [1,2,3,1]。
示例 2：

输入：candies = 10, num_people = 3
输出：[5,2,3]
解释：
第一次，ans[0] += 1，数组变为 [1,0,0]。
第二次，ans[1] += 2，数组变为 [1,2,0]。
第三次，ans[2] += 3，数组变为 [1,2,3]。
第四次，ans[0] += 4，最终数组变为 [5,2,3]。
 

提示：

1 <= candies <= 10^9
1 <= num_people <= 1000
'''
'''
时间复杂度：O(max(sqrt(G),N))
G 为糖果数量，N 为人数。

本方法的时间复杂度取决于循环到底走多少步
设总的步数为 s，用等差数列求和公式可以求得 s 步时发放的糖果数量为 s(s+1)/2 
那么只要 (s^2+s) >= 2G
糖果就可以保证被发完。

而只要当 s >= sqrt(2G)时，就有 s^2 > 2G 显然有s^2 + s >= 2G
因此可知总的步数 s <= |sqrt(2G)| 
​时间复杂度为 O(sqrt(G))
​
另外建立糖果分配数组并初值赋值需要 O(N) 的时间，因此总的时间复杂度为 O(max(sqrt(G),N))
空间复杂度:O(1)，除了答案数组只需要常数空间来存储若干变量。
'''
from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        i = 0
        while candies != 0:
            ans[i % num_people] += min(i + 1, candies)
            candies -= min(i + 1, candies)
            i += 1
        return ans

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        index = 0
        res = [0 for _ in range(num_people)]
        while candies > 0:
            for i in range(num_people):
                index += 1
                if candies - index < 0:
                    res[i] += candies
                    return res
                else:
                    candies -= index
                res[i] += index

# java
'''
class Solution {
    public int[] distributeCandies(int candies, int num_people) {
        int[] ans = new int[num_people];
        int i = 0;
        while (candies != 0) {
            ans[i % num_people] += Math.min(candies, i + 1);
            candies -= Math.min(candies, i + 1);
            i += 1;
        }
        return ans;
    }
}
'''

'''
import scala.util.control.Breaks._

object Solution {
  def distributeCandies(candies: Int, num_people: Int): Array[Int] = {
    val res = Array.fill(num_people)(0)
    var cnt = 0
    var c = candies
    while (c > 0) {
      breakable {
        (0 until num_people).foreach(i => {
          var t = num_people * cnt + i + 1
          if (c <= t) t = c
          res(i) += t
          c -= t
          if (c <= 0) break
        })
      }
      cnt += 1
    }
    res
  }
}
'''