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
                print(path, used)
                used[i] = True
                backtrack(path + [nums[i]])
                used[i] = False
                
        backtrack([])
      
        return ans


result = Solution()
result.permuteUnique(nums = [1,1,2])
# result.permuteUnique(nums = [1,2,3])
#result.permuteUnique(nums = [1])