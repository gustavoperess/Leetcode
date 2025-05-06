
from typing import List
class Solution:
    def subsetsWithDuBruteForce(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        ans = set()
        nums.sort()
        def dfs(i):
            if i == len(nums):
                ans.add(tuple(subsets))
                return
            
            subsets.append(nums[i])
            dfs(i + 1)
            subsets.pop()
            dfs(i + 1)
        
        dfs(0)
        
        return [list(i) for i in ans]
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        nums.sort()
        ans = []
        def dfs(i):
            if i == len(nums):
                ans.append(subsets.copy())
                return
            
            subsets.append(nums[i])
            dfs(i + 1)
            subsets.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)
        
        dfs(0)
        return ans
        

result = Solution()
#result.subsetsWithDup(nums = [1,2,2])
result.subsetsWithDup(nums = [4,4,4,1,4])
