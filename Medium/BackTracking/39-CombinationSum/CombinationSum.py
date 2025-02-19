
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets = []
        result = []
        
        def dfs(i, total):
            if total == target:
                result.append(subsets.copy())
                return
            if i >= len(candidates) or total > target:
               return
           
            subsets.append(candidates[i])
            dfs(i, total + candidates[i])
            subsets.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)

        return result

result = Solution()
#result.combinationSum(candidates = [2,3,6,7], target = 7)
result.combinationSum(candidates = [2,3,5], target = 8)