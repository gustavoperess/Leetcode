
from typing import List

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        INF = float('inf')
        dist = [[INF] * cols for _ in range(rows)]
        
        def dfs(r, c, d):
            if r < 0 or c < 0 or r >= rows or c >= cols or dist[r][c] <= d or dist[r][c] == 2:
                return
            dist[r][c] = d
            print(dist)
         
            for dr, dc in directions:
                dfs(r + dr, c + dc, d +1)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    dfs(r, c, 0)
        


result = Solution()
# result.shortestDistance(grid = [[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
result.shortestDistance(grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]])