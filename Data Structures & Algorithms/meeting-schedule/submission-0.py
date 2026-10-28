"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda i: i.start)
        strt = intervals[0].start
        end = intervals[0].end
        for i in intervals[1:]:
            
            curr_s, curr_e = i.start, i.end
            if curr_s < end:
                return False
            else:
                strt = curr_s
                end = curr_e
        return True


        
