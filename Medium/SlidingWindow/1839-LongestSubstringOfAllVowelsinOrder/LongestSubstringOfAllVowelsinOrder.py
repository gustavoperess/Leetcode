
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
    
    
 
        
result =Solution()
# result.maximumLengthSubstring(s = "bcbbbcba")
# result.divideArray(nums = [3,2,3,2,2,2])
