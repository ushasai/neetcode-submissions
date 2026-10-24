class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        col = len(grid[-1])
        max_area = 0
        visited = set()

        def dfs(r,c):
            area = 1

            if r < 0 or c < 0 or r >= rows or c >= col:
                return 0
            if grid[r][c] == 0 or (r,c) in visited:
                return 0
            visited.add((r,c))

            for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                dr = r + dr
                dc = c + dc
                area = area + dfs(dr, dc)
            return area
        for r in range(len(grid)):
            for c in range(len(grid[-1])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    cells = dfs(r,c)
                    max_area = max(max_area,cells)
        return max_area


