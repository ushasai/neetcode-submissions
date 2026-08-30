class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 
        length = 0
        set_s = set(nums)
        for x in set_s:
            if x-1 not in set_s:
                current = x
                length = 1
                while current+1 in set_s:
                        length += 1
                        current += 1
            longest = max(longest, length) 
        return longest





                    
            
           
        