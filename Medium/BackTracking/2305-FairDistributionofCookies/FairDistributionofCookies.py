from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        subset = []
        best = float("inf")
        def backtrack(index): 
            nonlocal best
            if index == len(cookies):
                best = min(best, max(subset))
                return
                
            if len(subset) < k:
                subset.append(cookies[index])
                backtrack(index + 1)
                subset.pop()
            
            for i in range(len(subset)):
                if subset[i] + cookies[index] < best:
                    subset[i] += cookies[index]
                    backtrack(index + 1)
                    subset[i] -= cookies[index] 
        
        backtrack(0)
        
   
        
result = Solution()
#result.distributeCookies(cookies = [6,1,3,2,2,4,1,2], k = 3)
result.numPairsDivisibleBy60( time = [30,20,150,100,40])
#result.numPairsDivisibleBy60( [418,204,77,278,239,457,284,263,372,279,476,416,360,18])
#result.numPairsDivisibleBy60(  time = [60,60,60])
#result.distributeCookies(cookies = [8,15,10,20,8], k = 2)