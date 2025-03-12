from typing import List

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


    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * len(code)
        if k > 0:
            for i in range(1, n + 1):
                subarr = [code[(i + j) % n] for j in range(k)]
                ans[i - 1] = sum(subarr)
        if k < 0:
            for i in range(n -1,-1,-1):
                subarr = [code[(i - j - 1) % n] for j in range(abs(k))] 
                ans[i] = sum(subarr)
        return ans

result = Solution()
result.lengthOfLongestSubstring(s = "abcabcbb")
#result.decrypt(code = [5,7,1,4], k = 3)
result.decrypt(code = [2,4,9,3], k = 0)