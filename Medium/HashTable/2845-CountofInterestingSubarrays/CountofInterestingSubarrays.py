
from typing import List

class Solution:        
       def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
            res = 0
            curr_sum = 0
            hashMap = {0: 1}
            
            for v in nums:
                if v % modulo == k:
                    curr_sum += 1
                
                target = (curr_sum - k) % modulo
                
                if target in hashMap:
                    res += hashMap[target]
                    
                if (curr_sum % modulo)in hashMap:
                    hashMap[curr_sum % modulo] += 1
                else:
                    hashMap[curr_sum % modulo] = 1
            return res
        
                    
  
        
result = Solution()
result.countInterestingSubarrays(nums = [3,2,4], modulo = 2, k = 1)
result.countInterestingSubarrays(nums = [3,1,9,6], modulo = 3, k = 0)







