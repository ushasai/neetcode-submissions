class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for val in stones:
            heapq.heappush(h,-val)
        while len(h) >=2 :
            first = -heapq.heappop(h)
            second = -heapq.heappop(h)
            if first != second:
                second = second - first
                heapq.heappush(h,second)
        return 0 if len(h) == 0 else -h[0]

    
        

            


        