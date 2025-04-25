
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0
        prefixSum = {0 : 1}
        
        for n in nums:
            currSum += n
            diff = currSum - k
            
            if diff in prefixSum:
                res += prefixSum[diff]
            
            if currSum in prefixSum:       
                prefixSum[currSum] += 1
            else:
                prefixSum[currSum] = 1
    
        return res


result = Solution()
# result.subarraySum(nums = [1,1,1], k = 2)
# result.subarraySum(nums = [1,2,3], k = 3)
# result.subarraySum([1,2,1,2,1], 3)
result.subarraySum([1,-1,0], 0)




