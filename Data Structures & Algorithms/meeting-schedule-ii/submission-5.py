"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i: i.start)   # process meetings in start order
        ends = []                               # min-heap: end time of each busy room

        for i in intervals:
            if ends and ends[0] <= i.start:     # the earliest-ending room is free by now
                heapq.heappop(ends)             #   → free it (this meeting reuses it)
            heapq.heappush(ends, i.end)         # this meeting occupies a room until i.end

        return len(ends)                        # rooms needed at the busiest point