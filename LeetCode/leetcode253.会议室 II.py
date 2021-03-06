'''
给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间
[[s1,e1],[s2,e2],...] (si < ei)
为避免会议冲突，同时要考虑充分利用会议室资源
请你计算至少需要多少间会议室，才能满足这些会议安排。

示例 1:

输入: [[0, 30],[5, 10],[15, 20]]
输出: 2
示例 2:

输入: [[7,10],[2,4]]
输出: 1
'''


# 排序
class Solution(object):
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        used_rooms = 0
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)
        j = 0
        for i in range(L):
            si = start_timings[i]
            ei = end_timings[j]
            if start_timings[i] < end_timings[j]:
                used_rooms += 1
            else:
                j += 1
        return used_rooms


# 使用优先级队列pq
'''
求所有会议时间并发的最大值即可。（思路简单粗暴，但是时间复杂度太高，取决于最大的会议结束时间）
优先队列法（堆）：我们无法按任意顺序处理给定的会议。处理会议的最基本方式是按其 开始时间 顺序排序，这也是我们采取的顺序。
按照 开始时间 对会议进行排序。
初始化一个新的 最小堆，将第一个会议的结束时间加入到堆中。我们只需要记录会议的结束时间，告诉我们什么时候房间会空。
对每个会议，检查堆的最小元素（即堆顶部的房间）是否空闲。
若房间空闲，则从堆顶拿出该元素，将其改为我们处理的会议的结束时间，加回到堆中。
若房间不空闲。开新房间，并加入到堆中。
处理完所有会议后，堆的大小即为开的房间数量。这就是容纳这些会议需要的最小房间数
'''



nums = [[1, 2], [1, 4], [5, 6], [5, 7], [5, 8]]
print(Solution().minMeetingRooms(nums))
# print(Solution().minMeetingRooms([[1,2],[2,3],[3,4],[1,4]]))
