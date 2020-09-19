# 003无重复最长子串.py
class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     #利用滑动窗口模板
    #     if s is None or len(s) == 0:
    #         return 0
    #     length = len(s)
    #     charArr = [0 for i in range(length)]
    #     res = 1
    #     left = 0
    #     for i in range(length):
    #         charArr[i] = ord(s[i])
    #     hash = [0 for i in range(257)]
    #     for right in range(length):
    #         # 构建hash数组
    #         hash[charArr[right]] += 1
    #         # 左指针移动的条件，左指针指向不重复
    #         while hash[charArr[right]] != 1:
    #             hash[charArr[left]] -= 1
    #             left += 1
    #         res = max(res,right - left + 1)
    #     return res
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        length = len(s)
        from collections import defaultdict
        result = 0
        # 默认初始化value为0
        hash = defaultdict(int)
        l = 0
        for r in range(length):
            hash[s[r]] += 1
            while hash[s[r]] != 1:
                hash[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result

# java
'''
class Solution {
    public int lengthOfLongestSubstring(String s) {
        // 哈希集合，记录每个字符是否出现过
        Set<Character> occ = new HashSet<Character>();
        int n = s.length();
        // 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        int rk = -1, ans = 0;
        for (int i = 0; i < n; ++i) {
            if (i != 0) {
                // 左指针向右移动一格，移除一个字符
                occ.remove(s.charAt(i - 1));
            }
            while (rk + 1 < n && !occ.contains(s.charAt(rk + 1))) {
                // 不断地移动右指针
                occ.add(s.charAt(rk + 1));
                ++rk;
            }
            // 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = Math.max(ans, rk - i + 1);
        }
        return ans;
    }
}
'''
# go
'''
func lengthOfLongestSubstring(s string) int {
    // 哈希集合，记录每个字符是否出现过
    m := map[byte]int{}
    n := len(s)
    // 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
    rk, ans := -1, 0
    for i := 0; i < n; i++ {
        if i != 0 {
            // 左指针向右移动一格，移除一个字符
            delete(m, s[i-1])
        }
        for rk + 1 < n && m[s[rk+1]] == 0 {
            // 不断地移动右指针
            m[s[rk+1]]++
            rk++
        }
        // 第 i 到 rk 个字符是一个极长的无重复字符子串
        ans = max(ans, rk - i + 1)
    }
    return ans
}

func max(x, y int) int {
    if x < y {
        return y
    }
    return x
}
'''

'''
func lengthOfLongestSubstring(s string) int {
    start,end := 0,0
    for i := 0; i < len(s); i++ {
        index := strings.Index(s[start:i],string(s[i]))
        if index==-1{
            if i+1>end{
                end=i+1
            } 
        }else{
                start+=index+1
                end+=index+1
            }
    }
    return end-start
}
'''

'''
func lengthOfLongestSubstring(s string) int {
	var Length int
	var s1 string
	left := 0
	right := 0
	s1 = s[left:right]
	for ; right < len(s); right++ {

		if index := strings.IndexByte(s1, s[right]); index != -1 {
			left += index + 1
		}
		s1 = s[left : right+1]
		if len(s1) > Length {
			Length = len(s1)
		}
	}

	return Length
}
'''

'''
func lengthOfLongestSubstring(s string) int {
    m := map[byte]int {}
    res := 0
    for i, j := 0, 0; i < len(s); i ++ {
        m[s[i]] ++
        for m[s[i]] > 1 {
            m[s[j]] --
            j ++
        }
        res = max(res, i - j + 1)
    }
    return res
}
func max (x, y int) int {
    if x > y {
        return x
    }
    return y
}
'''
