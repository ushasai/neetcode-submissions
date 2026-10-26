class Solution:
    def pacificAtlantic(self, heights):
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prev_height):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if (r, c) in visited or heights[r][c] < prev_height:
                return
            visited.add((r,c))
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(r + dr, c + dc, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])               # top row → Pacific
            dfs(rows - 1, c, atlantic, heights[rows-1][c])  # bottom row → Atlantic
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])                   # left column → ?
            dfs(r, cols - 1, atlantic, heights[r][cols-1])       # right column → ?

        return [list(cell) for cell in pacific & atlantic]