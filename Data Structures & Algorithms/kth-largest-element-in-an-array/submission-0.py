class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            heapq.heappush(h, n)
        while len(h) > k:
            heapq.heappop(h)
        if not h:
            return None
        return h[0]
        