from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def dfs(i):
            # print(f"DFS called with i={i}, subset={subset}")  
    
            if i >= len(nums):  
                # print(f"  Reached end: Adding {subset.copy()} to result")
                res.append(subset.copy())  
                return
                
            # print(f"  Including {nums[i]}")
            subset.append(nums[i])
            dfs(i + 1)
    
            # print(f"  Excluding {nums[i]} (backtrack)")
            subset.pop()
            dfs(i + 1)
    
        dfs(0)
        print("Final Result:", res)
        return res

# Run function
result = Solution()
result.subsets(nums=[1, 2, 3])
