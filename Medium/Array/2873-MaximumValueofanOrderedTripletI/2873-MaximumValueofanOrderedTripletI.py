from typing import List

class Solution:
    def maximumTripletValueBruteForce(self, nums: List[int]) -> int:
        #BRUTE FORCE WORKS , BUT WE CAN FIND A BETTER SOLUTION
        ans = 0 
        l = len(nums)
        for i in range(l):
            for y in range(i + 1, l):
                for x in range(y + 1, l):
                    calculation = (nums[i] -  nums[y]) * nums[x]
                    ans = max(ans, calculation)

        return ans
    
    
    def maximumTripletValue(self, nums: List[int]) -> int:
        #BRUTE FORCE WORKS , BUT WE CAN FIND A BETTER SOLUTION
        if len(nums) < 3:
            return 0
        max_result = 0
        max_value = nums[0]
        max_diff = 0
        for i in range(1, len(nums)):
            max_result = max(max_result, max_diff * nums[i])
            max_diff = max(max_diff, max_value - nums[i])
            max_value = max(max_value, nums[i])

        return max_result
        
        
result = Solution()
result.maximumTripletValue(nums = [12,6,1,2,7])
# result.maximumTripletValue( nums = [1,10,3,4,19])
# result.maximumTripletValue(nums = [1,2,3])
# result.maximumTripletValue([2,3,1])