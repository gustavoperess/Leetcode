
from typing import List

class Solution:        
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix  = 0
        sufix = sum(nums)
        for i, x in enumerate(nums):
            prefix += x
            if prefix == sufix:
                return i
            sufix -= x
        return -1
        
        
result = Solution()
result.findMiddleIndex(nums = [1,-1,4])
