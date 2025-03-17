
from typing import List

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        if len(word) < 5:
            return 0
        hashMap = {}
        l = 0
        seen = set()
        vowels = ["a", "e", "i", "o", "u"]
        position = 1  
        lastAdded = "a"
        ans = 0
        for r in range(len(word)):
            if word[r] in hashMap:
                hashMap[word[r]] += 1
            else:
                hashMap[word[r]] = 1
            
            if set(hashMap.keys()).issuperset(vowels):  
    
                if word[l] == lastAdded:
                    seen.add(word[l])
                elif position < len(vowels) and word[l] == vowels[position]:
                    lastAdded = word[l]
                    seen.add(word[l])
                    position += 1
            
            
                hashMap[word[l]] -= 1
                if hashMap[word[l]] == 0:
                    del hashMap[word[l]]
                l += 1
                
                
    def divideArray(self, nums: List[int]) -> bool:
        hashMap = {}
        for n in nums:
            if n in hashMap:
                hashMap[n].append(n)
            else:
                hashMap[n] = [n]
        
        for i in hashMap.values():
            if len(i) % 2 == 1:
                return False
        return True
    
    
    def maximumLengthSubstring(self, s: str) -> int:
        hashMap = {}
        l = 0
        ans = 0
        for r in range(len(s)):
            if s[r] in hashMap:
                hashMap[s[r]] += 1
            else:
                hashMap[s[r]] = 1
            
            while hashMap[s[r]] > 2:
                hashMap[s[l]] -= 1
                l += 1
            # while any(count > 2 for count in hashMap.values()):
            #     hashMap[s[l]] -= 1
            #     if hashMap[s[l]] == 0:
            #         del hashMap[s[l]]  
            #     l += 1  
            ans = max(ans, r - l + 1)
        return ans
    
    def divisorSubstrings(self, num: int, k: int) -> int:
        number = str(num)
        count = 0
        for i in range(0, len(number) - k + 1):
            n = int(number[i:i + k])
            if n > 0:
                if int(num) % n == 0:
                    count += 1
        return count
      
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        k -= 1
        min_diff = float("inf")
        for i in range(0,len(nums) - k):   
            min_diff = min(min_diff, nums[i+k]-nums[i])
        #     window = nums[i:i + k]
        #     diff = abs(-sum(abs(window[j + 1] - window[j]) for j in range(len(window)- 1)))
        #     ans = min(ans, diff)
        return min_diff
    
    def numOfSubarraysTLE(self, arr: List[int], k: int, threshold: int) -> int:
        # TLE
        hashMap = {}
        l = 0
        ans = 0
        for i in range(len(arr)):
            if arr[i] in hashMap:
                hashMap[arr[i]] += 1
            else:
                hashMap[arr[i]] = 1
            
            while sum(hashMap.values()) == k:
                for key, value in hashMap.items():
                    s +=  key * value
                if s / k >= threshold:
                    ans += 1
                hashMap[arr[l]] -= 1
                if hashMap[arr[l]] == 0:
                    del hashMap[arr[l]]
                l += 1
        return ans
    
    
        
result =Solution()
# result.maximumLengthSubstring(s = "bcbbbcba")
# result.divideArray(nums = [3,2,3,2,2,2])
# result.divisorSubstrings(num = 240, k = 2)

#result.longestSubarray(nums = [1,1,0,1])
#result.longestSubarray(nums = [1,1,1])