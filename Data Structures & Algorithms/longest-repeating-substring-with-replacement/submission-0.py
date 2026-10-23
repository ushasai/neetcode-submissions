class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}     
        
        p1 = 0
        for p2 in range(len(s)):
            count[s[p2]] = count.get(s[p2],0) + 1
            while (p2 - p1 + 1) - max(count.values()) >k:
                count[s[p1]] -= 1
                p1 += 1

            res = max(res, p2 - p1 + 1)
                
            
        return res

        
        
                

         
        
        