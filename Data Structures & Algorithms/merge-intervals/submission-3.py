class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        strt_idx = intervals[0][0]
        end_idx = intervals[0][1]
        intervals.sort()
        merge = []
        for i in intervals:
            
            if end_idx >= i[0]:
                end_idx = max(end_idx,i[1])              
            else:

                merge.append((strt_idx, end_idx))
                
                strt_idx, end_idx = i[0], i[1]
        
        merge.append((strt_idx, end_idx))    

        return merge
            
    


        