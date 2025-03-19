
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        min_length = float("inf")
        
        for r in range(len(nums)):
            total += nums[r]
            
            while total >= target:
                min_length = min(min_length, r - l + 1)
                total -= nums[l]
                l += 1

        return min_length if min_length != float("inf") else 0
    



result = Solution()
result.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])