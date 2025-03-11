from typing import List
import math
class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        numtoConvert = grid[0][0]
        yCount = 0
        n = math.ceil(len(grid) / 2)
        hashMap = {}
        for c in range(n):
            if grid[c][c] != numtoConvert:
                yCount += 1
            if c < n - 1:
                x = (len(grid) - 1) - c
                if grid[c][x] != numtoConvert:
                    yCount += 1
        print(yCount)
  
    



