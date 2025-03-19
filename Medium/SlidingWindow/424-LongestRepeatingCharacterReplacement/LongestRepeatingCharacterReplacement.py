

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        l = 0
        ans = 0
        for r in range(len(s)):
            if s[r] in hashMap:
                hashMap[s[r]] += 1
            else:
                hashMap[s[r]] = 1
            
            while (r - l + 1) - max(hashMap.values()) > k:
                hashMap[s[l]] -= 1
                if hashMap[s[l]] == 0:
                    del hashMap[s[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans 
            


            
        
        
result = Solution()
result.characterReplacement(s = "AABABBA", k = 1)