
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        subsets = []
        ans = []
        def dfs(i):
            if len(s) == i:
                ans.append(subsets.copy()) 
                return 
            
            for j in range(i, len(s)):
                if self.isPali(s, i,  j):
                    subsets.append(s[i:j + 1])
                    dfs(j + 1)
                    subsets.pop()
                    
        dfs(0)
        return ans
        
        
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    
    
        
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.count = 0
        def backtrack(self, start, path):
          
            for i in range(start, len(nums)):
                if path and abs(nums[i] - path[-1]) == k:
                    continue
                path.append(nums[i])
                backtrack(self, i + 1, path)
                path.pop()
            
        
        backtrack(self, 0, [])
        print(self.count)
        return self.count

result = Solution()
result.partition(s = "aab")
result.beautifulSubsets(nums = [4,2,5,9,10,3], k = 1)





