from collections import Counter
from typing import List
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        hashMap = {}
        ans = 0
        l = 0
        for r in range(len(s)):
            if s[r] in hashMap:
                hashMap[s[r]] += 1
            else:
                hashMap[s[r]] = 1
            
            while hashMap[s[r]] >= k:
                ans += len(s) - r
                hashMap[s[l]] -= 1
                l += 1
        
        return ans
    
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        count = 0
        hashMap = {}
        ans = 0
        numberTaken = cardPoints[0]
        l = numberTaken
        if numberTaken > len(cardPoints):
            return sum(cardPoints)
        
        for n in range(numberTaken, len(cardPoints)):
            if cardPoints[n] in hashMap:
                hashMap[cardPoints[n]] += 1
            else:
                hashMap[cardPoints[n]] = 1
            
            count += cardPoints[n]

            
            if sum(hashMap.values()) >= k - numberTaken:

                ans = max(ans, count)
                hashMap[cardPoints[l]] -= 1
                count -= cardPoints[l]
                if hashMap[cardPoints[l]] == 0:
                    del hashMap[cardPoints[l]]
                l += 1
       
        return ans + numberTaken
    
   
       
        
    

result = Solution()
result.numberOfSubstrings(s = "abcada", k = 2)