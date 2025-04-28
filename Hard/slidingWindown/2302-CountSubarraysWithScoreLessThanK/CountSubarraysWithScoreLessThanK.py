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
        


result = Solution()
#result.countSubarrays(nums = [2,1,4,3,5], k = 10)
#result.countSubarrays(nums = [1,1,1], k = 5)