from typing import Counter, List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        numbers = [i for y in grid for i in y]
        freq = [0] * (len(grid) * len(grid) + 1)
        freq[0] = 1 
        
        for i in range(len(numbers)):
            freq[numbers[i]]  += 1
        
        a = 0
        b = 0
        for i in range(len(freq)):
            if freq[i] == 2:
                a = i
            if freq[i] == 0:
                b = i
        return [a, b]

    
result = Solution()