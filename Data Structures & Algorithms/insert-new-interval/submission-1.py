class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        strt = intervals[0][0]
        end = intervals[0][1]
        merge = []

        n_s = newInterval[0]
        n_e = newInterval[1]

        for i in intervals:            
            if end >= i[0]:
                end = max(end,i[1])    
            else:
                merge.append((strt, end))
                strt = i[0]
                end = i[1]
        merge.append((strt, end))
        return merge

            
            

