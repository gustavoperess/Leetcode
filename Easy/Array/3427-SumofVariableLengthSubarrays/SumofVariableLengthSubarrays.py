from typing import List

class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            n = i - nums[i]
            if n < 0:
                n = 0
                res += sum(nums[n:i + 1])            
            else:
                res += sum(nums[n:i + 1])
        return res




result = Solution()
result.subarraySum(nums = [2,3,1])
result.subarraySum(nums = [3,1,1,2])