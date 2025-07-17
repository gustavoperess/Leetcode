from collections import defaultdict
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashMap = {}
        l = 0
        result = {}
        for r in range(len(s)):
            if s[r] in hashMap:
                hashMap[s[r]] += 1
            else:
                hashMap[s[r]] = 1
            
            while sum(hashMap.values()) >= 10:
                if s[l:r + 1] in result:
                    result[s[l:r + 1]] += 1
                else:
                    result[s[l:r + 1]] = 1
                hashMap[s[l]] -= 1
                if hashMap[s[l]] == 0:
                    del hashMap[s[l]]
                l += 1
            
        ans = [key for key,value  in hashMap.items() if value >= 2]
        return ans
    
    
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for y in range(i + 1, len(words)):
                x = words[y]
                if x.startswith(words[i]) and x.endswith(words[i]):
                    count += 1
                
    
        return count
    
    def kthCharacter(self, k: int) -> str:
        prev = ""
        ans = ""
        word = "a"
        while len(word) < k:
            next_part = ''
            for ch in word:
                if ch == "z":
                    next_part += "a"
                else:
                    next_part += chr(ord(ch) + 1)
                
            word += next_part

        print(word)
         
            
            
            
       

result = Solution()

result.kthCharacter( k = 500)
#result.minOperations( boxes = "001011")
#result.countMatchingSubarrays(nums = [1,4,4,1,3,5,5,3], pattern = [1,0,-1])
result.countPrefixSuffixPairs( words = ["a","aba","ababa","aa"])
#result.countPrefixSuffixPairs( words = ["pa","papa","ma","mama"])