
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # O(N) 
        
        currentSet = set(nums)
        res = 0
        
        for num in nums:
            if num - 1 not in currentSet:
                current_num = num
                current_streak = 1
                
                while current_num + 1 in currentSet:
                    current_num += 1
                    current_streak += 1
                    
                res = max(res, current_streak)
        return res
    
        # sort
        
    def longestConsecutiveSort(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        curr, streak = nums[0], 0 
        i = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            streak += 1
            curr += 1
            res = max(res, streak)
        
    
        return res
        

      

result = Solution()
result.longestConsecutive(nums = [2,20,4,10,3,4,5])
#result.longestConsecutive(nums = [0,3,2,5,4,6,1,1])
# result.longestConsecutive(nums = [100,4,200,1,3,2])
# result.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1])
# result.longestConsecutive(nums = [1,0,1,2])