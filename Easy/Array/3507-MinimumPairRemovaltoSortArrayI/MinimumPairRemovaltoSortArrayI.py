from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> List[int]:
            def is_non_decreasing(arr):
                return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
            
            def find_min_pair(nums):
                min_sum = float("inf")
                pos = 0
                for i in range(len(nums) - 1):
                    pair_sum = nums[i] + nums[i + 1]
                    if pair_sum < min_sum:
                        min_sum = pair_sum
                        pos = i
                return pos 
            
            nums = nums[:]
            count = 0


            while not is_non_decreasing(nums) and len(nums) > 1:
                pos = find_min_pair(nums)
                merged = nums[pos] + nums[pos + 1]
                nums[pos] = merged
                nums.pop(pos + 1)
                count += 1
            return count
        
                    

        

result = Solution()
result.minimumPairRemoval( nums = [5,2,3,1])
result.countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6)
result.countFairPairs(nums = [1,7,9,2,5], lower = 11, upper = 11)
result.minimumPairRemoval(nums = [1,2,2])