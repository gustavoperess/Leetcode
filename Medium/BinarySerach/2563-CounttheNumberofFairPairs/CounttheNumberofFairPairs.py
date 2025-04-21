from typing import List

class Solution:
    def countFairPairsTLE(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        l, l1 = 0, 1
        count = 0
        while l < len(nums):
            while l1 < len(nums):
                if nums[l] + nums[l1] < lower:
                    l1 += 1
                elif nums[l] + nums[l1] > upper:
                    l += 1
                    l1 = l + 1
                else:
                    count += 1
                    l1 += 1
            l += 1
            l1 = l + 1
        return count
    
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        def countp(target):
            count = 0
            left = 0
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] <= target:
                    count += right - left
                    left += 1
                else:
                    right -= 1
            return count
        t1 = countp(upper)
        t2 = countp(lower - 1)
        return t1 - t2


result = Solution()
result.countFairPairs(nums = [0,1,4,4,5,7], lower = 3, upper = 6)
# result.countFairPairs(nums = [1,7,9,2,5], lower = 11, upper = 11)