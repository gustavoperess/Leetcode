from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        original_len = len(nums)
        nums = nums + nums  # circular array simulation

        l = 0
        hashMap = {}

        for r in range(len(nums)):
            hashMap[nums[r]] = hashMap.get(nums[r], 0) + 1

            if (r - l + 1) == original_len:  
                print(hashMap)
            
                hashMap[nums[l]] -= 1
                if hashMap[nums[l]] == 0:
                    del hashMap[nums[l]]
                l += 1


result = Solution()
result.minSwaps( nums = [0,1,0,1,1,0,0])