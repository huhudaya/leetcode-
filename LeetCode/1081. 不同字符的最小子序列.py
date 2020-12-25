'''
返回 s 字典序最小的子序列，该子序列包含 s 的所有不同字符，且只包含一次。
注意：该题与 316 https://leetcode.com/problems/remove-duplicate-letters/ 相同

示例 1：
输入：s = "bcabc"
输出："abc"

示例 2：
输入：s = "cbacdcbc"
输出："acdb"
提示：
1 <= s.length <= 1000
s 由小写英文字母组成
'''

'''
func smallestSubsequence(s string) string {
    hash := [26]int{}
    for _, c := range s {
        hash[c - 'a']++
    }
    stack := []byte{}
    inStack := [26]bool{}
    for i := range s {
        ch := s[i]
        if inStack[ch - 'a'] == false {
            for len(stack) > 0 && stack[len(stack) - 1] > ch {
                last := stack[len(stack) - 1] - 'a'
                if hash[last] == 0 {
                    break
                }
                stack = stack[:len(stack) - 1]
                // 注意，弹出一个元素的时候需要是的inStack中该元素的value变为false
                inStack[last] = false
            }
            stack = append(stack, ch)
            inStack[ch - 'a'] = true
        }
        hash[ch - 'a']--
    }
    return string(stack)
}
'''