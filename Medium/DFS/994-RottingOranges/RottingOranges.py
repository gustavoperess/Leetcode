from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # DFS DOES NOT WORK NEED TO COME BACK
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(r, c, minutes):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or grid[r][c] == 0:
                return minutes
            
            visited.add((r, c))
            grid[r][c] = 2  
            
            max_minutes = minutes  
       
            for dr, dc in directions:
                max_minutes = max(max_minutes, dfs(r + dr, c + dc, minutes + 1))
            
            return max_minutes
        
        max_time = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:  
                    max_time = max(max_time, dfs(r, c, 0))
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: 
                    return -1
        
        return max_time - 1

# Example grid
# grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
grid = [[2,1,1],[0,1,1],[1,0,1]]
solution = Solution()
result = solution.orangesRotting(grid)
print(f"Minutes to rot all oranges: {result}")
