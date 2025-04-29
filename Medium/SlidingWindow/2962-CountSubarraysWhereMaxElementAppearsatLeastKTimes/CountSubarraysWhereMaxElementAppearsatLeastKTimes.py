
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        hashMap = {}
        l = 0
        mValue = max(nums)
        ans = 0
        for r in range(len(nums)):
            if nums[r] in hashMap:
                hashMap[nums[r]] += 1
            else:
                hashMap[nums[r]] = 1
           
            while mValue in hashMap and hashMap[mValue] >= k:
                    ans +=  len(nums) - r
                    hashMap[nums[l]] -= 1
                    if hashMap[nums[l]] == 0:
                        del hashMap[nums[l]]
                    l += 1
              

        return ans
            
        
        


result = Solution()
#result.countSubarrays(nums = [1,3,2,3,3], k = 2)
# result.countSubarrays(nums = [1,4,2,1], k = 3)
result.countSubarrays(nums = [28,5,58,91,24,91,53,9,48,85,16,70,91,91,47,91,61,4,54,61,49], k = 1)