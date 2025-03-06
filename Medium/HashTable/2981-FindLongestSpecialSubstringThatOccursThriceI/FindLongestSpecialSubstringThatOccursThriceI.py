from typing import Counter, List

class Solution:
    def maximumLength(self, s: str) -> int:
        freq = Counter()
        n = len(s)
        for i in range(n):
            substring = ""
            for y in range(i, n):
                if s[i] == s[y]:
                    substring += s[y]
                    freq[substring] += 1
                else:
                    break
        maxLen = -1
        for key, val in freq.items():
            if val >= 3:
                maxLen = max(maxLen, len(key))
        return maxLen
    

result = Solution()

print(result.maximumLength(s = "abcaba"))
# result.maximumLength(s = "aabcaba")