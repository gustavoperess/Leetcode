from typing import List

class Solution:
    def numSubarraysWithSumBruteForce(self, nums: List[int], goal: int) -> int:
        count = 0
        for i in range(len(nums)):
            for y in range(i, len(nums)):                
                subArray = nums[i: y + 1]
                if sum(subArray) == goal:
                    count += 1
        
        return count

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(x):
            res, l ,curr_sum = 0,0,0
            for r in range(len(nums)):
                if x < 0:
                    return 0
                curr_sum += nums[r]
                
                while curr_sum > x:
                    curr_sum -= nums[l]
                    l += 1
                res += (r - l + 1)
            return res
        
        return helper(goal) - helper(goal - 1)
    
                 
    


result = Solution()
result.numSubarraysWithSum(nums = [1,0,1,0,1], goal = 2)
#result.numSubarraysWithSum(nums = [0,0,0,0,0], goal = 0)
result.numSubarraysWithSum(nums = [0,0,0,0,0], goal = 0)