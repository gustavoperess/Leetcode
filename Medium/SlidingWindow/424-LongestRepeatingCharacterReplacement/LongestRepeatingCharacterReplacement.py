


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] in hashMap:
                hashMap[s[r]] += 1 
            else:
                hashMap[s[r]] = 1
            
            while (r - l + 1) - max(hashMap.values()) > k:
                hashMap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
            
        
        
result = Solution()
result.characterReplacement(s = "AABABBA", k = 2)