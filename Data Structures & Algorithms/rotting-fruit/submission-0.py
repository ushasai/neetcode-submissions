class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        visited = []
        fresh = 0
        q = deque()
        rows = len(grid)
        cols = len(grid[-1])
        
        for r in range(len(grid)):
            for c in range(len(grid[-1])):
                
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        level = []
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                level.append((r,c))
                for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                    dr = r + dr
                    dc = c + dc
                    if dr >= rows or dc >= cols or dr < 0 or dc <0:
                        continue
                    if grid[dr][dc] == 1:
                        grid[dr][dc] = 2
                        fresh -= 1
                        q.append((dr,dc))
                        visited.append((dr,dc))
                
                level.append((dr,dc))
            minutes += 1
        
                
        return -1 if fresh > 0 else minutes

        