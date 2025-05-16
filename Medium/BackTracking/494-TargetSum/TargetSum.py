from typing import List
from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans  = 0
        @lru_cache(maxsize=None)
        def backtrack(index, curr_sum):  
            if index == len(nums):
                return 1 if curr_sum == target else 0
            return backtrack(index + 1, curr_sum + nums[index]) + backtrack(index + 1, curr_sum - nums[index])
                 
        return backtrack(0, 0)
        


result = Solution()
#t = result.findTargetSumWays(nums = [1,1,1,1,1], target = 3)
t = result.findTargetSumWays(nums = [10,12,16,24,3,38,24,35,45,20,12,18,25,24,1,26,9,18,29,28], target = 31)
print(t)
#result.findTargetSumWays(nums = [1], target = 2)