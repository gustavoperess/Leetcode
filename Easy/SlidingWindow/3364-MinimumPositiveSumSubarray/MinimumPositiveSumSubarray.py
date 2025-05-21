from typing import List
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        hashMap = {}
        left = 0
        minValue = float("inf")
        
        for right in range(len(nums)):
            while right - left + 1 > r:
                left += 1

                
            if right - left + 1 >= l:
                print(nums[left:right+1])


result = Solution()
result.minimumSumSubarray(nums = [3, -2, 1, 4], l = 2, r = 3)
#result.minimumSumSubarray(nums = [-2, 2, -3, 1], l = 2, r = 3)
#result.minimumSumSubarray(nums = [5,8,-6], l = 1, r = 3)