import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def gettotal(k):
            total = 0
            t = 0
            for i in range(len(piles)):
                rem_b = piles[i]
                rem_b = math.ceil(rem_b/ k)                     
                total = total + rem_b
            return total
        left = 1
        right = max(piles)
        while left != right:
            mid = (left + right)//2
            k = gettotal(mid)
            if k <= h:
                right = mid
            else:
                left = mid + 1
                
        return left

                

