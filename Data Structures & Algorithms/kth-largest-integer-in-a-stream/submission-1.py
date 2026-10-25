class KthLargest:
    
    

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = []
        self.nums = nums
        
        for n in self.nums:
            self.add(n)
               
     
    def add(self, val: int) -> int:
        
        heapq.heappush(self.h, val)

        if len(self.h) > self.k:
            heapq.heappop(self.h)
        if not self.h:
            return 0
        return self.h[0]
         

        
