
from typing import List

class Solution:    
    def subarraysDivByKBruteForce(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] % k == 0:
                count += 1
            for y in range(i + 1, len(nums)):
                if sum(nums[i: y + 1]) % k == 0:
                    count += 1
        return count
       
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0
        prefixSum = {0 : 1}
        for n in nums:
            currSum += n
            diff = currSum % k 
    
            if diff in prefixSum:
                res += prefixSum.get(diff, 0)
                prefixSum[diff] += 1
            else:
                prefixSum[diff] = 1
    
        return res
        
            
        
                    
  
        
result = Solution()
#result.subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5)
result.subarraysDivByK( nums = [5], k = 9)







