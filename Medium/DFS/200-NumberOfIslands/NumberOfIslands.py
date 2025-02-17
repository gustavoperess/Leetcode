
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        directions = [[0,1], [0,-1], [1,0], [-1, 0]]
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= columns or grid[r][c] == "0" or (r,c) in visited:
                return 0
            
            visited.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
        
        numIslands = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r, c)
                    numIslands += 1
        return numIslands

result = Solution()
result.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])

result.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])