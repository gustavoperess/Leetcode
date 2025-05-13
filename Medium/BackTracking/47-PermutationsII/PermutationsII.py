from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        used = [False] * n
        ans = []
        def backtrack(path):
            if len(path) == n:
                ans.append(path[:])
                return
                
            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
        
                used[i] = True
                backtrack(path + [nums[i]])
                used[i] = False
                
        backtrack([])
      
        return ans
    
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        ans = []
        def backtrack(index, cursum):
            if cursum == target:
                ans.append(path.copy())
                return
            if len(candidates) == index or cursum >= target:
                return
            
            path.append(candidates[index])
            backtrack(index, cursum + candidates[index])
            path.pop()
            backtrack(index + 1, cursum)
            
            
        
        backtrack(0, 0)
        return ans
    
    def getHappyString(self, n: int, k: int) -> str:
        happyStrings = ['a', 'b', 'c']
        path = []
        ans = []
        def backtrack():
            if len(path) == n:
                ans.append("".join(path))
                return
            
            for i in range(len(happyStrings)):
                if path and happyStrings[i] == path[-1]:
                    continue
                path.append(happyStrings[i])
                backtrack()
                path.pop()
    
        backtrack()
        if k > len(ans):
            return ""
        return ans[k -1]
    
    
result = Solution()
result.getHappyString( n = 3, k = 9)
result.getHappyString( n = 1, k = 4)
result.getHappyString(n = 1, k = 3)
#result.lengthAfterTransformations(s = "v", t = 7)
#result.combinationSum(candidates = [2,3,6,7], target = 7)
# result.permuteUnique(nums = [1,2,3])
#result.permuteUnique(nums = [1])
#result.permuteUnique(nums = [1,1,2])

