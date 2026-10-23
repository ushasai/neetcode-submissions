class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        left = 0
        n = 0
        substring = []
        strings = []
        for p1 in range(len(s2)):          
            
            sub = s2[p1 : p1 + len(s1)]                
            p1 += 1
            if sorted(s1) == sorted(sub):
                return True
        return False

            
             
        