from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        subsets = []
        
        def backtrack(index):
            if len(subsets) == k:
                ans.append(subsets.copy())
                return
            
            for number in range(index, n + 1): 
                
                subsets.append(number)
                backtrack(number + 1)
                subsets.pop()
          
        
        backtrack(1)
        
        return ans
        
    



result = Solution()
result.combine(n=4, k = 2)
#result.combine(n=3, k = 3)
#result.combine(n = 1, k = 1)