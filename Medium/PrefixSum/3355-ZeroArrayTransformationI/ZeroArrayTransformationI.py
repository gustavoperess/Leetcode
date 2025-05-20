
from typing import List
class Solution:
    def isZeroArrayTLE(self, nums: List[int], queries: List[List[int]]) -> bool:
        sub = [0] * len(nums)
        for q in queries:
            start, end = q
            for i in range(start, end + 1):
                nums[i] -= 1
        
        for i in nums:
            if i > 0:
                return False
        return True
    
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        N = len(nums)
        sub = [0] * (N + 1)
        for l, r in queries:
            sub[l] += 1
            sub[r + 1] -= 1
        
        x = sub[0]
        for i in range(1 ,len(sub)):
            sub[i] += x
            x = sub[i] 
        
        for i in range(N):
            if nums[i] > sub[i]:
                return False
        return True

result = Solution()
result.isZeroArray(nums = [4,3,2,1], queries = [[1,3],[0,2]])
#result.isZeroArray( nums = [1,0,1], queries = [[0,2]])
#result.isZeroArray( nums = [1,0,2,1,2], queries = [[0,2], [1,3], [0,4], [4,4]])