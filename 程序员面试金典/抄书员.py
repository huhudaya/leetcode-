# copyBooks
'''
	info
		给定 n 本书, 第 i 本书的页数为 pages[i].
	    现在有 k 个人来复印这些书籍, 而每个人只能复印编号连续的一段的书
		比如一个人可以复印 pages[0], pages[1], pages[2], 但是不可以只复印 pages[0], pages[2], pages[3] 而不复印 pages[1].

		所有人复印的速度是一样的, 复印一页需要花费一分钟, 并且所有人同时开始复印.
		怎样分配这 k 个人的任务, 使得这 n 本书能够被尽快复印完?

		返回完成复印任务最少需要的分钟数.
'''
'''
	case
		输入: pages = [3, 2, 4], k = 2
		输出: 5
		解释: 第一个人复印前两本书, 耗时 5 分钟. 第二个人复印第三本书, 耗时 4 分钟.
	case 
		输入: 1,3,3,3 k=2
		输出: 
'''

'''	
	思路:
		注意，如果给定一个分钟数，
		要求分配的每个人工作的分钟数小于这个给定的分钟
		则需要分配的人数是一定的，这里我们通过一个函数实现
		注意这里最少需要max(pages)分钟
		1.计算得到start和end，start=max(list),end=sum(list)
		2.通过二分法计算得到一个分钟数，计算这个分钟需要分配几个人，这样就将问题划分为OOXX问题
		3.

'''
# 时间复杂度O(N*logM)
# 好题呀！！！
# 画图，画出坐标轴
# 限制的分钟是从start到end
'''	
	比如:
		4,5,6,7,8,9是限制的分钟数
		则对应需要的人数是:
		5,5,4,k,k,k,1,1
		所以需要求>=k的first位置，即对应的分钟数最少的，即7
		即给的分钟越多，需要的人越少，给的分钟越少，需要的人就越少哦

'''
'''
	注意点
		注意max和min
		因为只能一个人整本整本抄书，所以需要最低的是max(arr)，因为最少也需要分钟最多的。对多的是sum(arr)
		比如3，66，2 最少也需要66分钟，即两个人即可，最多则需要66+3+2=71，即1个人完成
'''


def copyBooks(pages, k):
    if len(pages) == 0:
        return 0
    total = 0
    maxNum = pages[0]
    for i in pages:
        total += i
        maxNum = max(i, maxNum)
    # print('max:' ,maxNum)
    # print('total:' ,total)
    start = maxNum
    end = total
    # start,end = max(pages),sum(pages)
    while start + 1 < end:
        mid = start + (end - start) // 2
        # 分钟越少，需要的人越多，所以取firstPostition
        # 找firsPosition，所以end在前面,相当于取count<=k部分的firstPosition
        if countCopier(pages, mid) <= k:
            end = mid
        else:
            start = mid
        # 因为是求firstPosition，所以先比较start
    if countCopier(pages, start) <= k:
        return start
    if countCopier(pages, end) <= k:
        return end
    return -1


# countCopier函数用来计算所需要的人数
# 注意一定要指定，copiers的初始值是1
def countCopier(pages, limit):
    if len(pages) == 0:
        return 0
    copiers = 1
    # 定义sum为
    sum = 0
    for i in pages:
        if (sum + i) > limit:
            copiers += 1
            sum = 0
        sum += i
    return copiers


print(countCopier([888, 2], 3))

# 或者也可以从1开始遍历
# def countCopier(pages,limit):
# 	if len(pages) == 0:
# 		return 0
# 	copiers = 1
# 	sum = pages[0]
# 	for i in range(1,len(pages)):
# 		print(i)
# 		if (sum+pages[i]) > limit:
# 			copiers += 1
# 			sum = 0
# 		sum += pages[i]
# 	return copiers

pages = [888888, 2, 4]
print(copyBooks(pages, 2))
