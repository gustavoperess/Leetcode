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



result = Solution()
result.numberOfSubstrings(s = "abcada", k = 2)