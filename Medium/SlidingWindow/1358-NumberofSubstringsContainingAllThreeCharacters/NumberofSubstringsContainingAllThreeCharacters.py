from typing import List

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hashMap = {}
        n = len(s)
        l = 0
        ans = 0
        for r in range(n):
            if s[r] in hashMap:
                hashMap[s[r]] += 1
            else:
                hashMap[s[r]] = 1
            
            while len(hashMap.values()) >= 3:
                ans += n - r
                hashMap[s[l]] -= 1
                if hashMap[s[l]] == 0:
                    del hashMap[s[l]]
                l += 1
              
     
        return ans
    
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        count = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] % 2:
                k -= 1
                count = 0

            while not k:
                k += nums[l] % 2
                count += 1
                l += 1
            res += count
        


result = Solution()
#result.numberOfSubarrays(nums = [1,1,2,1,1], k = 3)
result.numberOfSubarrays( nums = [2,2,2,1,2,2,1,2,2,2], k = 2)
#result.numberOfSubstrings(s = "abcabc")
#result.numberOfSubstrings(s= "aaacb")