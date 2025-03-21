from typing import List


def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hashMap = {}
        l = 0
        ans = 0
        windown_sum = 0
        for r in range(len(nums)):
            if nums[r] in hashMap:
                hashMap[nums[r]] += 1
            else:
                hashMap[nums[r]] = 1
            
            windown_sum += nums[r]
            
   
            while hashMap[nums[r]] > 1:
                hashMap[nums[l]] -= 1
                windown_sum -= nums[l]
                if hashMap[nums[l]] == 0:
                    del hashMap[nums[l]]
                l += 1
     
            ans = max(ans, windown_sum)
               
        return ans
    

maximumUniqueSubarray(nums = [4,2,4,5,6])