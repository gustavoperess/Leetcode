
from typing import List
from itertools import permutations 
 
class Solution:        
    def checkPowersOfThree(self, n: int) -> bool:
        x = 2
        powers = []
        power = 0
        
        while 3 ** power <= n:
            k = 3 ** power
            x += k
            if k == n:
                return True
            powers.append(k)
            power += 1
      

        def dfs(i, total):
            if total == n:
                return True
            if i == len(powers) or total > n:
                return False
            
            if dfs(i  + 1, total + powers[i]):
                return True
            return dfs(i + 1, total)
        
        return dfs(0, 0)
        
            
    
        
        
result = Solution()
print(result.checkPowersOfThree(91))



