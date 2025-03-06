from typing import Counter, List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        numbers = [i for y in grid for i in y]
        freq = [0] * (len(grid) * len(grid) + 1)
        freq[0] = 1 
        
        for i in range(len(numbers)):
            freq[numbers[i]]  += 1
        
        a = 0
        b = 0
        for i in range(len(freq)):
            if freq[i] == 2:
                a = i
            if freq[i] == 0:
                b = i
        return [a, b]

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