import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        result = []
        for n in points:
            x = n[0]
            y = n[1]
            d = math.sqrt(((x-0)*(x-0)) + ((y -0)*(y-0)))
            heapq.heappush(h,(d,(x,y)))
        for _ in range(k):
            d, p = heapq.heappop(h)
            result.append(list(p))

        return result
