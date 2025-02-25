
from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        oddCount, prefixSum, mod = 0, 0, 1_000_000_007
        for i in arr:
            prefixSum += i
            oddCount += prefixSum % 2
        oddCount += (len(arr) - oddCount) * oddCount
        print(oddCount, oddCount % mod, mod)
        return oddCount % mod
    
        


result = Solution()
result.numOfSubarrays(arr = [1,3,5])
# result.numOfSubarrays(arr=[1,2,3,4,5,6,7])
# result.numOfSubarrays(arr=[2,4,6])