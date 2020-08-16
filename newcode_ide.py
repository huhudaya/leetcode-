n = 5
a = 2
b = 2
nums = []
alist = []
blist = []
for i in range(n):
    arr = list(map(int, input().strip().split()))
    alist.append(arr[0])
    blist.append(arr[1])
    nums.append(arr)
k = len(alist)
g = len(blist)
print(sum(alist[k - a:]) + sum(blist[g - b:]))