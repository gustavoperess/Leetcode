from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        curr_sum = 0
        ans = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum * (r - l + 1) >= k:          
                curr_sum -= nums[l]
                l += 1
    
            ans += r - l + 1 
        return ans
    
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        maxEnding = nums[0]
        
        for i in range(1, len(nums)):
            maxEnding = max(maxEnding + nums[i], nums[i])
            res = max(res, maxEnding)
        
        return res
        


result = Solution()
result.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4])
#result.countSubarrays(nums = [2,1,4,3,5], k = 10)
#result.countSubarrays(nums = [1,1,1], k = 5)