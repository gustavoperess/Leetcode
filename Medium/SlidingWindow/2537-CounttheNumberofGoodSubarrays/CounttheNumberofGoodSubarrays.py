
from typing import List
from collections import Counter

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        N  = len(nums)
        l, total, pairs = 0,0,0
        seen = Counter()
        for r in range(N):
            pairs += seen[nums[r]]
            seen[nums[r]] += 1
            
            while pairs >= k:
                seen[nums[l]] -= 1
                pairs -= seen[nums[l]]
                l += 1
            total += l
        
        return total
                


result = Solution()
result.countGood(nums = [3,1,4,3,2,2,4], k = 2)
# result.countGood(nums = [2,3,3,3,3,1,3,1,3,2], k = 19)
# result.countGood(nums = [1,1,1,1,1], k = 10)