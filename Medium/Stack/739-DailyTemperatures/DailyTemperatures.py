
from typing import List

# monotonic stack 

class Solution:    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)

        return ans
    
    def maxWidthRampBruteForce(self, nums: List[int]) -> int:
        # brute force
        maxWidth = 0
        for i in range(len(nums)):
            for y in range(i + 1, len(nums)):
                if nums[i] <= nums[y]:                
                    maxWidth = max(maxWidth, y- i)
        return maxWidth
    
    
    def maxWidthRamp(self, nums: List[int]) -> int:
        # Monotonic Stack 
        stack = []
        n = len(nums)
        ans = 0
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
                
        for j in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                x = stack.pop()
                ans = max(ans, j - x)
        return ans
                
    
result = Solution()
result.maxWidthRamp(nums = [9,8,1,0,1,9,4,0,4,1])
#result.maxWidthRamp(nums = [6,0,8,2,1,5])
result.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73])
