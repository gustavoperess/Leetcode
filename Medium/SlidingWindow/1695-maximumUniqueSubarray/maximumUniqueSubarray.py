from typing import List


def maximumUniqueSubarray(nums: List[int]) -> int:
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

def countSubarrays(nums: List[int], k: int) -> int:
    hashMap = {}
    l = 0
    m = max(nums)
    count = 0
    for r in range(len(nums)):
        if nums[r] in hashMap:
            hashMap[nums[r]] += 1
        else:
            hashMap[nums[r]] = 1
            
        if nums[r] == m:
            count += 1
    
        
        if count >= k:
            print(count, hashMap)
        # while max(hashMap.values()) >= k:
        #     #print(hashMap,l, r)
        #     hashMap[nums[l]] -= 1
        #     if hashMap[nums[l]] == 0:
        #         del hashMap[nums[l]]
        #     l += 1
       

        
# maximumUniqueSubarray(nums = [4,2,4,5,6])
countSubarrays(nums = [1,3,2,3,3], k = 2)
#countSubarrays(nums=[28,5,58,91,24,91,53,9,48,85,16,70,91,91,47,91,61,4,54,61,49], k=1)