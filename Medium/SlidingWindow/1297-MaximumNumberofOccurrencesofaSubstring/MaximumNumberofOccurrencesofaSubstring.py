

from typing import List
class Solution:
 def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        hashMap = {}
        l = 0
        seen = {}
        for r in range(len(s)):
            if s[r] in hashMap:
                hashMap[s[r]] += 1
            else:
                hashMap[s[r]] = 1
                
            if r - l + 1 > minSize:
                hashMap[s[l]] -= 1
                if hashMap[s[l]] == 0:
                    del hashMap[s[l]]
                l += 1
            if r - l + 1  == minSize and len(hashMap) <= maxLetters:
                substring = s[l:r + 1]
                if substring in seen:
                    seen[substring] += 1
                else:
                    seen[substring] = 1
        return max(seen.values(), default=0)
    


result = Solution()
result.maxFreq( s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4)