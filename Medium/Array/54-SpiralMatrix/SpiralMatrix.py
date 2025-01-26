from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        directios = [[0, 1], [1, 0], [0, -1], [-1, 0]] #r, c
        res = []
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                print(matrix[row], matrix)
        
        
        return res        
  



result = Solution()
# result.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]])
result.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]])