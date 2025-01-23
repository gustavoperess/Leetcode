from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:     
        result: list = []
        for i in range(len(A)):
            subA: list = A[:i + 1]
            subB: list = B[:i + 1]
            v = sum(1 for item in subA if item in subB)
            result.append(v)
            
        return result
      
        



input = Solution()
result = input.findThePrefixCommonArray(A = [1,3,2,4], B = [3,1,2,4])
