from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        oddCount, prefixSum, mod = 0, 0, 1_000_000_007
        for i in arr:
            prefixSum += i
            oddCount += prefixSum % 2
        oddCount += (len(arr) - oddCount) * oddCount
        return oddCount % mod
    
        
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [0] * (n+1)
        for (a,b) in trust:
            trusted[a] -= 1
            trusted[b] += 1
        
        for i in range(1, len(trusted)):
            if trusted[i] == n-1:
                return i
        return -1
    

    
