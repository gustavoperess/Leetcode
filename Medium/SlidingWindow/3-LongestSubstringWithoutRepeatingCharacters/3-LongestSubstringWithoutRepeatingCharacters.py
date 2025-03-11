

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # l, r = 0,0
        # ans = 0
        # seen = set()
        # while l <= len(s) - 1:
        #     if s[l] not in seen:
        #         seen.add(s[l])
        #         l += 1
        #     else:
        #         seen = set()
        #         r += 1
        #         l = r
        #     ans = max(ans, len(seen))

        # return ans
    
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, len(charSet))
        return res




result = Solution()
result.lengthOfLongestSubstring(s = "abcabcbb")