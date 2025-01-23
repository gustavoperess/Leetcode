from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        answer = {}
        for row in matrix:
            first = row[0]
            canonical = ""
            for i in row:
                canonical += '1' if i == first else '0'
            answer[canonical] = answer.get(canonical, 0) + 1
        

        return answer
    

result = Solution()
# result.maxEqualRowsAfterFlips([[1,0,0,0,1,1,1,0,1,1,1],[1,0,0,0,1,0,0,0,1,0,0],[1,0,0,0,1,1,1,0,1,1,1],[1,0,0,0,1,0,0,0,1,0,0],[1,1,1,0,1,1,1,0,1,1,1]])
# result.maxEqualRowsAfterFlips([[0,1],[1,0]])
result.maxEqualRowsAfterFlips(matrix = [[0,0,0],[0,0,1],[1,1,0]])