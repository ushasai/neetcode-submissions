class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prefix = []
        suffix = []
        prod_a = []
        for i in range(len(nums)):
            prefix.append(prod)
            prod = prod * nums[i]
            
        prod_s = 1
        for i in range(len(nums) -1, -1, -1):
            suffix.append(prod_s)
            prod_s = prod_s * nums[i]
        suffix.reverse()
        for i in range(len(nums)):
            prod_i = prefix[ i] * suffix [i]
            prod_a.append(prod_i)
        return prod_a

        