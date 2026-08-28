class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        count = {}
        for i in nums:
            count[i] = count.get(i,0) + 1
        count_s = sorted(count, key = count.get, reverse = True)
        

        return count_s[:k]

            
            

                


        