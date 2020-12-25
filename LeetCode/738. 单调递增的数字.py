'''

给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。

（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）

示例 1:
输入: N = 10
输出: 9

示例 2:
输入: N = 1234
输出: 1234

示例 3:
输入: N = 332
输出: 299

n   = 1234321
res = 1233999

n    = 2333332
res  = 2299999

说明: N 是在 [0, 10^9] 范围内的一个整数。
'''

# java
'''
【思路】
从左往右遍历各位数字，找到第一个开始下降的数字[i]，将[i]减1，然后将[i+1 ...]各位数字全部置为9即可
例如：1232123，从左往右遍历，找到第一个开始下降的数字3，将3改为2，然后将后面所有数字全部置为9，最后为：1229999 即为答案
【需要注意一点】：如果第一个开始下降的数字[i]，前面还有与其相等的数字，需要找到最前面的一个数字作为上面所说的[i]
例如：13332，从左往右遍历，找到第一个开始下降的数字3，往前再看下，是否还有等于3的数字，找到最前面那个3，将3改为2，然后将后面的各个数字置为9，最后为：12999
'''

# 循环执行次数为N的位数，而N的位数为log10 N，渐进时间复杂度去掉系数就是O(lg N)了
# 注意这个N是指数字的大小是N，这样N的位数为log10 N
'''
class Solution {
    /**
     * 思路：
     *  从右向左扫描数字，若发现当前数字比其左边一位（较高位）小，
     *  则把其左边一位数字减1，并将该位及其右边的所有位改成9
     */
    public static int monotoneIncreasingDigits(int n) {
        String s = String.valueOf(n);
        int length = s.length();
        char[] chars = s.toCharArray();
        int flag = length;
        for (int i = length - 1; i >= 1; i--) {
            if (chars[i] < chars[i - 1]) {
                flag = i;
                chars[i - 1]--;
            }
        }

        for (int i = flag; i < length; i++) {
            chars[i] = '9';
        }
        return Integer.parseInt(new String(chars));

    }

}
'''


# c++
'''
class Solution {
public:
    int monotoneIncreasingDigits(int N) {
        string strNum = to_string(N);
        // flag用来标记赋值9从哪里开始
        // 设置为这个默认值，为了防止第二个for循环在flag没有被赋值的情况下执行
        int flag = strNum.size();
        for (int i = strNum.size() - 1; i > 0; i--) {
            if (strNum[i - 1] > strNum[i] ) {
                flag = i;
                strNum[i - 1]--;
            }
        }
        for (int i = flag; i < strNum.size(); i++) {
            strNum[i] = '9';
        }
        return stoi(strNum);
    }
};
'''

# java
# 事件复杂度为logN
'''
public int monotoneIncreasingDigits(int N) {
        int res = 0;
        // 倍数
        int seed = 1;
        while (N > 0) {
            int num = N % 10;
            N /= 10;
            int high = N % 10;
            if (high > num) {
                // 高位大于低位，将低位全部置为9，高位数字-1
                res = seed*10 - 1;
                N -= 1;
            }else  {
                res = num * seed + res;
            }
            seed *= 10;
        }
        return res;
    }
'''

# GO
'''
func monotoneIncreasingDigits(N int) int {
	if N < 10 {
		//如果N是一位数，直接返回
		return N
	}
	num := []byte(strconv.Itoa(N))
	index, is := isIncrease(num)	//判断数字是否本身就符合递增
	if is {
		return N
	}
	//如果本身不是递增的，则最小递增位置数字减一
	num[index]--
	//最小递增位置后面的位置全部改成9
	for i := index + 1; i < len(num); i++ {
		num[i] = '9'
	}

	n, _ := strconv.Atoi(string(num))
	return n
}

func isIncrease(num []byte) (int, bool) {
	index, is := 0, true
	for i := 1; i < len(num); i++ {
		if num[i] < num[index] {
			is = false
			break
		} else if num[i] > num[index] {
			index = i
		}
	}
	return index, is
}
'''

'''
func monotoneIncreasingDigits(N int) int {
    res := 0
	// 从低位往高位遍历
	for i := 1; i <= N; i *= 10 {
		// 获取当前位的数字
		pos := N/i%10
		// 如果有更高位的数值且比当前位大，进行削弱
		if N >= i*10 && (N/i/10)%10 > pos {
			// 削弱后给后继位修改值
			N -= i*10
			res = 0
			for j := i; j > 0; j /= 10 {
				res += j*9
			}
		} else {
			res += pos*i
		}
	}
	return res
}
'''


# 贪心golang
'''
func monotoneIncreasingDigits(N int) int {
    strNum := strconv.Itoa(N)
    ss := []byte(strNum)
    n := len(ss)
    flag := n
    for i := n - 1; i > 0; i-- {
        if ss[i] < ss[i - 1] {
            ss[i - 1]--
            flag = i
        }
    }
    for i := flag; i < n; i++ {
        ss[i] = '9'
    }
    // ascii to intege
    res, _ := strconv.Atoi(string(ss))
    return res
}
'''