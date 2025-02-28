
from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        sets = []
       
        def dfs(i, curr_number):
            if i >= len(nums):
                if len(sets) > 0:
                    subsets.append(sets.copy())
                return curr_number
         
            sets.append(nums[i])
            include = dfs(i + 1, curr_number ^ nums[i])
            
            sets.pop()
            exclude = dfs(i + 1, curr_number)
        
            return include + exclude
        result = dfs(0, 0)
        return result
    


result = Solution()
result.subsetXORSum(nums = [5,1,6])