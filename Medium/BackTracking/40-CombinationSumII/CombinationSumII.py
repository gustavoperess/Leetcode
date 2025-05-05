from typing import List

class Solution:
    def combinationSum2BruteForce(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets = []
        res = set()
        candidates.sort()
        def dfs(i, total):
            if total == target:
                res.add(tuple(subsets))
                return
        
            if i == len(candidates) or total > target:
                return
            
            subsets.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            subsets.pop()
            dfs(i + 1, total)

        dfs(0, 0)

     
        r = [list(i) for i in res]
        return res
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets = []
        res = []
        candidates.sort()
        def dfs(i, total):
            if total == target:
                res.append(subsets.copy())
                return
        
            if i == len(candidates) or total > target:
                return
            
            subsets.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            subsets.pop()
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total)

        dfs(0, 0)

     
        print(res)
        return res

result = Solution()
#result.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8)
# result.combinationSum2(candidates = [2,5,2,1,2], target = 5)
result.combinationSum2(candidates = [4,4,2,1,4,2,2,1,3], target = 6)