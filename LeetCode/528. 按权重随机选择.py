'''
给定一个正整数数组 w ，其中 w[i] 代表位置 i 的权重，请写一个函数 pickIndex ，它可以随机地获取位置 i，选取位置 i 的概率与 w[i] 成正比。

例如，给定一个值 [1，9] 的输入列表，当我们从中选择一个数字时，很有可能 10 次中有 9 次应该选择数字 9 作为答案。

 

示例 1：

输入：
["Solution","pickIndex"]
[[[1]],[]]
输出：[null,0]
示例 2：

输入：
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
输出：[null,0,1,1,1,0]
输入语法说明：
输入是两个列表：调用成员函数名和调用的参数。Solution 的构造函数有一个参数，即数组 w。pickIndex 没有参数。输入参数是一个列表，即使参数为空，也会输入一个 [] 空列表。

提示：
1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex 将被调用不超过 10000 次
'''
'''
思路：
对于w[i][1,3,5,6]我们需要根据权重获取随机数，所以需要从头开始将权重值进行逐步累积，累积后数组为：[1,4,9,15]
然后使用Random产生一个[1,15]之间的随机数，如果随机数落在[1]，对应元素为0，如果随机数落在[2,4]区间，对应元素为1，如果随机数落在[5,9]区间，对应元素为2，如果随机数落在[10,15]，对应元素为4
在得出随机数后如果顺序遍历效率比较低，这里的权重累积数组是递增的，所以可以考虑使用二分法，找到随机数对应的区间。
'''

from typing import List
from random import random
import bisect


class Solution:

    def __init__(self, w: List[int]):
        probability = [0] * len(w)
        _sum = sum(w)
        cur = 0
        for i in range(len(w)):
            cur += w[i]
            probability[i] = cur / _sum
        self.probability = probability

    def pickIndex(self) -> int:
        return bisect.bisect_right(self.probability, random.random())


# java
'''
class Solution {
    //权重累加数组
    int[] arr;

    public Solution(int[] w) {
        arr = new int[w.length];
        int sum = 0;
        for (int i = 0; i < w.length; i++) {
            sum += w[i];
            arr[i] = sum;
        }
    }
    public int pickIndex() {
        //产生随机数
        Random random = new Random();
        int randomNum = random.nextInt(arr[arr.length - 1]) + 1;
        //二分查找随机数所在的区间
        int left = 0, right = arr.length - 1;
        while (left < right) {
            int mid = left + ((right - left) >> 1);
            if (arr[mid] == randomNum) {
                return mid;
            } else if (arr[mid] > randomNum) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}
'''
import itertools


class Solution:

    def __init__(self, w: List[int]):
        self.cum = list(itertools.accumulate(w))
        self.total = self.cum[-1]

    def pickIndex(self) -> int:
        target = random.randint(0, self.total - 1)
        l, r = 0, len(self.cum) - 1
        while l < r:
            mid = (l + r) // 2
            if self.cum[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return l

class Solution:
    # 常规求和再二分查找的方法，应对pick调用次数较多但数据量不大的情况
    def __init__(self, w: list):
        self.w, self.sum = [0], 0
        for i in w:
            self.sum += i
            self.w.append(self.sum)
        self.sum -= 1

    def pickIndex(self) -> int:
        w = random.randint(0, self.sum)
        return bisect.bisect(self.w, w)-1

class Solution:
    # 处理海量数据的A-res算法，应对pick调用次数较少但数据量特别大以及数据流的情况
    def __init__(self, w: list):
        self.w = w

    def pickIndex(self) -> int:
        _i, _v = 0,  float('-inf')
        for i, w in enumerate(self.w):
            v = random.random()**(1/w)
            if v > _v:
                _i, _v = i, v
        return _i

# 前缀和数组+二分
'''
class Solution {

    List<Integer> psum = new ArrayList<>();
    int tot = 0;
    Random rand = new Random();

    public Solution(int[] w) {
        for (int x : w) {
            tot += x;
            psum.add(tot);
        }
    }

    public int pickIndex() {
        int targ = rand.nextInt(tot);

        int lo = 0;
        int hi = psum.size() - 1;
        while (lo != hi) {
            int mid = (lo + hi) / 2;
            if (targ >= psum.get(mid)) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
'''
# 自己的版本
import random
import bisect
class Solution:

    def __init__(self, w: List[int]):
        n = len(w)
        pre_sum = [0] * n
        pre_sum[0] = w[0]
        for i in range(1, n):
            pre_sum[i] = pre_sum[i - 1] + w[i]
        self.tmp_sum = pre_sum[-1]
        self.pre_sum = pre_sum
        self.n = n
    def pickIndex(self) -> int:
        index = random.randint(1, self.tmp_sum)
        return bisect.bisect_left(self.pre_sum, index)
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


'''
type Solution struct {
	w   []int
	sum int
}

func Constructor(w []int) Solution {
	rand.Seed(time.Now().UnixNano())

	sum := 0
	for _, v := range w {
		sum += v
	}
	return Solution{
		w:   w,
		sum: sum,
	}
}

func (this *Solution) PickIndex() int {
	tmp := rand.Intn(this.sum)

	out := 0
	for i, v := range this.w {
		tmp -= v
		if tmp < 0 {
			out = i
			break
		}
	}
	return out
}
'''

# 自己版本的golang
'''
type Solution struct {
    PreSum []int
    Sum int
    size int
}

func Constructor(w []int) Solution {
    // 构造前缀和数组
    node := make([]int, len(w) + 1)
    for i, c := range w {
        node[i + 1] = c + node[i]
    }
    return Solution{
        PreSum:     node[1:],
        Sum:        node[len(w)],
        size:       len(w),
    }
}


func (this *Solution) PickIndex() int {
    //取[1, thie.Sum]的数:
    rand.Seed(time.Now().UnixNano())
    tmp := rand.Intn(this.Sum - 1 + 1) + 1
    left := 0
    right := this.size
    w := this.PreSum
    // 二分法找左边界
    for left + 1 < right {
        mid := left + (right - left) >> 1
        // first_position
        if w[mid] >= tmp {
            right = mid
        }else {
            left = mid
        }
    }
    if w[left] >= tmp {
        return left
    }else {
        return right
    }
}
'''