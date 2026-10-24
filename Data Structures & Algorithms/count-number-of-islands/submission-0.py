class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        col = len(grid[-1])
        visited = set()
        count = 0
        def dfs(r,c):
            if r < 0 or c <0 or r >= rows or c >= col:
                return
            if grid[r][c] == "0" or (r,c) in visited:
                return 
            visited.add((r,c))
            for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                dr = r + dr
                dc = c + dc
                dfs(dr, dc)
            
        for r in range(len(grid)):
            for c in range(len(grid[-1])):
                
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r,c) 
                    count += 1

        return count


        