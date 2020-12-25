'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

 

示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2

提示：你可以假定该字符串只包含小写字母。
'''

# go
'''
func firstUniqChar(s string) int {
	counts := make([]int, 26) // 长度为26

	for _, c := range s { // 遍历s，统计每个字符的出现次数
		counts[c-'a']++
	}

	for i, c := range s { // 再次遍历s，找出第一个频次为1的字符的索引
		if counts[c-'a'] == 1 {
			return i
		}
	}

	return -1 // 如果没有找到，返回-1
}
'''

