n = int(input())
res = []
for i in range(n):
    lines = list(map(int, input().strip().split()))
    if lines[0] == 1:
        start = lines[1]
        num = lines[2]
        res.insert(start - 1, num)
    elif lines[0] == 2:
        start = lines[1]
        res.pop(start - 1)
    else:
        n =
        for i in res:
            print(i, end=" ")