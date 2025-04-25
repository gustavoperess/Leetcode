
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
    
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
        for _ in range(2, n + 1):
            temp = curr
            curr = prev + curr
            prev = temp
        
        return curr
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        hashMap = {0: 1}
        count = 0
        isOdd = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                isOdd += 1
                
            if (isOdd - k) in hashMap:
                count += hashMap[isOdd - k]
            
            if isOdd in hashMap:
                hashMap[isOdd] += 1
            else:
                hashMap[isOdd] = 1
        
        return count
        

        
                    
    
                
        
        
result = Solution()


# result.longestNiceSubstring( s = "YazaAay")
# result.longestNiceSubstring( s = "BebjJE")
# result.arrayPairSum( nums = [6,2,6,5,1,2])
# result.repeatedSubstringPattern(s = "abcabcabcabc")
result.climbStairs(4)# 5

#result.numberOfSubarrays(nums = [1,1,2,1,1], k = 3)
result.numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2)
# result.equalFrequency(word = "bac")# true
# result.equalFrequency(word = "aazz") # true
result.deleteGreatestValue(grid = [[1,2,4],[3,3,1]])