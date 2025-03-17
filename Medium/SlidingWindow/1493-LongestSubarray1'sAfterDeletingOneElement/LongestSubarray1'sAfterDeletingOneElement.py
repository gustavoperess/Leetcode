from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
            hashMap = {}
            l = 0
            zeroCount = 0
            ans = 0
            for i in range(len(nums)):
                if nums[i] in hashMap:
                    hashMap[nums[i]] += 1
                else:
                    hashMap[nums[i]] = 1
                
                if nums[i] == 0:
                    zeroCount += 1
            
                while zeroCount > 1:
                    hashMap[nums[l]] -= 1
                    if nums[l] == 0:
                        zeroCount -= 1
                    if hashMap[nums[l]] == 0:
                        del hashMap[nums[l]]
                    l += 1
                    
            
                ans = max(ans, i - l)
            return ans
        

result = Solution()
result.longestSubarray(nums = [0,1,1,1,0,1,1,0,1])

