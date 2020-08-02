import sys
# n = int(input())
# nums = []
#
# for i in range(n):
#     si, ei = list(map(int, input().strip().split()))
#     nums.append([si, ei])
nums = [[1,4],[1,2],[2,3],[3,4]]
nums = [[1,2],[2,3],[5,6],[7,8]]
nums.sort(key = lambda x:x[1])
end = nums[0][1]
cnt = 0
for i in range(4):
    start = nums[i][0]
    if start >= end:
        cnt += 1
        end = nums[i][1]
print(cnt)
  10 20
  10    40
            50 60
5    15