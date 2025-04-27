from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):
            s = nums[i] + nums[i + 2]
            if nums[i + 1] / 2 == s:
                count += 1
        return count
        
    def countSubarraysTwo(self, nums: List[int], minK: int, maxK: int) -> int:
        # hashMap = {}
        # l = 0
        # ans = 0
        # for r in range(len(nums)):
        #     if nums[r] in hashMap:
        #         hashMap[nums[r]] += 1
        #     else:
        #         hashMap[nums[r]] = 1
            
        
        #     while hashMap and min(hashMap.keys()) < minK:
        #         hashMap[nums[l]] -= 1
        #         if hashMap[nums[l]] == 0:
        #             del hashMap[nums[l]]
        #         l += 1
                
                
        #     while hashMap and max(hashMap.keys()) > maxK:
        #         hashMap[nums[l]] -= 1
        #         if hashMap[nums[l]] == 0:
        #             del hashMap[nums[l]]
        #         l += 1

        #     if minK in hashMap and maxK in hashMap:
        #         print(hashMap, r - len(nums))
        #         # ans += hashMap[minK] 
        last_minK = last_maxK = last_invalid = -1
        ans = 0
        
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                last_invalid = i
            if num == minK:
                last_minK = i
            if num == maxK:
                last_maxK = i
            
            ans += max(0, min(last_minK, last_maxK) - last_invalid)
        return ans
                
result = Solution()
#result.countSubarraysTwo(nums = [1,2,3,4,5,6,7,8], minK = 3, maxK = 6)
result.countSubarraysTwo(nums = [1,3,5,2,7,5], minK = 1, maxK = 5)
result.countSubarraysTwo(nums = [1,1,1,1], minK = 1, maxK = 1)
result.countSubarraysTwo(nums =[35054,398719,945315,945315,820417,945315,35054,945315,171832,945315,35054,109750,790964,441974,552913] , minK= 35054,maxK= 945315 )
