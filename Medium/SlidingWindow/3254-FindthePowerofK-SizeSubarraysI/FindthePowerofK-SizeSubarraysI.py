from typing import List                
 
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        l = 0
        concecutive_numers = 1
        ans = []
        for r in range(len(nums)):
            if r > 0 and nums[r - 1] + 1 == nums[r]:
                concecutive_numers += 1
            
            if r - l + 1 > k:
                if nums[l] + 1 == nums[l + 1]:
                    concecutive_numers -= 1
                l += 1
            
            if r - l + 1 == k:
                if concecutive_numers == k:
                    ans.append(nums[r])
                else:
                    ans.append(-1)
                    #print(concecutive_numers, nums[r])
    
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        l = 0
        hashMap = {}
        flips = 0
        for r in range(len(nums)):
            if r >= k and (r - k) in hashMap:
                flips -= hashMap[r - k]
            
            if flips % 2 == 1:
                nums[r] = 1 - nums[r]
            
            if nums[r] == 0:
                hashMap[r] = 1
                flips += 1
            
            print(hashMap, flips)
            

    
    
    
result = Solution()
result.minKBitFlips( nums = [0,0,0,1,0,1,1,0], k = 3)
#result.resultsArray( nums = [2,2,2,2,2], k = 4)