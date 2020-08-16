'''
假设咖啡卖 5 元，每个客户可能给你 5、10、20 元的纸币，初始情况下你没有任何纸币，问是否能够找零。
如果能找零就输出 true，总用户数， 否则输出 false,失败的用户index。
例如：
5,5,5,10 => true,4
10,10 => false,1
'''
from collections import defaultdict
def isSell(nums):
    pass
    hash = defaultdict()
    for i, num in enumerate(nums):
        if num == 5:
            hash[num] += 1
        if nums == 10:
            if hash[5] > 0:
                hash[num] -= 1
            else:
                return i
        if nums == 20:
            if hash[10] > 0:
                hash[10] -= 1
            if hash[5] > 0:
                hash[5] -= 1
            else:
                return i
    return -1
