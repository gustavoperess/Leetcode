
from typing import List
from collections import Counter

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ss = (s + s)[1:-1]
        if s in ss:
            return True
        return False

    def longestNiceSubstring(self, s: str) -> str:
        if not s: return "" 
        ss = set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in ss: 
                s0 = self.longestNiceSubstring(s[:i])
                s1 = self.longestNiceSubstring(s[i+1:])
                return max(s0, s1, key=len)
        
        return s
    
    def arrayPairSum(self, nums: List[int]) -> int:
        arr = []
        nums.sort()
        ans = 0
        for i in range(0, len(nums), 2):
            ans += nums[i]
        return ans
    
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            if len(set(Counter(word[:i]+word[i+1:]).values()))==1:
                return True
        return False
    
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        s = [sorted(i) for i in grid]
        l = 0
        r = len(grid) 
        hashMap = {}
        while l < r:
            k = 0
            while k < len(s[0]):
                if k in hashMap:
                    hashMap[k].append(s[l][k])
                else:
                    hashMap[k] = [s[l][k]]
                k += 1
            l += 1
        ans = 0
        for i in hashMap.values():
            ans += max(i)
        return ans
              
        
        
result = Solution()
# result.longestNiceSubstring( s = "YazaAay")
# result.longestNiceSubstring( s = "BebjJE")
# result.arrayPairSum( nums = [6,2,6,5,1,2])
# result.repeatedSubstringPattern(s = "abcabcabcabc")
result.equalFrequency(word = "abbcc")# true
# result.equalFrequency(word = "bac")# true
# result.equalFrequency(word = "aazz") # true
result.deleteGreatestValue(grid = [[1,2,4],[3,3,1]])