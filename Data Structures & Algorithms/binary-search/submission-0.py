class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            m = (left + right) // 2 
            if target == nums[m]:
                return m
            if target > nums[m]:
                left = m + 1
            elif target < nums[m]:
                right = m - 1
        return -1