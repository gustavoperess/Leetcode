

from typing import List

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        ans = [0] * (N + 1)
        for p,f in queries:
            ans[p] += 1
            ans[f + 1] -= 1

        
    def pivotInteger(self, n: int) -> int:
        left_sum, right_sum = 0,  n * (n + 1) // 2
        for i in range(1, n + 1):
            left_sum += i
            if left_sum == right_sum:
                return i
            right_sum -= i
     
        return - 1  
        
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        l, ans = 0, 0
        for i in range(len(nums)):
            l += nums[i]
            if l == 0:
                ans += 1
        return ans
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        t = [0] * 51
        for r,l in ranges:
            t[r] += 1
            t[l +1] -= 1
        for i in range(1, len(t)):
            t[i] += t[i - 1]
        return min(t[left:right + 1]) >= 0
            
    
result = Solution()
#result.isCovered(ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5)
result.isCovered(ranges = [[37,49],[5,17],[8,32]], left = 29, right = 49)
# result.isCovered(ranges = [[1,5]], left = 1, right = 5)


