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
    
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxNum = 0
        for i in range(len(nums)):
            for y in range(i, len(nums)):
                subarrays = abs(sum(nums[i: y + 1]))
                maxNum = max(maxNum, subarrays)
        return (maxNum)
      

result = Solution()
result.maxAbsoluteSum(nums = [1,-3,2,3,-4])
result.maxAbsoluteSum(nums = [2,-5,1,-4,3,-2])
