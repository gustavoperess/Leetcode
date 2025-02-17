from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        visited = set()
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        # base cases
        # if r >= row == if row is out of bounds
        # if c >= column == if column is out of bounds
        # if in the directions that I am going to is equal 0 
        # if the index c or r is out of bounds too
        #the other condition is if row and column has been visited
      
        def dfs(r, c):
            if r >= row or c >= column or grid[r][c] == 0 or r < 0 or c < 0:
                return 1
            if (r, c) in visited:
                return 0
            
            visited.add((r,c))
            ans = 0
            for dr, dc in directions:
                ans += dfs(r + dr, c + dc)
            
            return ans
        for r in range(row):
            for c in range(column):
                if grid[r][c] == 1:
                    return dfs(r, c)
    
    
    

result = Solution()
t3 = result.islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
print(t3)