from typing import List

class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(nums)):
            while stack and nums[i] < stack[-1]:
                stack.pop()
            stack.append(nums[i])
            ans += len(stack)
        return ans
               
        
        
        
        


result = Solution()
#result.validSubarrays(nums = [1,4,2,5,3])
result.validSubarrays(nums = [2,2,2])