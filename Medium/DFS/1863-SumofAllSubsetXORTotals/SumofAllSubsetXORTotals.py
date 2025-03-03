
from typing import List
import math
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, curr_number):
            if i >= len(nums):
                return curr_number
            include = dfs(i + 1, curr_number ^ nums[i])
            exclude = dfs(i + 1, curr_number)
            return include + exclude
        
        result = dfs(0, 0)
        
        return result
    def decode(self, encoded: List[int], first: int) -> List[int]:
        firstV = [first]
        for i in encoded:
            t = firstV[-1] ^ i
            firstV.append(t)
        print(firstV)            

result = Solution()
result.decode(encoded = [1,2,3], first = 1)