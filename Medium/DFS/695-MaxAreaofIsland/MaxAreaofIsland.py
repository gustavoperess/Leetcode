from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
            rows = len(grid)
            cols = len(grid[0])
            directions = [[0, 1], [0, -1], [1, 0], [-1,0]]
            visited = set()
            
            def dfs(r, c):
                #base case
                if r < 0 or c < 0 or c >= cols or r >= rows or grid[r][c] == 0 or (r,c) in visited:
                    return 0
                
                visited.add((r,c))
                area = 1
                for dr, dc in directions:
                    area += dfs(r + dr, c + dc)
                return area
                    
            maxArea = 0
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1:
                        maxArea = max(maxArea, dfs(r,c))
                        
            return maxArea

result = Solution()
t1 = result.maxAreaOfIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
t2 = result.maxAreaOfIsland(grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])
print(t2)