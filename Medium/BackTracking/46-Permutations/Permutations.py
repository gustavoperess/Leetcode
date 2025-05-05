

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        result = []
        def dfs():
            if len(subsets) == len(nums):
                result.append(subsets.copy())
            
            for x in nums:
                if x not in subsets:
                    subsets.append(x)
                    print(x, subsets)
                    dfs()
                    subsets.pop()
        
        dfs()

        print(result)
      


result = Solution()
result.permute(nums = [1,2,3])