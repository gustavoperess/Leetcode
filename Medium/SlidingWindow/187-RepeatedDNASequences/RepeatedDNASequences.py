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
        print()
        return ans
        
        


result = Solution()
result.findRepeatedDnaSequences( s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")